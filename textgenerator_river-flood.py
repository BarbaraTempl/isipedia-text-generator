# NEW FILES


"""
To: Generate Text for ISIPedia Project
By: Julian Hunt (IIASA)
On: 2018/04

The one which we are going to write newly should be more simple.
This old one contains 1) country data extraction, 2) mapping, and 3) plotting as well, which other ISIpedia colleagues are in charge of. Previously, we thought we would do it too, but they are not our tasks any more. We can focus on text parts.
What we will do for a new text generator(s?) are;
Change IO part to handle json input files and markdown output files
Upgrade lines after l.376 of this old script

"""

import json
import os
import pandas as pd
import numpy as np


def to_zero(text):
    
    if type(text) == str or str(text) == 'None':
      return 0
        
    else:
      return text 
     

input_foulder = '/home/julian/ISIPedia_DKRZ_Server/data_cube/'
output_foulder = '/home/julian/ISIPedia_DKRZ_Server/data_cube/'

#input_foulder = '/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/data_cube/'
#output_foulder = '/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/data_cube/'

# Get the folder names, i.e the indicator names. 
indicator_names= os.listdir (input_foulder)

for indicator_name in indicator_names:
# if(indicator_name=='crop-failure' or indicator_name=='river-flood' or indicator_name=='tropical-cyclone' or indicator_name=='wildfire'):
 if(indicator_name=='river-flood'):
    
    ## Look world first
           # Land affected by INDICATOR
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
    
           text = open('templates/river-flood_world.md').read().format(
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
               

               
           countries_rank = pd.read_excel('/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/Github/ISIPedia/Countries Names.xls')# Creating a rank for [‘overall‘][‘median_relative_changes’][6]
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
                    text = open('templates/river-flood.md').read().format(
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


#%%

























# OLD FILES
    #! /usr/local/bin/python
"""
To: Generate Text for ISIPedia Project
By: Julian Hunt (IIASA)
On: 2018/04

The one which we are going to write newly should be more simple.
This old one contains 1) country data extraction, 2) mapping, and 3) plotting as well, which other ISIpedia colleagues are in charge of. Previously, we thought we would do it too, but they are not our tasks any more. We can focus on text parts.
What we will do for a new text generator(s?) are;
Change IO part to handle json input files and markdown output files
Upgrade lines after l.376 of this old script

"""

import json
import os
import pandas as pd

# I tried 6 different approaches to connect to the server though python but I could not do it. 
# Some of these attamps includes the direction on the sites below:
# https://git.geomar.de/python/jupyter_on_HPC_setup_guide/issues/13
# https://www.dkrz.de/up/systems/swift/python

input_foulder = '/home/julian/ISIPedia_DKRZ_Server/data_cube_preliminary/'
output_foulder = '/home/julian/ISIPedia_DKRZ_Server/data_cube/'
#working ofline:
#input_foulder =  '/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/'
#output_foulder = '/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/text_generator_output_test/'

# Get the folder names, i.e the indicator names. 
indicator_names= os.listdir (input_foulder)

for indicator_name in indicator_names:

    countries_rank = pd.read_excel('/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/Github/ISIPedia/Countries Names.xls')# Creating a rank for [‘overall‘][‘median_relative_changes’][6] 
    country_names= os.listdir (input_foulder+indicator_name+'/ISIMIP-projections')
    for country_name in country_names:
        if(len(country_name) == 3):
         json_temperature_change = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/'+indicator_name+'_ISIMIP-projections_'+country_name+'_versus-temperature-change.json'
         json_timeslices =         input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/'+indicator_name+'_ISIMIP-projections_'+country_name+'_versus-timeslices.json'
           
         json_server = open(json_temperature_change).read()
         json_server = json_server.replace('.,','.0,')
         json_server = json_server.replace('.]','.0]')

         json_local = open('/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/intermediate.json', 'w')
         json_local.write(json_server)
         json_local.close()     

         with open('/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/intermediate.json') as f:
           data = json.load(f)    
         if (country_name != 'world'):
          countries_rank.set_value(countries_rank.loc[countries_rank['Abbreviation'] == country_name]['Country_Name'].index[0] , 'Index_Rank', data['data']['overall']['median_relative_changes'][6]) 
    countries_rank_sorted = pd.DataFrame(countries_rank.sort_values('Index_Rank', ascending=False).values)
    countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][0]][0].index[0] , 'Rank', 1) 
    c = 1
    while c < countries_rank_sorted.shape[0]:
     if countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][c-1]][2].values[0] == countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][c]][2].values[0]:
      countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][c]][0].index[0] , 'Rank', countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][c-1]]['Rank'].values[0]) 
     else: 
      countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][c]][0].index[0] , 'Rank', countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][c-1]]['Rank'].values[0]+1) 
     c=c+1    
     
    # Going though all the countries in the list.
    country_names= os.listdir (input_foulder+indicator_name+'/ISIMIP-projections')
    for country_name in country_names:
        if (country_name != 'world'):
         if(len(country_name) == 3):
           #print(country_name)    
           #countries_abbreviation_and_names = pd.read_excel('H:/Things in C Drive/IIASA/Water Group/ISIpedia/Countries Names.xlsx')
           #countries_abbreviations = countries_abbreviation_and_names["Abbreviation"]
           #countries_names = countries_abbreviation_and_names["Country_Name"]

           # Finding JSON file:
           #json_names= os.listdir(input_foulder+'/'+indicator_name+'/ISIMIP-projections/'+country_name)    
           #print(json_names)
           json_temperature_change = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/'+indicator_name+'_ISIMIP-projections_'+country_name+'_versus-temperature-change.json'
           json_timeslices =         input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/'+indicator_name+'_ISIMIP-projections_'+country_name+'_versus-timeslices.json'
           
           json_server = open(json_temperature_change).read()
           json_server = json_server.replace('.,','.0,')
           json_server = json_server.replace('.]','.0]')

           json_local = open('/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/intermediate.json', 'w')
           json_local.write(json_server)
           json_local.close()      
               
           # load JSON files           
           with open('/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/intermediate.json') as f:
                data = json.load(f)                          
           
           #with open(json_timeslices) as f:   #I removed the timeslices.json because there are indicators which do not have this yet.
           #     data2 = json.load(f)     
                
           country = data['region']
           indicator = data['indicator'].replace('-',' ') 
           indicator_capital = data['indicator'].replace('-',' ').capitalize()
                  
           absolutechange                 = data['data']['overall']['median_absolute_changes'][6] 
           median_relative_changes_3      = data['data']['overall']['median_relative_changes'][6] # 1800%
           median_relative_changes_2      = data['data']['overall']['median_relative_changes'][4] # 678%0
           median_relative_changes_1      = data['data']['overall']['median_relative_changes'][2] # 172%
           
           temperature_rise_3               = data['temperature_list'][6] # 3
           temperature_rise_2               = data['temperature_list'][4] # 2
           temperature_rise_1               = data['temperature_list'][2] # 1     
    
           shading_lower_border_relative_changes = data['data']['overall']['shading_lower_border_relative_changes'][6] # 369%
           shading_upper_border_relative_changes = data['data']['overall']['shading_upper_border_relative_changes'][6] # 4908%
    
           rcp26_near_future               = 'x' # data2['data']['rcp26']['MIROC5']['median_relative_changes'][18]
           rcp26_mid_future                = 'y' # data2['data']['rcp26']['MIROC5']['median_relative_changes'][19]
           rcp26_far_future                = 'z' # data2['data']['rcp26']['MIROC5']['median_relative_changes'][21]

           rcp60_near_future               = 'X' # data2['data']['rcp60']['MIROC5']['median_relative_changes'][18]
           rcp60_mid_future                = 'Y' # data2['data']['rcp60']['MIROC5']['median_relative_changes'][19]
           rcp60_far_future                = 'Z' # data2['data']['rcp60']['MIROC5']['median_relative_changes'][21]

           rank_median_relative_changes_3 = countries_rank_sorted.loc[countries_rank_sorted[0] == country_name]['Rank'].values[0]

           # Writing the text.
           text1 = country
           text2 = indicator_capital           
           text3 = '* Under the pi-control reference conditions {indicator} is affected by {absolutechange}%.\n\
                  * Climate change is expected to increase the {indicator} with up to {median_relative_changes_3}% under a global warming level of {temperature_rise_3} degrees Celsius and/or with up to {rcp60_far_future}% when moving towards the far-future.\n\
                  * {country} ranks {rank_median_relative_changes_3}th globally for the relative change in {indicator}.'.format(
                   country=country,indicator=indicator,indicator_capital=indicator_capital,absolutechange=absolutechange, median_relative_changes_3=median_relative_changes_3, temperature_rise_3=temperature_rise_3,
                   rank_median_relative_changes_3=rank_median_relative_changes_3,rcp60_far_future=rcp60_far_future)
           text4 = 'The following section shows the climate impact assessment results for the {indicator} for {country} comparing different levels of global warming and future time-periods with the pi-control reference conditions.'.format(
                   country=country,indicator=indicator)
           text5 = 'Model simulations indicate that {absolutechange}% of the {indicator} under the pi-control reference conditions. According to these simulations, climate change is expected to increase the {indicator} on average with {median_relative_changes_1}%, {median_relative_changes_2}%, and {median_relative_changes_3}% under increases of respectively 1, 2, and 3 degree Celsius compared to the pi-control reference conditions.\n\
                   The ensemble-spread in the estimated increase of {indicator} under a global warming level of 3 degrees Celsius can be considered large with estimates of individual model runs that vary between {shading_lower_border_relative_changes}% up to {shading_upper_border_relative_changes}%.\n\
                   For the near-term, mid-term, and far-future, model simulations estimate increases in the {indicator} compared to the pi-control reference period of {rcp26_near_future}, {rcp26_mid_future}%, and {rcp26_far_future}% under RCP 2.6 and {rcp60_near_future}, {rcp60_mid_future}%, and {rcp60_far_future}% under RCP 6.0.'.format(
                   absolutechange=absolutechange,indicator=indicator,median_relative_changes_1=median_relative_changes_1,median_relative_changes_2=median_relative_changes_2,median_relative_changes_3=median_relative_changes_3,shading_lower_border_relative_changes=shading_lower_border_relative_changes,shading_upper_border_relative_changes=shading_upper_border_relative_changes,
                   rcp26_near_future=rcp26_near_future,rcp26_mid_future=rcp26_mid_future,rcp26_far_future=rcp26_far_future,rcp60_near_future=rcp60_near_future,rcp60_mid_future=rcp60_mid_future,rcp60_far_future=rcp60_far_future)  
           text6 = 'Relative change in the {indicator} under different levels of global warming compared to the pi-control reference conditions'.format(
                   indicator=indicator)    
           text7 = 'In comparison to other countries, {country} ranks {rank_median_relative_changes_3}th globally when comparing the relative change in the {indicator} under a global warming level of 3 degrees Celsius compared to the pi-control reference conditions.'.format(
                   indicator=indicator,country=country,rank_median_relative_changes_3=rank_median_relative_changes_3) 
           #text8 = 'Ensemble-median land area affected by droughts under the pi-control reference conditions.'    
           #text9 = 'Ensemble-median change in land area affected by droughts under a global warming level of 3 degrees Celsius compared to the pi-control reference conditions'    
           #text10 = 'Under the pi-control reference conditions, the regions in {country} that are affected most with regards to the land area affected by droughts are the North and South. Regions that show, on average, the largest increase in land area affected by droughts under a 3 degree Celsius global warming level compared to the pi-control conditions are the West and East.'    

           # Output in the Markdown format
           # Create folder if it does not exist
           output_foulder_local = output_foulder+indicator_name+'/ISIMIP-projections/'+country_name
           if not os.path.exists(output_foulder_local):
             os.makedirs(output_foulder_local)
           # TT1
           md_file = output_foulder_local+'/TT1_'+indicator_name+'_ISIMIP-projections_'+country_name+'.md'
           with open(md_file, 'w') as f:
              f.write(text1)
           # TT2
           md_file = output_foulder_local+'/TT2_'+indicator_name+'_ISIMIP-projections_'+country_name+'.md'
           with open(md_file, 'w') as f:
              f.write(text2)
           # KM
           md_file = output_foulder_local+'/KM_'+indicator_name+'_ISIMIP-projections_'+country_name+'.md'
           with open(md_file, 'w') as f:
              f.write(text3)
           # INTR
           md_file = output_foulder_local+'/INTR_'+indicator_name+'_ISIMIP-projections_'+country_name+'.md'
           with open(md_file, 'w') as f:
              f.write(text4)
           # GRPH
           md_file = output_foulder_local+'/GRPH_'+indicator_name+'_ISIMIP-projections_'+country_name+'.md'
           with open(md_file, 'w') as f:
              f.write(text5)
           # GRPH_TT
           md_file = output_foulder_local+'/GRPH_TT_'+indicator_name+'_ISIMIP-projections_'+country_name+'.md'
           with open(md_file, 'w') as f:
              f.write(text6)
           # RNK
           md_file = output_foulder_local+'/RNK_'+indicator_name+'_ISIMIP-projections_'+country_name+'.md'
           with open(md_file, 'w') as f:
              f.write(text7)
           print(indicator, " - ",country)   
           # Text 8, 9, 10 are missing. 

#%%
# Look though the JSON file in a sturctured way.

import pprint
import json
text = ''

json_temperature_change = ''
json_timeslices =         '/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/land-area-affected-by-crop-failure/ISIMIP-projections/AFG/land-area-affected-by-crop-failure_ISIMIP-projections_AFG_versus-timeslices.json'

with open(json_timeslices) as f:   #I removed the timeslices.json because there are indicators which do not have this yet.
  data = json.load(f)   
                
data_keys = data.keys()

for keys in data_keys:
    #text = text + str(data[keys])
    #print (keys , 'NEW KEY ************')
    #print(data[keys])
     
    pprint.pprint(data[keys])

#%%

for (k,v) in data['data'].items():
    
    print('*****Keys1', k,'Values2' ,v )
    
    for (k2,v2) in data['data'][k].items():
        
        print('***********Keys2', k2,'Values2' ,v2 )
 
   #  for (k3,v3) in data['data'][k][k2].items():
        
    #    print('********************Keys3', k3,'Values3' ,v3 )    
    
#%%

    
