"""Generate Text for ISIPedia Project
"""
import json
import os

from isipedia.jsonfiles import generate_variables, Config

class AreaReport:
  def __init__(self, **kw):
    vars(self).update(kw)


def process_area(indicator_name, area, input_foulder):
  data = _process_area(indicator_name, area, 'land', input_foulder)
  pop = _process_area(indicator_name, area, 'pop', input_foulder)
  data.update(pop)
  return AreaReport(**data)


def _add_times(res, k, val):
  # add times
  k += '_times'
  res[k] = round(val/100+1, 3) if val else None

  k += '_higher_or_lower'
  if not val:
    res[k] = None
  elif val > 100:
    res[k] = 'higher'
  else:
    res[k] = 'lower'  


def _process_area(indicator_name, area, land_or_pop, input_foulder):
  dirname = input_foulder+indicator_name+'/ISIMIP-projections/'+area

  if land_or_pop == 'land':
    land_or_pop_long = 'land-area-affected-by'
  else:
    land_or_pop_long = 'population-exposed-to'

  variables = generate_variables([indicator_name], [land_or_pop_long], 
    ['', 'absolute-changes', 'relative-changes'], ['versus-temperature-change', 'versus-timeslices'], 
    config=Config(cube_json=input_foulder))

  fmt = {
    'land-area-affected-by' : 'land',
    'population-exposed-to' : 'pop',
    'absolute-changes' : 'abs',
    'relative-changes' : 'rel',
    'versus-temperature-change' : 'tc',
    # 'versus-timeslices' : 'tp',
  }

  res = {}
  for v in variables:
    js = json.load(open(v.jsonfile(area)))
    data = js['data']

    climate_model_list = js['climate_model_list']
    impact_model_list = js['impact_model_list']

    if v.axis == 'versus-timeslices':
      # example: land_rcp26_abs_far_future      
      timeslices_list = [tuple(e) for e in js['timeslices_list']]
      scenarios_list = js['climate_scenario_list']
      time_tags = {
        "far_future" : (2081, 2100),
        "today" : (2001, 2020),
      }
      indices = {tag: timeslices_list.index(period) for tag, period in time_tags.items()}
      for scenario in scenarios_list:
        for tag, index in indices.items():
          k = '{land}_{rcp}_{abs}_{period}'.format(land=fmt[v.exposure], rcp=scenario, 
            abs=fmt.get(v.change, v.change), period=tag).replace('__', '_')
          val = data[scenario]['overall']['median'][index]
          res[k] = round(val, 3) if val else None

          if fmt.get(v.change) == 'rel': 
            _add_times(res, k, val)    

    elif v.axis == 'versus-temperature-change':
      temperature_list = js['temperature_list']
      # example: land_tc_rel_ov_md_2c
      for warming in [0, 1, 2, 3, 4]:
          k = '{}_tc_{}_ov_md_{}c'.format(fmt[v.exposure], fmt.get(v.change, v.change), warming).replace('__', '_')
          index = temperature_list.index(warming)
          val = data['overall']['median'][index]
          res[k] = round(val, 3) if val else None

          if fmt.get(v.change) == 'rel':
            _add_times(res, k, val)

          elif fmt.get(v.change) == 'abs':
            # add min/max for absolute changes

            data_list = [data[climate_model]['runs'][impact_model]['mean'][index] 
              for climate_model in climate_model_list for impact_model in impact_model_list]
            data_list = [e for e in data_list if e] # remove None
            minimum = min(data_list) if data_list else None
            maximum = max(data_list) if data_list else None

            k = 'minimum_{}_tc_{}_ov_md_{}c'.format(fmt[v.exposure], fmt.get(v.change, v.change), warming).replace('__', '_')
            res[k] = round(minimum, 3) if minimum else None
            k = 'maximum_{}_tc_{}_ov_md_{}c'.format(fmt[v.exposure], fmt.get(v.change, v.change), warming).replace('__', '_')
            res[k] = round(maximum, 3) if maximum else None


    else:
      raise ValueError(repr(v.axis))

  res[land_or_pop+'_substract_2_and_1'] = res[land_or_pop+'_tc_ov_md_2c'] - res[land_or_pop+'_tc_ov_md_1c']

  # pick a variable without relative/absolute in the name 
  for v in variables:
    if not v.change:
      js = json.load(open(v.jsonfile(area)))
      data = js['data']
      break

  # additional info
  country                = js['region']
  
  if country[len(country)-1] == 's':
    country_apostrophe   = js['region']+'’'
  else:
    country_apostrophe   = js['region']+'’s'
    
  # rank_land_tc_rel_2c        = '(ranking-value: '+land_or_pop_long+'-river-flood-relative-changes_ISIMIP-projections_versus-temperature-change_'+area+' value: position temperature:2)' #Should show ranking with regards to relative change in land area affected under 2 degrees temperature change
  # rank_land_tc_rel_2081_2100 = '(ranking-value: '+land_or_pop_long+'-river-flood-relative-changes_ISIMIP-projections_versus-timeslices_'+area+' value: position time:2081-2100  scenario: rcp60)'

  res.update({
          'indicator_short': js['indicator'].replace('-',' '), 
          'code':area,
          'name': country, 
          'apostrophe':country_apostrophe,

          'nb_climate_models' : len(climate_model_list),
          'nb_impact_models': len(impact_model_list), 

          # land exposed to
          land_or_pop+'_indicator' : js['variable'].replace('-',' '),
          land_or_pop+'_indicator_raw' : js['variable'],
          land_or_pop+'_indicator_capital': js['variable'].replace('-',' ').capitalize(),

          'rank_'+land_or_pop+'_tc_rel_2c':'(ranking-value: '+land_or_pop_long+'-river-flood-relative-changes_ISIMIP-projections_versus-temperature-change_'+area+' value: position temperature:2)', #Should show ranking with regards to relative change in land area affected under 2 degrees temperature change,
          'rank_'+land_or_pop+'_tc_rel_2081_2100':'(ranking-value: '+land_or_pop_long+'-river-flood-relative-changes_ISIMIP-projections_versus-timeslices_'+area+' value: position time:2081-2100  scenario: rcp60)',
  })

  return res



