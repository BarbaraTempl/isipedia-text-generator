"""Generate Text for ISIPedia Project

Initially created Julian Hunt (IIASA) on 2018/04
"""

import json
import os
import numpy as np


def to_zero(text):
    
    if type(text) == str or str(text) == 'None':
      return 0
        
    else:
      return text 
     

class AreaReport:
  def __init__(self, **kw):
    vars(self).update(kw)


def process_area(indicator_name, area, input_foulder):
  data = _process_area(indicator_name, area, 'land', input_foulder)
  pop = _process_area(indicator_name, area, 'pop', input_foulder)
  data.update(pop)
  return AreaReport(**data)


def _process_area(indicator_name, area, land_or_pop, input_foulder):
  dirname = input_foulder+indicator_name+'/ISIMIP-projections/'+area

  if land_or_pop == 'land':
    land_or_pop_long = 'land-area-affected-by'
  else:
    land_or_pop_long = 'population-exposed-to'

  # Land affected by INDICATOR
  json_land_temperature_change_absolute_changes = dirname+'/'+land_or_pop_long+'-'+indicator_name+'-absolute-changes_ISIMIP-projections_versus-temperature-change_'+area+'.json'
  json_land_timeslices_absolute_changes = dirname+'/'+land_or_pop_long+'-'+indicator_name+'-absolute-changes_ISIMIP-projections_versus-timeslices_'+area+'.json' 

  json_land_temperature_change = dirname+'/'+land_or_pop_long+'-'+indicator_name+'_ISIMIP-projections_versus-temperature-change_'+area+'.json'
  json_land_timeslices = dirname+'/'+land_or_pop_long+'-'+indicator_name+'_ISIMIP-projections_versus-timeslices_'+area+'.json' 

  json_land_temperature_change_relative_changes = dirname+'/'+land_or_pop_long+'-'+indicator_name+'-relative-changes_ISIMIP-projections_versus-temperature-change_'+area+'.json'
  json_land_timeslices_relative_changes = dirname+'/'+land_or_pop_long+'-'+indicator_name+'-relative-changes_ISIMIP-projections_versus-timeslices_'+area+'.json' 

  # load JSON files  
  # Land affected by INDICATOR           
  with open(json_land_temperature_change_absolute_changes) as f:
       data_land_temperature_change_absolute_changes = json.load(f)                          
  with open(json_land_timeslices_absolute_changes) as f:
       data_land_timeslices_absolute_changes = json.load(f)      
  with open(json_land_temperature_change) as f:
       data_land_temperature_change = json.load(f)   
  with open(json_land_timeslices) as f:
       data_land_timeslices = json.load(f)                          
  with open(json_land_temperature_change_relative_changes) as f:
       data_land_temperature_change_relative_changes = json.load(f)   
  with open(json_land_timeslices_relative_changes) as f:
       data_land_timeslices_relative_changes = json.load(f)                          
   
  # Fill variables 
  # Land affected by INDICATOR     

  country                = data_land_timeslices['region']
  
  if country[len(country)-1] == 's':
    country_apostrophe   = data_land_timeslices['region']+'’'
  else:
    country_apostrophe   = data_land_timeslices['region']+'’s'
    
  land_indicator_raw     = data_land_timeslices['variable']
  land_indicator         = data_land_timeslices['variable'].replace('-',' ') 
  land_indicator_capital = data_land_timeslices['variable'].replace('-',' ').capitalize()
  indicator_short        = data_land_timeslices['indicator'].replace('-',' ')#land_indicator.replace('land area affected by ','') 

  climate_model_list     = len(data_land_timeslices['climate_model_list'])
  impact_model_list      = len(data_land_timeslices['impact_model_list'])                      
  
  land_tc_abs_ov_md_0c   = round(to_zero(data_land_temperature_change_absolute_changes['data']['overall']['median'][0]),3) 
  land_tc_abs_ov_md_1c   = round(to_zero(data_land_temperature_change_absolute_changes['data']['overall']['median'][2]),3) 
  land_tc_abs_ov_md_2c   = round(to_zero(data_land_temperature_change_absolute_changes['data']['overall']['median'][4]),3) 

  list_land_tc_abs_ov_md_1c = []
  for climate_model in data_land_timeslices['climate_model_list']:
      for impact_model in data_land_timeslices['impact_model_list']:
          list_land_tc_abs_ov_md_1c.append(round(to_zero(data_land_temperature_change_absolute_changes['data'][climate_model]['runs'][impact_model]['mean'][2]),3))
  minimum_land_tc_abs_ov_md_1c = min(list_land_tc_abs_ov_md_1c)
  maximum_land_tc_abs_ov_md_1c = max(list_land_tc_abs_ov_md_1c)

  list_land_tc_abs_ov_md_2c = []
  for climate_model in data_land_timeslices['climate_model_list']:
      for impact_model in data_land_timeslices['impact_model_list']:
          list_land_tc_abs_ov_md_2c.append(round(to_zero(data_land_temperature_change_absolute_changes['data'][climate_model]['runs'][impact_model]['mean'][4]),3))
  minimum_land_tc_abs_ov_md_2c = min(list_land_tc_abs_ov_md_2c)
  maximum_land_tc_abs_ov_md_2c = max(list_land_tc_abs_ov_md_2c)


  land_tc_rel_ov_md_0c   = round(to_zero(data_land_temperature_change_relative_changes['data']['overall']['median'][0]),3) 
  land_tc_rel_ov_md_1c   = round(to_zero(data_land_temperature_change_relative_changes['data']['overall']['median'][2]),3) 
  land_tc_rel_ov_md_2c   = round(to_zero(data_land_temperature_change_relative_changes['data']['overall']['median'][4]),3) 
  land_tc_rel_ov_md_1c_times = round(to_zero(data_land_temperature_change_relative_changes['data']['overall']['median'][2])/100+1,3)
  if land_tc_rel_ov_md_1c_times < 1:
     land_tc_rel_ov_md_1c_times_higher_or_lower = 'higher'
  else:
     land_tc_rel_ov_md_1c_times_higher_or_lower = 'lower'
  land_tc_rel_ov_md_2c_times = round(to_zero(data_land_temperature_change_relative_changes['data']['overall']['median'][4])/100+1,3)
     
  land_tc_ov_md_0c       = round(to_zero(data_land_temperature_change['data']['overall']['median'][0]),3) 
  land_tc_ov_md_1c       = round(to_zero(data_land_temperature_change['data']['overall']['median'][2]),3) 
  land_tc_ov_md_2c       = round(to_zero(data_land_temperature_change['data']['overall']['median'][4]),3) 
  land_substract_2_and_1 = round((land_tc_ov_md_2c - land_tc_ov_md_1c),3)
  land_tc_ov_md_1c_times = round((to_zero(data_land_temperature_change['data']['overall']['median'][2])/100+1),3)


  land_tc_rel_ov_md_2c   = round(to_zero(data_land_temperature_change_relative_changes['data']['overall']['median'][4]),3)   

  timeslices_list = [tuple(e) for e in data_land_timeslices['timeslices_list']]
  itoday = timeslices_list.index((2001, 2020))
  ifuture = timeslices_list.index((2081, 2100))

  land_pc_abs_today      = round(to_zero(data_land_timeslices_absolute_changes['data']['rcp60']['overall']['median'][itoday]),3)

  # land_pc_abs_far_future = round(to_zero(data_land_timeslices_absolute_changes['data']['piControl']['overall']['median'][ifuture]),3)
  # land_pc_rel_far_future = round(to_zero(data_land_timeslices_relative_changes['data']['piControl']['overall']['median'][ifuture]),3)

  land_rcp26_abs_far_future  = round(to_zero(data_land_timeslices_absolute_changes['data']['rcp26']['overall']['median'][ifuture]),3)
  land_rcp60_abs_far_future  = round(to_zero(data_land_timeslices_absolute_changes['data']['rcp60']['overall']['median'][ifuture]),3)
  land_rcp26_rel_far_future  = round(to_zero(data_land_timeslices_relative_changes['data']['rcp26']['overall']['median'][ifuture]),3)
  land_rcp60_rel_far_future  = round(to_zero(data_land_timeslices_relative_changes['data']['rcp60']['overall']['median'][ifuture]),3)
  land_rcp26_far_future      = round(to_zero(data_land_timeslices['data']['rcp26']['overall']['median'][ifuture]),3)
  land_rcp60_far_future      = round(to_zero(data_land_timeslices['data']['rcp60']['overall']['median'][ifuture]),3)
  land_rcp60_far_future_times = round((to_zero(data_land_timeslices['data']['rcp60']['overall']['median'][ifuture])/100+1),3)
  land_rcp26_far_future_times = round((to_zero(data_land_timeslices['data']['rcp26']['overall']['median'][ifuture])/100+1),3)
  land_rcp60_rel_far_future_times = round(to_zero(data_land_timeslices_relative_changes['data']['rcp60']['overall']['median'][ifuture])/100+1,3)
  land_rcp26_rel_far_future_times = round(to_zero(data_land_timeslices_relative_changes['data']['rcp26']['overall']['median'][ifuture])/100+1,3)

  rank_land_tc_rel_2c        = '(ranking-value: '+land_or_pop_long+'-river-flood-relative-changes_ISIMIP-projections_versus-temperature-change_'+area+' value: position temperature:2)' #Should show ranking with regards to relative change in land area affected under 2 degrees temperature change
  rank_land_tc_rel_2081_2100 = '(ranking-value: '+land_or_pop_long+'-river-flood-relative-changes_ISIMIP-projections_versus-timeslices_'+area+' value: position time:2081-2100  scenario: rcp60)'


  kw = dict(
          indicator_short=indicator_short, name=country, code=area,

          climate_model_list=climate_model_list,
          impact_model_list=impact_model_list, 
          apostrophe=country_apostrophe,

          # land exposed to
          land_indicator=land_indicator,
          land_indicator_raw=land_indicator_raw,
          land_indicator_capital=land_indicator_capital,

          land_substract_2_and_1=land_substract_2_and_1,

          land_tc_ov_md_0c=land_tc_ov_md_0c,
          land_tc_ov_md_1c=land_tc_ov_md_1c, land_tc_ov_md_1c_times = land_tc_ov_md_1c_times,
          land_tc_ov_md_2c=land_tc_ov_md_2c,
          land_tc_rel_ov_md_1c=land_tc_rel_ov_md_1c, land_tc_rel_ov_md_1c_times=land_tc_rel_ov_md_1c_times, land_tc_rel_ov_md_1c_times_higher_or_lower=land_tc_rel_ov_md_1c_times_higher_or_lower,
          land_tc_rel_ov_md_2c=land_tc_rel_ov_md_2c, land_tc_rel_ov_md_2c_times=land_tc_rel_ov_md_2c_times,
          land_tc_abs_ov_md_0c=land_tc_abs_ov_md_0c,
          land_tc_abs_ov_md_2c=land_tc_abs_ov_md_2c,
          
          # land_pc_abs_far_future=land_pc_abs_far_future,
          # land_pc_rel_far_future=land_pc_rel_far_future,

          land_rcp26_far_future=land_rcp26_far_future,
          land_rcp26_rel_far_future_times=land_rcp26_rel_far_future_times,
          land_rcp26_abs_far_future=land_rcp26_abs_far_future, 
          land_rcp60_far_future=land_rcp60_far_future, land_rcp60_far_future_times=land_rcp60_far_future_times,
          land_rcp60_rel_far_future=land_rcp60_rel_far_future, land_rcp60_rel_far_future_times=land_rcp60_rel_far_future_times,
          land_rcp60_abs_far_future=land_rcp60_abs_far_future,

          minimum_land_tc_abs_ov_md_1c=minimum_land_tc_abs_ov_md_1c,
          maximum_land_tc_abs_ov_md_1c=maximum_land_tc_abs_ov_md_1c,
          minimum_land_tc_abs_ov_md_2c=minimum_land_tc_abs_ov_md_2c,
          maximum_land_tc_abs_ov_md_2c=maximum_land_tc_abs_ov_md_2c,

          rank_land_tc_rel_2c=rank_land_tc_rel_2c,
          rank_land_tc_rel_2081_2100=rank_land_tc_rel_2081_2100,
  )

  if land_or_pop == 'pop':
    kwpop = {}
    for k, v in kw.items():
      kwpop[k.replace('land','pop')] = v
    return kwpop
  else:
    return kw



def process_indicator(indicator_name, input_foulder, output_foulder, country_names=None):

  ## Look world first
  # world_results = process_world(indicator_name, input_foulder, output_foulder)
  general_vars = ['impact_model_list', 'climate_model_list', 
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