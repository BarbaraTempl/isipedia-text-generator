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
     

def process_indicator(indicator_name, input_foulder, output_foulder):

  ## Look world first
  json_land_temperature_change_absolute_changes = input_foulder+indicator_name+'/ISIMIP-projections/world/land-area-affected-by-'+indicator_name+'-absolute-changes_ISIMIP-projections_versus-temperature-change_world.json'
  json_land_timeslices_absolute_changes = input_foulder+indicator_name+'/ISIMIP-projections/world/land-area-affected-by-'+indicator_name+'-absolute-changes_ISIMIP-projections_versus-timeslices_world.json' 
  json_land_years_absolute_changes = input_foulder+indicator_name+'/ISIMIP-projections/world/land-area-affected-by-'+indicator_name+'-absolute-changes_ISIMIP-projections_versus-timeslices_world.json'
 
  json_land_temperature_change = input_foulder+indicator_name+'/ISIMIP-projections/world/land-area-affected-by-'+indicator_name+'_ISIMIP-projections_versus-temperature-change_world.json'
  json_land_timeslices = input_foulder+indicator_name+'/ISIMIP-projections/world/land-area-affected-by-'+indicator_name+'_ISIMIP-projections_versus-timeslices_world.json' 
  json_land_years = input_foulder+indicator_name+'/ISIMIP-projections/world/land-area-affected-by-'+indicator_name+'_ISIMIP-projections_versus-timeslices_world.json'
 
  json_land_temperature_change_relative_changes = input_foulder+indicator_name+'/ISIMIP-projections/world/land-area-affected-by-'+indicator_name+'-relative-changes_ISIMIP-projections_versus-temperature-change_world.json'
  json_land_timeslices_relative_changes = input_foulder+indicator_name+'/ISIMIP-projections/world/land-area-affected-by-'+indicator_name+'-relative-changes_ISIMIP-projections_versus-timeslices_world.json' 
  json_land_years_relative_changes = input_foulder+indicator_name+'/ISIMIP-projections/world/land-area-affected-by-'+indicator_name+'-relative-changes_ISIMIP-projections_versus-timeslices_world.json'
 
  # Population exposed to INDICATOR
  json_pop_temperature_change_absolute_changes = input_foulder+indicator_name+'/ISIMIP-projections/world/population-exposed-to-'+indicator_name+'-absolute-changes_ISIMIP-projections_versus-temperature-change_world.json'
  json_pop_timeslices_absolute_changes = input_foulder+indicator_name+'/ISIMIP-projections/world/population-exposed-to-'+indicator_name+'-absolute-changes_ISIMIP-projections_versus-timeslices_world.json' 
  json_pop_years_absolute_changes = input_foulder+indicator_name+'/ISIMIP-projections/world/population-exposed-to-'+indicator_name+'-absolute-changes_ISIMIP-projections_versus-timeslices_world.json'
 
  json_pop_temperature_change = input_foulder+indicator_name+'/ISIMIP-projections/world/population-exposed-to-'+indicator_name+'_ISIMIP-projections_versus-temperature-change_world.json'
  json_pop_timeslices = input_foulder+indicator_name+'/ISIMIP-projections/world/population-exposed-to-'+indicator_name+'_ISIMIP-projections_versus-timeslices_world.json' 
  json_pop_years = input_foulder+indicator_name+'/ISIMIP-projections/world/population-exposed-to-'+indicator_name+'_ISIMIP-projections_versus-timeslices_world.json'
 
  json_pop_temperature_change_relative_changes = input_foulder+indicator_name+'/ISIMIP-projections/world/population-exposed-to-'+indicator_name+'-relative-changes_ISIMIP-projections_versus-temperature-change_world.json'
  json_pop_timeslices_relative_changes = input_foulder+indicator_name+'/ISIMIP-projections/world/population-exposed-to-'+indicator_name+'-relative-changes_ISIMIP-projections_versus-timeslices_world.json' 
  json_pop_years_relative_changes = input_foulder+indicator_name+'/ISIMIP-projections/world/population-exposed-to-'+indicator_name+'-relative-changes_ISIMIP-projections_versus-timeslices_world.json'
      
  # load JSON files  
  # Land affected by INDICATOR           
  with open(json_land_temperature_change_absolute_changes) as f:
       data_land_temperature_change_absolute_changes = json.load(f)                          
  with open(json_land_timeslices_absolute_changes) as f:
       data_land_timeslices_absolute_changes = json.load(f)      
  with open(json_land_years_absolute_changes) as f:
       data_land_years_absolute_changes = json.load(f)                          
  with open(json_land_temperature_change) as f:
       data_land_temperature_change = json.load(f)   
  with open(json_land_timeslices) as f:
       data_land_timeslices = json.load(f)                          
  with open(json_land_years) as f:
       data_land_years = json.load(f)                 
  with open(json_land_temperature_change_relative_changes) as f:
       data_land_temperature_change_relative_changes = json.load(f)   
  with open(json_land_timeslices_relative_changes) as f:
       data_land_timeslices_relative_changes = json.load(f)                          
  with open(json_land_years_relative_changes) as f:
       data_land_years_relative_changes = json.load(f)    
 
  # Population exposed to INDICATOR
  with open(json_pop_temperature_change_absolute_changes) as f:
       data_pop_temperature_change_absolute_changes = json.load(f)                          
  with open(json_pop_timeslices_absolute_changes) as f:
       data_pop_timeslices_absolute_changes = json.load(f)      
  with open(json_pop_years_absolute_changes) as f:
       data_pop_years_absolute_changes = json.load(f)                          
  with open(json_pop_temperature_change) as f:
       data_pop_temperature_change = json.load(f)   
  with open(json_pop_timeslices) as f:
       data_pop_timeslices = json.load(f)                          
  with open(json_pop_years) as f:
       data_pop_years = json.load(f)                 
  with open(json_pop_temperature_change_relative_changes) as f:
       data_pop_temperature_change_relative_changes = json.load(f)   
  with open(json_pop_timeslices_relative_changes) as f:
       data_pop_timeslices_relative_changes = json.load(f)
  with open(json_pop_years_relative_changes) as f:
       data_pop_years_relative_changes = json.load(f)    
   
  # Fill variables 
  # Land affected by INDICATOR     
  country                = data_land_years['region']
  
  if country[len(country)-1] == 's':
    country_apostrophe   = data_land_years['region']+'’'
  else:
    country_apostrophe   = data_land_years['region']+'’s'
    
  land_indicator_raw     = data_land_years['variable']
  land_indicator         = data_land_years['variable'].replace('-',' ') 
  land_indicator_capital = data_land_years['variable'].replace('-',' ').capitalize()
  indicator_short        = data_land_years['indicator'].replace('-',' ')#land_indicator.replace('land area affected by ','') 
 
  climate_model_list     = len(data_land_years['climate_model_list'])
  impact_model_list      = len(data_land_years['impact_model_list'])                      
  
  world_land_tc_abs_ov_md_0c   = round(to_zero(data_land_temperature_change_absolute_changes['data']['overall']['median'][0]),3) 
  world_land_tc_abs_ov_md_1c   = round(to_zero(data_land_temperature_change_absolute_changes['data']['overall']['median'][2]),3) 
  world_land_tc_abs_ov_md_2c   = round(to_zero(data_land_temperature_change_absolute_changes['data']['overall']['median'][4]),3) 
  world_list_land_tc_abs_ov_md_1c = []
  for climate_model in data_land_years['climate_model_list']:
      for impact_model in data_land_years['impact_model_list']:
          world_list_land_tc_abs_ov_md_1c.append(round(to_zero(data_land_temperature_change_absolute_changes['data'][climate_model]['runs'][impact_model]['mean'][2]),3))
  world_minimum_land_tc_abs_ov_md_1c = min(world_list_land_tc_abs_ov_md_1c)
  world_maximum_land_tc_abs_ov_md_1c = max(world_list_land_tc_abs_ov_md_1c)
 
  world_list_land_tc_abs_ov_md_2c = []
  for climate_model in data_land_years['climate_model_list']:
      for impact_model in data_land_years['impact_model_list']:
          world_list_land_tc_abs_ov_md_2c.append(round(to_zero(data_land_temperature_change_absolute_changes['data'][climate_model]['runs'][impact_model]['mean'][4]),3))
  world_minimum_land_tc_abs_ov_md_2c = min(world_list_land_tc_abs_ov_md_2c)
  world_maximum_land_tc_abs_ov_md_2c = max(world_list_land_tc_abs_ov_md_2c)
 
 
  world_land_tc_rel_ov_md_0c   = round(to_zero(data_land_temperature_change_relative_changes['data']['overall']['median'][0]),3) 
  world_land_tc_rel_ov_md_1c   = round(to_zero(data_land_temperature_change_relative_changes['data']['overall']['median'][2]),3) 
  world_land_tc_rel_ov_md_2c   = round(to_zero(data_land_temperature_change_relative_changes['data']['overall']['median'][4]),3) 
  world_land_tc_rel_ov_md_1c_times = round((to_zero(data_land_temperature_change_relative_changes['data']['overall']['median'][2])/100+1),3)
  if world_land_tc_rel_ov_md_1c_times < 1:
     world_land_tc_rel_ov_md_1c_times_higher_or_lower = 'higher'
  else:
     world_land_tc_rel_ov_md_1c_times_higher_or_lower = 'lower'
  world_land_tc_rel_ov_md_2c_times = round((to_zero(data_land_temperature_change_relative_changes['data']['overall']['median'][4])/100+1),3)
               
  world_land_tc_ov_md_0c       = round(to_zero(data_land_temperature_change['data']['overall']['median'][0]),3) 
  world_land_tc_ov_md_1c       = round(to_zero(data_land_temperature_change['data']['overall']['median'][2]),3) 
  world_land_tc_ov_md_2c       = round(to_zero(data_land_temperature_change['data']['overall']['median'][4]),3) 
  #world_land_substract_2_and_1 = round((land_tc_ov_md_2c - land_tc_ov_md_1c),3)
  world_land_tc_ov_md_1c_times = round((to_zero(data_land_temperature_change['data']['overall']['median'][2])/100+1),3)
 
 
  world_land_tc_rel_ov_md_2c   = round(to_zero(data_land_temperature_change_relative_changes['data']['overall']['median'][4]),3) 
 
  world_land_pc_abs_today      = round(to_zero(data_land_timeslices_absolute_changes['data']['rcp60']['overall']['median'][17]),3)
  world_land_pc_abs_far_future = round(to_zero(data_land_timeslices_absolute_changes['data']['piControl']['overall']['median'][21]),3)
  world_land_pc_rel_far_future = round(to_zero(data_land_timeslices_relative_changes['data']['piControl']['overall']['median'][21]),3)
 
  world_land_rcp26_abs_far_future  = round(to_zero(data_land_timeslices_absolute_changes['data']['rcp26']['overall']['median'][21]),3)
  world_land_rcp60_abs_far_future  = round(to_zero(data_land_timeslices_absolute_changes['data']['rcp60']['overall']['median'][21]),3)
  world_land_rcp26_rel_far_future  = round(to_zero(data_land_timeslices_relative_changes['data']['rcp26']['overall']['median'][21]),3)
  world_land_rcp60_rel_far_future  = round(to_zero(data_land_timeslices_relative_changes['data']['rcp60']['overall']['median'][21]),3)
  world_land_rcp26_far_future      = round(to_zero(data_land_timeslices['data']['rcp26']['overall']['median'][21]),3)
  world_land_rcp60_far_future      = round(to_zero(data_land_timeslices['data']['rcp60']['overall']['median'][21]),3)
  world_land_rcp60_far_future_times = round((to_zero(data_land_timeslices['data']['rcp60']['overall']['median'][21])/100+1),3)
  world_land_rcp26_far_future_times = round((to_zero(data_land_timeslices['data']['rcp26']['overall']['median'][21])/100+1),3)
  world_land_rcp60_rel_far_future_times = round((to_zero(data_land_timeslices_relative_changes['data']['rcp60']['overall']['median'][21])/100+1),3)
  world_land_rcp26_rel_far_future_times = round((to_zero(data_land_timeslices_relative_changes['data']['rcp26']['overall']['median'][21])/100+1),3)
 
  world_rank_land_tc_rel_2c        = '(ranking-value: land-area-affected-by-river-flood-relative-changes_ISIMIP-projections_versus-temperature-change_world value: position temperature:2)' #Should show ranking with regards to relative change in land area affected under 2 degrees temperature change
  world_rank_land_tc_rel_2c_high_or_low = 'high'#Can we make this flexible to the outcome: e.g. if the ranking is  <100 it is ‘high’, if the ranking is >100 it is ‘low’. Probably CDLX should provide this information. Or we need to calculate the rankings ourselves.
 
  world_rank_land_rcp60_rel_far_future  = '(ranking-value: land-area-affected-by-river-flood-relative-changes_ISIMIP-projections_versus-timeslices_world value: position time:2081-2100  scenario: rcp60)'
  world_rank_land_rcp60_rel_far_future_high_or_low = 'high' 
 
  # Population exposed to INDICATOR
  pop_indicator_raw         = data_pop_years['variable'] 
  pop_indicator             = data_pop_years['variable'].replace('-',' ') 
  pop_indicator_capital     = data_pop_years['variable'].replace('-',' ').capitalize()
  
  world_pop_tc_abs_ov_md_0c       = round(to_zero(data_pop_temperature_change_absolute_changes['data']['overall']['median'][0]),3) 
  world_pop_tc_abs_ov_md_1c       = round(to_zero(data_pop_temperature_change_absolute_changes['data']['overall']['median'][2]),3) 
  world_pop_tc_abs_ov_md_2c       = round(to_zero(data_pop_temperature_change_absolute_changes['data']['overall']['median'][4]),3) 
 
  world_pop_tc_rel_ov_md_0c       = round(to_zero(data_pop_temperature_change_relative_changes['data']['overall']['median'][0]),3) 
  world_pop_tc_rel_ov_md_1c       = round(to_zero(data_pop_temperature_change_relative_changes['data']['overall']['median'][2]),3) 
  world_pop_tc_rel_ov_md_2c       = round(to_zero(data_pop_temperature_change_relative_changes['data']['overall']['median'][4]),3) 
  world_pop_tc_rel_ov_md_1c_times = round((to_zero(data_pop_temperature_change_relative_changes['data']['overall']['median'][2])/100+1),3)
  world_pop_tc_rel_ov_md_2c_times = round((to_zero(data_pop_temperature_change_relative_changes['data']['overall']['median'][4])/100+1),3)
  if world_pop_tc_rel_ov_md_1c_times < 1:
     world_pop_tc_rel_ov_md_1c_times_higher_or_lower = 'higher'
  else:
     world_pop_tc_rel_ov_md_1c_times_higher_or_lower = 'lower'
 
 
  world_pop_tc_ov_md_0c           = round(to_zero(data_pop_temperature_change['data']['overall']['median'][0]),3) 
  world_pop_tc_ov_md_1c           = round(to_zero(data_pop_temperature_change['data']['overall']['median'][2]),3) 
  world_pop_tc_ov_md_2c           = round(to_zero(data_pop_temperature_change['data']['overall']['median'][4]),3) 
  world_list_pop_tc_abs_ov_md_1c = []
  for climate_model in data_pop_years['climate_model_list']:
      for impact_model in data_pop_years['impact_model_list']:
          world_list_pop_tc_abs_ov_md_1c.append(round(to_zero(data_pop_temperature_change_absolute_changes['data'][climate_model]['runs'][impact_model]['mean'][2]),3))
  world_minimum_pop_tc_abs_ov_md_1c = min(world_list_pop_tc_abs_ov_md_1c)
  world_maximum_pop_tc_abs_ov_md_1c = max(world_list_pop_tc_abs_ov_md_1c)
  world_list_pop_tc_abs_ov_md_2c = []
  for climate_model in data_pop_years['climate_model_list']:
      for impact_model in data_pop_years['impact_model_list']:
          world_list_pop_tc_abs_ov_md_2c.append(round(to_zero(data_pop_temperature_change_absolute_changes['data'][climate_model]['runs'][impact_model]['mean'][2]),3))
  world_minimum_pop_tc_abs_ov_md_2c = min(world_list_pop_tc_abs_ov_md_2c)
  world_maximum_pop_tc_abs_ov_md_2c = max(world_list_pop_tc_abs_ov_md_2c)
 
 
  world_pop_tc_rel_ov_md_2c       = round(to_zero(data_pop_temperature_change_relative_changes['data']['overall']['median'][4]),3) 
 
  world_pop_pc_abs_today          = round(to_zero(data_pop_timeslices_absolute_changes['data']['rcp60']['overall']['median'][17]),3)
  world_pop_pc_abs_far_future     = round(to_zero(data_pop_timeslices_absolute_changes['data']['piControl']['overall']['median'][21]),3)
  world_pop_pc_rel_far_future     = round(to_zero(data_pop_timeslices_relative_changes['data']['piControl']['overall']['median'][21]),3)
 
  world_pop_rcp26_abs_far_future  = round(to_zero(data_pop_timeslices_absolute_changes['data']['rcp26']['overall']['median'][21]),3)
  world_pop_rcp60_abs_far_future  = round(to_zero(data_pop_timeslices_absolute_changes['data']['rcp60']['overall']['median'][21]),3)
  world_pop_rcp26_rel_far_future  = round(to_zero(data_pop_timeslices_relative_changes['data']['rcp26']['overall']['median'][21]),3)
  world_pop_rcp26_rel_far_future_times = round((to_zero(data_pop_timeslices_relative_changes['data']['rcp26']['overall']['median'][21])/100+1),3)
  world_pop_rcp60_rel_far_future  = round(to_zero(data_pop_timeslices_relative_changes['data']['rcp60']['overall']['median'][21]),3)
  world_pop_rcp26_far_future      = round(to_zero(data_pop_timeslices['data']['rcp26']['overall']['median'][21]),3)
  world_pop_rcp60_far_future      = round(to_zero(data_pop_timeslices['data']['rcp60']['overall']['median'][21]),3)
  world_pop_rcp60_far_future_times = round((to_zero(data_pop_timeslices['data']['rcp60']['overall']['median'][21])/100+1),3)
  world_pop_rcp60_rel_far_future_times = round((to_zero(data_pop_timeslices_relative_changes['data']['rcp60']['overall']['median'][21])/100+1),3)
 
  world_rank_pop_tc_rel_2c       = '(ranking-value: population-exposed-to-river-flood-relative-changes_ISIMIP-projections_versus-temperature-change_'+data_land_years['region']+' value: position temperature:2)'# Should show ranking with regards to relative change in population exposed under 2 degrees temperature change
  world_rank_pop_tc_rel_2c_high_or_low = 'high'#Can we make this flexible to the outcome: e.g. if the ranking is  <100 it is ‘high’, if the ranking is >100 it is ‘low’. Probably CDLX should provide this information. Or we need to calculate the rankings ourselves.
  world_rank_pop_rcp60_rel_far_future  = '(ranking-value: population-exposed-to-river-flood-relative-changes_ISIMIP-projections_versus-timeslices_world value: position time:2081-2100  scenario: rcp60)'
  world_rank_pop_rcp60_rel_far_future_high_or_low = 'high' 
  world_rank_pop_rel_2081_2100 = '(ranking-value: population-exposed-to-river-flood-relative-changes_ISIMIP-projections_versus-timeslices_world value: position time:2081-2100  scenario: rcp60)'
 
  text = open('templates/'+indicator_name+'_world.md').read().format(
                  indicator_short=indicator_short,land_indicator_capital=land_indicator_capital,land_indicator=land_indicator,
                  world_land_tc_ov_md_0c=world_land_tc_ov_md_0c,world_land_tc_rel_ov_md_1c=world_land_tc_rel_ov_md_1c,
                  world_land_rcp60_rel_far_future=world_land_rcp60_rel_far_future,
                  world_land_tc_ov_md_1c=world_land_tc_ov_md_1c,     
                  world_land_tc_ov_md_2c=world_land_tc_ov_md_2c,world_land_tc_rel_ov_md_2c=world_land_tc_rel_ov_md_2c,land_indicator_raw=land_indicator_raw,
                  world_land_pc_abs_far_future=world_land_pc_abs_far_future,world_land_tc_abs_ov_md_2c=world_land_tc_abs_ov_md_2c,
                  world_land_pc_rel_far_future=world_land_pc_rel_far_future,world_land_tc_abs_ov_md_0c=world_land_tc_abs_ov_md_0c,
                  world_land_tc_ov_md_1c_times = world_land_tc_ov_md_1c_times,
                  world_land_rcp26_far_future=world_land_rcp26_far_future,world_land_rcp60_far_future=world_land_rcp60_far_future,
                  world_land_rcp60_far_future_times=world_land_rcp60_far_future_times,
                  world_land_tc_rel_ov_md_1c_times_higher_or_lower=world_land_tc_rel_ov_md_1c_times_higher_or_lower,
                  world_land_tc_rel_ov_md_1c_times=world_land_tc_rel_ov_md_1c_times,
                  world_minimum_land_tc_abs_ov_md_1c=world_minimum_land_tc_abs_ov_md_1c,
                  world_minimum_land_tc_abs_ov_md_2c=world_minimum_land_tc_abs_ov_md_2c,
                  world_land_tc_rel_ov_md_2c_times=world_land_tc_rel_ov_md_2c_times,
                  world_land_rcp60_abs_far_future=world_land_rcp60_abs_far_future,
                  world_land_rcp26_abs_far_future=world_land_rcp26_abs_far_future, 
                  world_land_rcp60_rel_far_future_times=world_land_rcp60_rel_far_future_times,
                  world_land_rcp26_rel_far_future_times=world_land_rcp26_rel_far_future_times,
                  world_maximum_land_tc_abs_ov_md_2c=world_maximum_land_tc_abs_ov_md_2c,
                  
                  world_rank_pop_rel_2081_2100=world_rank_pop_rel_2081_2100,                  
 
                  climate_model_list=climate_model_list,impact_model_list=impact_model_list,country_apostrophe=country_apostrophe,
 
                  world_pop_tc_ov_md_0c=world_pop_tc_ov_md_0c,world_pop_tc_rel_ov_md_1c=world_pop_tc_rel_ov_md_1c,
                  world_pop_rcp60_rel_far_future=world_pop_rcp60_rel_far_future,
                  world_pop_tc_ov_md_1c=world_pop_tc_ov_md_1c,world_pop_rcp26_far_future=world_pop_rcp26_far_future,world_pop_rcp60_far_future=world_pop_rcp60_far_future,          
                  world_pop_tc_ov_md_2c=world_pop_tc_ov_md_2c,world_pop_tc_rel_ov_md_2c=world_pop_tc_rel_ov_md_2c,world_pop_tc_abs_ov_md_2c=world_pop_tc_abs_ov_md_2c,
                  world_pop_pc_abs_far_future=world_pop_pc_abs_far_future,pop_indicator=pop_indicator,pop_indicator_capital=pop_indicator_capital,
                  world_pop_pc_rel_far_future=world_pop_pc_rel_far_future,pop_indicator_raw=pop_indicator_raw,          
                  world_pop_rcp60_rel_far_future_times=world_pop_rcp60_rel_far_future_times,world_pop_rcp60_abs_far_future=world_pop_rcp60_abs_far_future,
                  world_pop_rcp26_rel_far_future_times=world_pop_rcp26_rel_far_future_times,world_pop_rcp26_abs_far_future=world_pop_rcp26_abs_far_future,
                  world_pop_rcp60_far_future_times=world_pop_rcp60_far_future_times,
                  world_pop_tc_rel_ov_md_1c_times=world_pop_tc_rel_ov_md_1c_times,
                  world_pop_tc_rel_ov_md_1c_times_higher_or_lower=world_pop_tc_rel_ov_md_1c_times_higher_or_lower,
                  world_pop_tc_rel_ov_md_2c_times=world_pop_tc_rel_ov_md_2c_times,
                  world_minimum_pop_tc_abs_ov_md_1c=world_minimum_pop_tc_abs_ov_md_1c,
                  world_minimum_pop_tc_abs_ov_md_2c=world_minimum_pop_tc_abs_ov_md_2c,world_maximum_pop_tc_abs_ov_md_2c=world_maximum_pop_tc_abs_ov_md_2c,                
                  world_maximum_pop_tc_abs_ov_md_1c=world_maximum_pop_tc_abs_ov_md_1c,
          )      
          
          
  output_foulder_local = output_foulder+indicator_short.replace(' ','-')+'/ISIMIP-projections/world'
  if not os.path.exists(output_foulder_local):
     os.makedirs(output_foulder_local)
  
  md_file = output_foulder_local+'/'+indicator_short.replace(' ','-')+'-world.md'
  with open(md_file, 'w') as f:
      f.write(text)
      
 
  country_names= os.listdir (input_foulder+indicator_name+'/ISIMIP-projections')
  # Going though all the countries in the list.
  country_names= os.listdir (input_foulder+indicator_name+'/ISIMIP-projections')
  for country_name in country_names:
     if(country_name != 'oceans' and country_name != 'world'):
      #if(country_name == 'AFG'):
          print(indicator_name+ " - " +country_name)  
          
          # Land affected by INDICATOR
          json_land_temperature_change_absolute_changes = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/land-area-affected-by-'+indicator_name+'-absolute-changes_ISIMIP-projections_versus-temperature-change_'+country_name+'.json'
          json_land_timeslices_absolute_changes = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/land-area-affected-by-'+indicator_name+'-absolute-changes_ISIMIP-projections_versus-timeslices_'+country_name+'.json' 
          json_land_years_absolute_changes = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/land-area-affected-by-'+indicator_name+'-absolute-changes_ISIMIP-projections_versus-timeslices_'+country_name+'.json'
 
          json_land_temperature_change = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/land-area-affected-by-'+indicator_name+'_ISIMIP-projections_versus-temperature-change_'+country_name+'.json'
          json_land_timeslices = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/land-area-affected-by-'+indicator_name+'_ISIMIP-projections_versus-timeslices_'+country_name+'.json' 
          json_land_years = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/land-area-affected-by-'+indicator_name+'_ISIMIP-projections_versus-timeslices_'+country_name+'.json'
 
          json_land_temperature_change_relative_changes = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/land-area-affected-by-'+indicator_name+'-relative-changes_ISIMIP-projections_versus-temperature-change_'+country_name+'.json'
          json_land_timeslices_relative_changes = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/land-area-affected-by-'+indicator_name+'-relative-changes_ISIMIP-projections_versus-timeslices_'+country_name+'.json' 
          json_land_years_relative_changes = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/land-area-affected-by-'+indicator_name+'-relative-changes_ISIMIP-projections_versus-timeslices_'+country_name+'.json'
 
          # Population exposed to INDICATOR
          json_pop_temperature_change_absolute_changes = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/population-exposed-to-'+indicator_name+'-absolute-changes_ISIMIP-projections_versus-temperature-change_'+country_name+'.json'
          json_pop_timeslices_absolute_changes = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/population-exposed-to-'+indicator_name+'-absolute-changes_ISIMIP-projections_versus-timeslices_'+country_name+'.json' 
          json_pop_years_absolute_changes = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/population-exposed-to-'+indicator_name+'-absolute-changes_ISIMIP-projections_versus-timeslices_'+country_name+'.json'
 
          json_pop_temperature_change = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/population-exposed-to-'+indicator_name+'_ISIMIP-projections_versus-temperature-change_'+country_name+'.json'
          json_pop_timeslices = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/population-exposed-to-'+indicator_name+'_ISIMIP-projections_versus-timeslices_'+country_name+'.json' 
          json_pop_years = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/population-exposed-to-'+indicator_name+'_ISIMIP-projections_versus-timeslices_'+country_name+'.json'
 
          json_pop_temperature_change_relative_changes = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/population-exposed-to-'+indicator_name+'-relative-changes_ISIMIP-projections_versus-temperature-change_'+country_name+'.json'
          json_pop_timeslices_relative_changes = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/population-exposed-to-'+indicator_name+'-relative-changes_ISIMIP-projections_versus-timeslices_'+country_name+'.json' 
          json_pop_years_relative_changes = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/population-exposed-to-'+indicator_name+'-relative-changes_ISIMIP-projections_versus-timeslices_'+country_name+'.json'
              
          # load JSON files  
          # Land affected by INDICATOR           
          with open(json_land_temperature_change_absolute_changes) as f:
               data_land_temperature_change_absolute_changes = json.load(f)                          
          with open(json_land_timeslices_absolute_changes) as f:
               data_land_timeslices_absolute_changes = json.load(f)      
          with open(json_land_years_absolute_changes) as f:
               data_land_years_absolute_changes = json.load(f)                          
          with open(json_land_temperature_change) as f:
               data_land_temperature_change = json.load(f)   
          with open(json_land_timeslices) as f:
               data_land_timeslices = json.load(f)                          
          with open(json_land_years) as f:
               data_land_years = json.load(f)                 
          with open(json_land_temperature_change_relative_changes) as f:
               data_land_temperature_change_relative_changes = json.load(f)   
          with open(json_land_timeslices_relative_changes) as f:
               data_land_timeslices_relative_changes = json.load(f)                          
          with open(json_land_years_relative_changes) as f:
               data_land_years_relative_changes = json.load(f)    
 
          # Population exposed to INDICATOR
          with open(json_pop_temperature_change_absolute_changes) as f:
               data_pop_temperature_change_absolute_changes = json.load(f)                          
          with open(json_pop_timeslices_absolute_changes) as f:
               data_pop_timeslices_absolute_changes = json.load(f)      
          with open(json_pop_years_absolute_changes) as f:
               data_pop_years_absolute_changes = json.load(f)                          
          with open(json_pop_temperature_change) as f:
               data_pop_temperature_change = json.load(f)   
          with open(json_pop_timeslices) as f:
               data_pop_timeslices = json.load(f)                          
          with open(json_pop_years) as f:
               data_pop_years = json.load(f)                 
          with open(json_pop_temperature_change_relative_changes) as f:
               data_pop_temperature_change_relative_changes = json.load(f)   
          with open(json_pop_timeslices_relative_changes) as f:
               data_pop_timeslices_relative_changes = json.load(f)
          with open(json_pop_years_relative_changes) as f:
               data_pop_years_relative_changes = json.load(f)    
           
          # Fill variables 
          # Land affected by INDICATOR     
          country                = data_land_years['region']
          
          if country[len(country)-1] == 's':
            country_apostrophe   = data_land_years['region']+'’'
          else:
            country_apostrophe   = data_land_years['region']+'’s'
            
          land_indicator_raw     = data_land_years['variable']
          land_indicator         = data_land_years['variable'].replace('-',' ') 
          land_indicator_capital = data_land_years['variable'].replace('-',' ').capitalize()
          indicator_short        = data_land_years['indicator'].replace('-',' ')#land_indicator.replace('land area affected by ','') 
 
          climate_model_list     = len(data_land_years['climate_model_list'])
          impact_model_list      = len(data_land_years['impact_model_list'])                      
          
          land_tc_abs_ov_md_0c   = round(to_zero(data_land_temperature_change_absolute_changes['data']['overall']['median'][0]),3) 
          land_tc_abs_ov_md_1c   = round(to_zero(data_land_temperature_change_absolute_changes['data']['overall']['median'][2]),3) 
          land_tc_abs_ov_md_2c   = round(to_zero(data_land_temperature_change_absolute_changes['data']['overall']['median'][4]),3) 
          list_land_tc_abs_ov_md_1c = []
          for climate_model in data_land_years['climate_model_list']:
              for impact_model in data_land_years['impact_model_list']:
                  list_land_tc_abs_ov_md_1c.append(round(to_zero(data_land_temperature_change_absolute_changes['data'][climate_model]['runs'][impact_model]['mean'][2]),3))
          minimum_land_tc_abs_ov_md_1c = min(list_land_tc_abs_ov_md_1c)
          maximum_land_tc_abs_ov_md_1c = max(list_land_tc_abs_ov_md_1c)
 
          list_land_tc_abs_ov_md_2c = []
          for climate_model in data_land_years['climate_model_list']:
              for impact_model in data_land_years['impact_model_list']:
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
 
          land_pc_abs_today      = round(to_zero(data_land_timeslices_absolute_changes['data']['rcp60']['overall']['median'][17]),3)
          land_pc_abs_far_future = round(to_zero(data_land_timeslices_absolute_changes['data']['piControl']['overall']['median'][21]),3)
          land_pc_rel_far_future = round(to_zero(data_land_timeslices_relative_changes['data']['piControl']['overall']['median'][21]),3)
 
          land_rcp26_abs_far_future  = round(to_zero(data_land_timeslices_absolute_changes['data']['rcp26']['overall']['median'][21]),3)
          land_rcp60_abs_far_future  = round(to_zero(data_land_timeslices_absolute_changes['data']['rcp60']['overall']['median'][21]),3)
          land_rcp26_rel_far_future  = round(to_zero(data_land_timeslices_relative_changes['data']['rcp26']['overall']['median'][21]),3)
          land_rcp60_rel_far_future  = round(to_zero(data_land_timeslices_relative_changes['data']['rcp60']['overall']['median'][21]),3)
          land_rcp26_far_future      = round(to_zero(data_land_timeslices['data']['rcp26']['overall']['median'][21]),3)
          land_rcp60_far_future      = round(to_zero(data_land_timeslices['data']['rcp60']['overall']['median'][21]),3)
          land_rcp60_far_future_times = round((to_zero(data_land_timeslices['data']['rcp60']['overall']['median'][21])/100+1),3)
          land_rcp26_far_future_times = round((to_zero(data_land_timeslices['data']['rcp26']['overall']['median'][21])/100+1),3)
          land_rcp60_rel_far_future_times = round(to_zero(data_land_timeslices_relative_changes['data']['rcp60']['overall']['median'][21])/100+1,3)
          land_rcp26_rel_far_future_times = round(to_zero(data_land_timeslices_relative_changes['data']['rcp26']['overall']['median'][21])/100+1,3)
 
          rank_land_tc_rel_2c        = '(ranking-value: land-area-affected-by-river-flood-relative-changes_ISIMIP-projections_versus-temperature-change_'+country_name+' value: position temperature:2)' #Should show ranking with regards to relative change in land area affected under 2 degrees temperature change
          rank_land_tc_rel_2081_2100 = '(ranking-value: land-area-affected-by-river-flood-relative-changes_ISIMIP-projections_versus-timeslices_'+country_name+' value: position time:2081-2100  scenario: rcp60)'
 
          # Population exposed to INDICATOR
          pop_indicator_raw         = data_pop_years['variable'] 
          pop_indicator             = data_pop_years['variable'].replace('-',' ') 
          pop_indicator_capital     = data_pop_years['variable'].replace('-',' ').capitalize()
          
          pop_tc_abs_ov_md_0c       = round(to_zero(data_pop_temperature_change_absolute_changes['data']['overall']['median'][0]),3) 
          pop_tc_abs_ov_md_1c       = round(to_zero(data_pop_temperature_change_absolute_changes['data']['overall']['median'][2]),3) 
          pop_tc_abs_ov_md_2c       = round(to_zero(data_pop_temperature_change_absolute_changes['data']['overall']['median'][4]),3) 
 
          list_pop_tc_abs_ov_md_1c = []
          for climate_model in data_pop_years['climate_model_list']:
              for impact_model in data_pop_years['impact_model_list']:
                  list_pop_tc_abs_ov_md_1c.append(round(to_zero(data_pop_temperature_change_absolute_changes['data'][climate_model]['runs'][impact_model]['mean'][2]),3))
          minimum_pop_tc_abs_ov_md_1c = min(list_pop_tc_abs_ov_md_1c)
          maximum_pop_tc_abs_ov_md_1c = max(list_pop_tc_abs_ov_md_1c)
 
          list_pop_tc_abs_ov_md_2c = []
          for climate_model in data_pop_years['climate_model_list']:
              for impact_model in data_pop_years['impact_model_list']:
                  list_pop_tc_abs_ov_md_2c.append(round(to_zero(data_pop_temperature_change_absolute_changes['data'][climate_model]['runs'][impact_model]['mean'][4]),3))
          minimum_pop_tc_abs_ov_md_2c = min(list_pop_tc_abs_ov_md_2c)
          maximum_pop_tc_abs_ov_md_2c = max(list_pop_tc_abs_ov_md_2c)        
 
          pop_tc_rel_ov_md_0c       = round(to_zero(data_pop_temperature_change_relative_changes['data']['overall']['median'][0]),3) 
          pop_tc_rel_ov_md_1c       = round(to_zero(data_pop_temperature_change_relative_changes['data']['overall']['median'][2]),3) 
          pop_tc_rel_ov_md_2c       = round(to_zero(data_pop_temperature_change_relative_changes['data']['overall']['median'][4]),3) 
          pop_tc_rel_ov_md_1c_times = round((to_zero(data_pop_temperature_change_relative_changes['data']['overall']['median'][2])/100+1),3)
          if pop_tc_rel_ov_md_1c_times < 1:
             pop_tc_rel_ov_md_1c_times_higher_or_lower = 'higher'
          else:
             pop_tc_rel_ov_md_1c_times_higher_or_lower = 'lower'
          pop_tc_rel_ov_md_2c_times = round((to_zero(data_pop_temperature_change_relative_changes['data']['overall']['median'][4])/100+1),3)
             
          pop_tc_ov_md_0c           = round(to_zero(data_pop_temperature_change['data']['overall']['median'][0]),3) 
          pop_tc_ov_md_1c           = round(to_zero(data_pop_temperature_change['data']['overall']['median'][2]),3) 
          pop_tc_ov_md_2c           = round(to_zero(data_pop_temperature_change['data']['overall']['median'][4]),3) 
          pop_substract_2_and_1     = round(pop_tc_ov_md_2c - pop_tc_ov_md_1c,3)
 
          pop_tc_rel_ov_md_2c       = round(to_zero(data_pop_temperature_change_relative_changes['data']['overall']['median'][4]),3) 
 
          pop_pc_abs_today          = round(to_zero(data_pop_timeslices_absolute_changes['data']['rcp60']['overall']['median'][17]),3)
          pop_pc_abs_far_future     = round(to_zero(data_pop_timeslices_absolute_changes['data']['piControl']['overall']['median'][21]),3)
          pop_pc_rel_far_future     = round(to_zero(data_pop_timeslices_relative_changes['data']['piControl']['overall']['median'][21]),3)
 
          pop_rcp26_abs_far_future  = round(to_zero(data_pop_timeslices_absolute_changes['data']['rcp26']['overall']['median'][21]),3)
          pop_rcp60_abs_far_future  = round(to_zero(data_pop_timeslices_absolute_changes['data']['rcp60']['overall']['median'][21]),3)
          pop_rcp26_rel_far_future  = round(to_zero(data_pop_timeslices_relative_changes['data']['rcp26']['overall']['median'][21]),3)
          pop_rcp60_rel_far_future  = round(to_zero(data_pop_timeslices_relative_changes['data']['rcp60']['overall']['median'][21]),3)
          pop_rcp26_far_future      = round(to_zero(data_pop_timeslices['data']['rcp26']['overall']['median'][21]),3)
          pop_rcp60_far_future      = round(to_zero(data_pop_timeslices['data']['rcp60']['overall']['median'][21]),3)
          pop_rcp60_far_future_times = round((to_zero(data_pop_timeslices['data']['rcp60']['overall']['median'][21])/100+1),3)
          pop_rcp26_far_future_times = round((to_zero(data_pop_timeslices['data']['rcp26']['overall']['median'][21])/100+1),3)
          pop_rcp60_rel_far_future_times = round((to_zero(data_pop_timeslices_relative_changes['data']['rcp60']['overall']['median'][21])/100+1),3)
          pop_rcp26_rel_far_future_times = round((to_zero(data_pop_timeslices_relative_changes['data']['rcp26']['overall']['median'][21])/100+1),3)
 
          rank_pop_tc_rel_2c       = '(ranking-value: land-area-affected-by-river-flood-relative-changes_ISIMIP-projections_versus-temperature-change_'+country_name+' value: position temperature:2)'# Should show ranking with regards to relative change in population exposed under 2 degrees temperature change
          rank_pop_tc_rel_2081_2100= '(ranking-value: population-exposed-to-river-flood-relative-changes_ISIMIP-projections_versus-timeslices_'+country_name+' value: position time:2081-2100 scenario: rcp60)'
          
          # Writing the text. 
 
          if (country_name != 'world'): 
           text = open('templates/'+indicator_name+'.md').read().format(
                  indicator_short=indicator_short,country=country,country_name=country_name,land_indicator_capital=land_indicator_capital,
                  land_tc_ov_md_0c=land_tc_ov_md_0c,land_tc_rel_ov_md_1c=land_tc_rel_ov_md_1c,
                  land_rcp60_rel_far_future=land_rcp60_rel_far_future,land_substract_2_and_1=land_substract_2_and_1,
                  land_tc_ov_md_1c=land_tc_ov_md_1c,     
                  land_tc_ov_md_2c=land_tc_ov_md_2c,land_tc_rel_ov_md_2c=land_tc_rel_ov_md_2c,land_indicator_raw=land_indicator_raw,
                  land_pc_abs_far_future=land_pc_abs_far_future,land_indicator=land_indicator,land_tc_abs_ov_md_2c=land_tc_abs_ov_md_2c,
                  land_pc_rel_far_future=land_pc_rel_far_future,land_tc_abs_ov_md_0c=land_tc_abs_ov_md_0c,
                  land_tc_ov_md_1c_times = land_tc_ov_md_1c_times,
                  land_rcp26_far_future=land_rcp26_far_future,land_rcp60_far_future=land_rcp60_far_future,
                  land_rcp60_far_future_times=land_rcp60_far_future_times,
                  land_tc_rel_ov_md_1c_times_higher_or_lower=land_tc_rel_ov_md_1c_times_higher_or_lower,
                  land_tc_rel_ov_md_1c_times=land_tc_rel_ov_md_1c_times,
                  minimum_land_tc_abs_ov_md_1c=minimum_land_tc_abs_ov_md_1c,maximum_land_tc_abs_ov_md_1c=maximum_land_tc_abs_ov_md_1c,
                  minimum_land_tc_abs_ov_md_2c=minimum_land_tc_abs_ov_md_2c,maximum_land_tc_abs_ov_md_2c=maximum_land_tc_abs_ov_md_2c,
                  land_tc_rel_ov_md_2c_times=land_tc_rel_ov_md_2c_times,land_rcp60_rel_far_future_times=land_rcp60_rel_far_future_times,
                  land_rcp60_abs_far_future=land_rcp60_abs_far_future,land_rcp26_rel_far_future_times=land_rcp26_rel_far_future_times,
                  land_rcp26_abs_far_future=land_rcp26_abs_far_future, 
                  rank_land_tc_rel_2c=rank_land_tc_rel_2c,
                  rank_land_tc_rel_2081_2100=rank_land_tc_rel_2081_2100,
                  
                  world_land_tc_rel_ov_md_2c_times=world_land_tc_rel_ov_md_2c_times,
                  world_rank_land_rcp60_rel_far_future=world_rank_land_rcp60_rel_far_future,
                  world_rank_land_rcp60_rel_far_future_high_or_low=world_rank_land_rcp60_rel_far_future_high_or_low,
                  world_land_rcp60_rel_far_future_times=world_land_rcp60_rel_far_future_times,
                  world_land_tc_ov_md_0c=world_land_tc_ov_md_0c,
                  world_rank_land_tc_rel_2c=world_rank_land_tc_rel_2c,
                  world_rank_land_tc_rel_2c_high_or_low=world_rank_land_tc_rel_2c_high_or_low,
                  world_pop_tc_ov_md_0c=world_pop_tc_ov_md_0c,
                  world_pop_tc_rel_ov_md_2c_times=world_pop_tc_rel_ov_md_2c_times,
                  world_pop_rcp60_rel_far_future_times=world_pop_rcp60_rel_far_future_times,
                  world_rank_pop_tc_rel_2c=world_rank_pop_tc_rel_2c,
                  world_rank_pop_tc_rel_2c_high_or_low=world_rank_pop_tc_rel_2c_high_or_low,
                  world_rank_pop_rcp60_rel_far_future=world_rank_pop_rcp60_rel_far_future,
                  world_rank_pop_rcp60_rel_far_future_high_or_low=world_rank_pop_rcp60_rel_far_future_high_or_low, 
                  
 
                  climate_model_list=climate_model_list,impact_model_list=impact_model_list,country_apostrophe=country_apostrophe,
 
                  pop_tc_ov_md_0c=pop_tc_ov_md_0c,pop_tc_rel_ov_md_1c=pop_tc_rel_ov_md_1c,
                  pop_rcp60_rel_far_future=pop_rcp60_rel_far_future,pop_substract_2_and_1=pop_substract_2_and_1,
                  pop_tc_ov_md_1c=pop_tc_ov_md_1c,pop_rcp26_far_future=pop_rcp26_far_future,pop_rcp60_far_future=pop_rcp60_far_future,          
                  pop_tc_ov_md_2c=pop_tc_ov_md_2c,pop_tc_rel_ov_md_2c=pop_tc_rel_ov_md_2c,pop_tc_abs_ov_md_2c=pop_tc_abs_ov_md_2c,
                  pop_pc_abs_far_future=pop_pc_abs_far_future,pop_indicator=pop_indicator,pop_indicator_capital=pop_indicator_capital,
                  pop_pc_rel_far_future=pop_pc_rel_far_future,pop_indicator_raw=pop_indicator_raw,          
                  pop_rcp60_rel_far_future_times=pop_rcp60_rel_far_future_times,pop_rcp60_abs_far_future=pop_rcp60_abs_far_future,
                  pop_rcp26_rel_far_future_times=pop_rcp26_rel_far_future_times,pop_rcp26_abs_far_future=pop_rcp26_abs_far_future,
                  pop_rcp60_far_future_times=pop_rcp60_far_future_times,
                  pop_tc_rel_ov_md_1c_times=pop_tc_rel_ov_md_1c_times,
                  pop_tc_rel_ov_md_1c_times_higher_or_lower=pop_tc_rel_ov_md_1c_times_higher_or_lower,
                  pop_tc_rel_ov_md_2c_times=pop_tc_rel_ov_md_2c_times,
                  minimum_pop_tc_abs_ov_md_1c=minimum_pop_tc_abs_ov_md_1c,maximum_pop_tc_abs_ov_md_1c=maximum_pop_tc_abs_ov_md_1c,
                  minimum_pop_tc_abs_ov_md_2c=minimum_pop_tc_abs_ov_md_2c,maximum_pop_tc_abs_ov_md_2c=maximum_pop_tc_abs_ov_md_2c,
                  rank_pop_tc_rel_2c=rank_pop_tc_rel_2c,
                  rank_pop_tc_rel_2081_2100=rank_pop_tc_rel_2081_2100
 
                  )          
                  
           output_foulder_local = output_foulder+indicator_short.replace(' ','-')+'/ISIMIP-projections/'+country_name
           if not os.path.exists(output_foulder_local):
             os.makedirs(output_foulder_local)
          
           md_file = output_foulder_local+'/'+indicator_short.replace(' ','-')+'-'+country_name+'.md'
           with open(md_file, 'w') as f:
              f.write(text)



def main():

  input_foulder = 'test-data/'
  output_foulder = 'test-data/'

  # Get the folder names, i.e the indicator names. 
  indicator_names= os.listdir (input_foulder)

  for indicator_name in indicator_names:
    process_indicator(indicator_name, input_foulder, output_foulder)



if __name__ == '__main__':
  main()    