def process_indicator(indicator_name, input_foulder, output_foulder, country_names=None):

  ## Look world first
  # world_results = process_world(indicator_name, input_foulder, output_foulder)
  general_vars = ['nb_impact_models', 'nb_climate_models', 
  'land_indicator', 'indicator_short', 'pop_indicator', 'land_indicator_capital', 'pop_indicator_capital']
              # indicator_short=indicator_short,country=country,country_name=area,land_indicator_capital=land_indicator_capital,

  world_results = process_area(indicator_name, 'world', input_foulder)

  general = {k:getattr(world_results, k, 'UNDEFINED') for k in general_vars}

  text = open('templates/'+indicator_name+'_world.md').read().format(world=world_results, **general)      
          
  indicator_short = world_results.indicator_short
  output_foulder_local = output_foulder+indicator_short.replace(' ','-')+'/ISIMIP-projections/world'
  if not os.path.exists(output_foulder_local):
     os.makedirs(output_foulder_local)
  
  md_file = output_foulder_local+'/'+indicator_short.replace(' ','-')+'-world.md'
  with open(md_file, 'w') as f:
      f.write(text)
      
  # Going though all the countries in the list.
  if country_names is None:
    country_names = os.listdir (input_foulder+indicator_name+'/ISIMIP-projections')

  for country_name in country_names:
     if(country_name != 'oceans' and country_name != 'world'):
      #if(country_name == 'AFG'):
          print(indicator_name+ " - " +country_name)  
          country_results = process_area(indicator_name, country_name, input_foulder)
          general.update(vars(country_results))

          if (country_name != 'world'): 
           text = open('templates/'+indicator_name+'.md').read().format(
              country=country_results,
              world=world_results, **general)

           output_foulder_local = output_foulder+indicator_short.replace(' ','-')+'/ISIMIP-projections/'+country_name
           if not os.path.exists(output_foulder_local):
             os.makedirs(output_foulder_local)
          
           md_file = output_foulder_local+'/'+indicator_short.replace(' ','-')+'-'+country_name+'.md'
           with open(md_file, 'w') as f:
              f.write(text)



def main():

  import argparse

  parser = argparse.ArgumentParser()
  parser.add_argument('--indicators', nargs='*', help='scan all indicators by default')
  parser.add_argument('--areas', nargs='*', help='scan all areas by default')
  parser.add_argument('--input-folder', default='test-data', help='%(defaults)s')
  parser.add_argument('--output-folder', default='test-data', help='%(defaults)s')

  o = parser.parse_args()

  if not o.indicators:
    o.indicators = os.listdir (o.input_folder)  

  for indicator_name in o.indicators:
    process_indicator(indicator_name, o.input_folder+'/', o.output_folder+'/', country_names=o.areas)


if __name__ == '__main__':
  main()    