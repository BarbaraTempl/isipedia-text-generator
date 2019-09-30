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
    
           text = """This (link: glossary/climate-impact-assessment text: climate impact) assessment presents (link: glossary/projections text: projections) of the {land_indicator} and the number of people exposed to {indicator_short} globally, based on {impact_model_list} different (link: glossary/global-hydrological-models text: global hydrological models) (GHMs) and {climate_model_list} different global (link: glossary/climate-models text: climate models)(GCMs) participating in [ISIMIP](https://www.isimip.org/).\n\
\n\
Here, (link: glossary/river-floods text: {indicator_short}) refer to a situation where the daily (link: glossary/river-flow text: river flow) exceeds the so-called 100-year (link: glossary/return-level text: return level). For each (link: glossary/grid-cell text: grid cell), which covers an area of up to 50x50 square-kilometers affected to {indicator_short}, we calculate the percentage of area flooded by redistributing the (link: glossary/flood-volume text: flood volume) per cell in accordance variations in (link: glossary/surface-elevation text: surface elevation). To calculate the {land_indicator} at the global scale, the percentage of area flooded are added up across all grid cells worldwide. To calculate the number of people exposed to {indicator_short} globally, we first multiply the percentage of area flooded of each grid cell by the number of people living in that grid cell to estimate the number of people exposed to {indicator_short}, and then add up those numbers across all grid cells worldwide.\n\
\n\
We analyze the {land_indicator} and the number of people exposed to {indicator_short} at different (link: glossary/levels-of-global-warming text: levels of global warming)(0, 1, 2, and 3 degrees Celsius) and during different time periods. We cover the time before (link: glossary/anthropogenic-climate-change text: anthropogenic climate change) started (conventionally set at 1850), present-day (2001-2020), mid-century (2041-2060) and end-of-century (2081-2100). We compare the later periods against the climate conditions before anthropogenic climate change started (1850). A ranking of countries for each indicator is provided to allow comparison between countries on the basis of their (link: glossary/relative-change text: relative change) in the land area affected or the number of people exposed under different levels of global warming and for various time horizons, compared to conditions before anthropogenic climate change started. Here, a ranking of 1 implies that the country experiences a change in the (link: glossary/indicator text: indicator) that is more than all other ranked countries, whereas a lower ranking entails comparatively less effects due to climate change.\n\
\n\
It is important to note that our (link: glossary/future-projections text: future projections) assume that the number of people living in an area, as well as the area’s (link: glossary/land-use text: land use) and (link: glossary/land-cover text: land cover), remain constant to that of the year 2005. This is not necessarily meant to be realistic, but to isolate the influence of climate change from the influence of other changes.\n\
\n\
In the key messages we report the results for the (link: glossary/median text: median) of the (link: glossary/model-ensemble text: model ensemble) of global hydrological models providing data to ISIMIP. The median represents the middle of the ensemble, meaning that 50% of the ensemble members provide higher numbers and 50% provide lower numbers. After the key message, which only references the median, you can find the model-specific results in the figures, a discussion of the methodology and the restrictions of the analysis at the end of the article.\n\
\n\
### Key messages\n\
* Without human-made greenhouse gas emissions, {world_land_tc_ov_md_0c}% of the global land area and {world_pop_tc_ov_md_0c}% of the world’s population would be affected by {indicator_short} each year, on average.\n\
* At today’s levels of 1 degrees Celsius of global warming the land area affected is {world_land_tc_rel_ov_md_1c_times} times as much: {world_land_tc_rel_ov_md_1c}% of the total land area, while the number of people affected is {world_pop_tc_rel_ov_md_1c_times} times as much: {world_pop_tc_ov_md_1c}% of the total population.\n\
* At 2 degrees Celsius of global warming, the global {land_indicator} is projected to increase by a factor of {world_land_tc_rel_ov_md_2c} compared to a world without human-made greenhouse gas emissions, to {world_land_tc_ov_md_0c}%. Likewise, the world’s {pop_indicator} is projected to increase by a factor {world_pop_tc_rel_ov_md_2c}, to {world_pop_tc_ov_md_0c}%.\n\
* Following the higher-emissions scenario (RCP6.0) which can entail over 3 degrees Celsius of global warming by the end of the century (2081-2100), this factor is projected to reach {world_land_rcp60_far_future_times} for the global land area affected to {indicator_short} (to {world_land_rcp60_far_future_times}%) and {world_pop_rcp60_far_future_times} for the world’s {pop_indicator} (to {world_pop_rcp60_far_future}%).\n\
* The countries that rank highest with regards to their relative change in {land_indicator} at 2 degrees Celsius of global warming in comparison to a situation without anthropogenic climate change, implying most severe impacts, are: (ranking-area: land-area-affected-by-river-flood-relative-changes_ISIMIP-projections_versus-temperature-change order: 1 value: name temperature: 2 type: country), (ranking-area: land-area-affected-by-river-flood-relative-changes_ISIMIP-projections_versus-temperature-change order: 2 value: name temperature: 2 type: country), (ranking-area: land-area-affected-by-river-flood-relative-changes_ISIMIP-projections_versus-temperature-change order: 3 value: name temperature: 2 type: country), (ranking-area: land-area-affected-by-river-flood-relative-changes_ISIMIP-projections_versus-temperature-change order: 4 value: name temperature: 2 type: country), (ranking-area: land-area-affected-by-river-flood-relative-changes_ISIMIP-projections_versus-temperature-change order: 5 value: name temperature: 2 type: country).\n\
* The countries that rank highest with regards to their relative change in {pop_indicator} at 2 degrees Celsius of global warming in comparison to a situation without anthropogenic climate change, implying most severe impacts, are: (ranking-area: population-exposed-to-river-flood-relative-changes_ISIMIP-projections_versus-temperature-change order: 1 value: name temperature: 2 type: country), (ranking-area: population-exposed-to-river-flood-relative-changes_ISIMIP-projections_versus-temperature-change order: 2 value: name temperature: 2 type: country), (ranking-area: population-exposed-to-river-flood-relative-changes_ISIMIP-projections_versus-temperature-change order: 3 value: name temperature: 2 type: country), (ranking-area: population-exposed-to-river-flood-relative-changes_ISIMIP-projections_versus-temperature-change order: 4 value: name temperature: 2 type: country), (ranking-area: population-exposed-to-river-flood-relative-changes_ISIMIP-projections_versus-temperature-change order: 5 value: name temperature: 2 type: country).\n\
\n\
### Results\n\
The figures below shows the relative change in the global land area affected by and world’s {pop_indicator} in comparison to the time period before anthropogenic climate change. Results are shown both for the (link: glossary/historical-period text: historical time period) and for the (link: glossary/future-projections text: future projections) and can be visualized with regards to their change over time as well as with regards to their change in terms of global warming. Under the ‘change in terms of time’ setting, the change in global land area affected by and the world’s {pop_indicator} over time is shown for 20-year (link: glossary/time-slices text: time-slices) from 1861-1880 until the end-of-the-century (2081-2100). Under the ‘change in terms of global warming’, the change in global land area affected by and the world’s {pop_indicator} is shown for 20-year (link: glossary/time-slices text time-slices) representing increasing levels of global warming from 0 degrees Celsius up to 3 degrees Celsius compared to the time period before anthropogenic climate change started.\n\
\n\
In both cases, results are shown for all possible combinations of (link: glossary/global-hydrological-models text: global hydrological models) and (link: glossary/global-climate-models text: global climate models) (normal lines) as well as for the median of the model ensemble (thick line). The influence of (link: glossary/inter-annual-variability text: inter-annual variability) on the results is visualized by means of the shaded area in black. This inter-annual variability is only shown for the median model combination. For the future projections and under the ‘change in terms of time’ settings only, an additional distinction is made between the results of two future (link: glossary/emissions-trajectories text: emissions trajectories): a low-emissions trajectory limiting global mean temperature in the 21st century to below 2 degrees Celsius compared to before anthropogenic climate change started, called RCP2.6 (blue lines), and a higher-emissions scenario leading global mean temperature to above 3 degrees Celsius by 2100, compared to pre-climate change conditions, called RCP6.0 (red lines). The shaded areas in blue and red indicate the variety (or spread) in results between all combinations of global hydrological models and global climate models for these two emissions trajectories. A filtering menu top-right of the graph allows the user to select individual emissions trajectories, individual global climate models, and individual global hydrological models for visualization.\n\
\n\
By hovering over or clicking on a particular value in the figure additional details, such as the specific global climate model or hydrological used, behind the presented value become available. The visualization below the graph shows, for the selected model run under this time-period or temperature-change level, how countries ranks in comparison to other countries on their relative change in land area affected by or {pop_indicator}.\n\
\n\
#### {land_indicator_capital}\n\
\n\
(line-plot: land-area-affected-by-drought-relative-changes_ISIMIP-projections_versus-temperature-change_world,land-area-affected-by-drought-relative-changes_ISIMIP-projections_versus-timeslices_world first-temperature: 2 second-scenario: rcp26 second-time: 2141-2160)
\n\
Without human-made greenhouse gas emissions, {world_land_tc_ov_md_0c}% of the global land area would be affected by {indicator_short} each year, on average.\n\
\n\
Under the ‘change in terms of global warming’ setting the figure shows that at today’s level of 1 degrees Celsius of global warming the global {land_indicator} is, on average, already {world_land_tc_rel_ov_md_1c_times} times (or {world_land_tc_rel_ov_md_1c}%) {world_land_tc_rel_ov_md_1c_times_higher_or_lower} and amount to {world_land_tc_ov_md_1c}% of the total land area. This level of change ranges from {world_minimum_land_tc_abs_ov_md_2c}% to {world_maximum_land_tc_abs_ov_md_2c}% for the individual combinations of global hydrological models and global climate models. At 2 degrees Celsius of global warming, the global {land_indicator} is projected to change by a factor of {world_land_tc_rel_ov_md_2c_times} (or {world_land_tc_abs_ov_md_2c}%) in comparison to a world without human-made greenhouse gas emissions. Under these conditions, {world_land_tc_ov_md_2c}% of the total land area would be affected by {indicator_short} on a yearly basis, on average. Across the individual combinations of global hydrological models and global climate models this expected level of change ranges from {world_minimum_land_tc_abs_ov_md_2c}% up to {world_maximum_land_tc_abs_ov_md_2c}%.\n\
\n\
When presenting the ‘change in terms of time’, we find that when following the higher-emissions scenario (RCP6.0) towards the end-of-the-century (equivalent to over 3 degrees Celsius change) would result in a change in the global {land_indicator} of, on average, a factor {world_land_rcp60_rel_far_future_times} ({world_land_rcp60_abs_far_future}%), towards: {world_land_rcp60_far_future}% of the total land area. Following the (link: glossary/climate-mitigation-emissions-scenario text: climate-mitigation emissions scenario)(RCP2.6) towards the end-of-the-century (entailing an average 2.5 degrees Celsius change) would result in a foreseen change in the global {land_indicator} of, on average, a factor {world_land_rcp26_rel_far_future_times} ({world_land_rcp26_abs_far_future}%), {world_land_rcp26_far_future}% of the total land area being affected.\n\
\n\
Worldwide, countries that rank highest with regards to their relative change in {land_indicator} at 2 degrees Celsius of global warming in comparison to a situation without anthropogenic climate change, implying most severe impacts, are: (ranking-area: land-area-affected-by-river-flood-relative-changes_ISIMIP-projections_versus-temperature-change order: 1 value: name temperature: 2 type: country), (ranking-area: land-area-affected-by-river-flood-relative-changes_ISIMIP-projections_versus-temperature-change order: 2 value: name temperature: 2 type: country), (ranking-area: land-area-affected-by-river-flood-relative-changes_ISIMIP-projections_versus-temperature-change order: 3 value: name temperature: 2 type: country), (ranking-area: land-area-affected-by-river-flood-relative-changes_ISIMIP-projections_versus-temperature-change order: 4 value: name temperature: 2 type: country), (ranking-area: land-area-affected-by-river-flood-relative-changes_ISIMIP-projections_versus-temperature-change order: 5 value: name temperature: 2 type: country).\n\
\n\
The countries that rank highest with regards to their relative change in {land_indicator} towards the-end-of-the-century under a higher-emissions scenario (RCP6.0), in comparison to a situation without anthropogenic climate change, implying most severe impacts, are: (ranking-area: land-area-affected-by-river-flood-relative-changes_ISIMIP-projections_versus-timeslices order: 1 value: name time: 2081-2100 scenario: rcp60 type: country), (ranking-area: land-area-affected-by-river-flood-relative-changes_ISIMIP-projections_versus-timeslices order: 2 value: name time: 2081-2100 scenario: rcp60 type: country), (ranking-area: land-area-affected-by-river-flood-relative-changes_ISIMIP-projections_versus-timeslices order: 3 value: name time: 2081-2100 scenario: rcp60 type: country), (ranking-area: land-area-affected-by-river-flood-relative-changes_ISIMIP-projections_versus-timeslices order: 4 value: name time: 2081-2100 scenario: rcp60 type: country), (ranking-area: land-area-affected-by-river-flood-relative-changes_ISIMIP-projections_versus-timeslices order: 5 value: name time: 2081-2100 scenario: rcp60 type: country).\n\
\n\
#### {pop_indicator_capital}\n\
\n\
(line-plot: population-exposed-to-drought-relative-changes_ISIMIP-projections_versus-temperature-change_world,population-exposed-to-drought-relative-changes_ISIMIP-projections_versus-timeslices_world first-temperature: 2 second-scenario: rcp26 second-time: 2141-2160)\n\
\n\
Without human-made greenhouse gas emissions, {world_pop_tc_ov_md_0c}% of the world’s population would be exposed to {indicator_short} each year, on average.\n\
\n\
Under the ‘change in terms of global warming’ setting the figure shows that at today’s level of 1 degrees Celsius of global warming the world’s {pop_indicator} is, on average, already {world_pop_tc_rel_ov_md_1c_times} times (or {world_pop_tc_rel_ov_md_1c}%) {world_pop_tc_rel_ov_md_1c_times_higher_or_lower}: {world_pop_tc_ov_md_1c}% of the total land area. This level of change ranges from {world_minimum_pop_tc_abs_ov_md_1c}% to {world_maximum_pop_tc_abs_ov_md_1c}% for the individual combinations of global hydrological models and global climate models. At 2 degrees Celsius of global warming, the world’s {pop_indicator} is projected to change by a factor of {world_pop_tc_rel_ov_md_2c_times} (or {world_pop_tc_abs_ov_md_2c}%) in comparison to a world without human-made greenhouse gas emissions. Under these conditions, {world_pop_tc_ov_md_2c}% of the total global population would be exposed to {indicator_short} on a yearly basis, on average. Across the individual combinations of global hydrological models and global climate models this expected level of change ranges from {world_minimum_pop_tc_abs_ov_md_2c}% up to {world_maximum_pop_tc_abs_ov_md_2c}%.\n\
\n\
When presenting the ‘change in terms of time’, we find that when following the higher-emissions scenario (RCP6.0) towards the end-of-the-century (equivalent to over 3 degrees Celsius change) would result in a foreseen change in the world’s {pop_indicator} of, on average, a factor {world_pop_rcp60_rel_far_future_times} ({world_pop_rcp60_abs_far_future}%),{world_pop_rcp60_far_future}% of the total population. Following the climate-mitigation emissions scenario (RCP2.6) towards the end-of-the-century (entailing an average 2.5 degrees Celsius change) would result in a foreseen change in the world’s {pop_indicator} of, on average, a factor {world_pop_rcp26_rel_far_future_times} ({world_pop_rcp26_abs_far_future}%), {world_pop_rcp26_far_future}% of the total global population being exposed.\n\
\n\
Worldwide, countries that rank highest with regards to their relative change in {pop_indicator} at 2 degrees Celsius of global warming in comparison to a situation without anthropogenic climate change, implying most severe impacts, are: (ranking-area: population-exposed-to-river-flood-relative-changes_ISIMIP-projections_versus-temperature-change order: 1 value: name temperature: 2 type: country), (ranking-area: population-exposed-to-river-flood-relative-changes_ISIMIP-projections_versus-temperature-change order: 2 value: name temperature: 2 type: country), (ranking-area: population-exposed-to-river-flood-relative-changes_ISIMIP-projections_versus-temperature-change order: 3 value: name temperature: 2 type: country), (ranking-area: population-exposed-to-river-flood-relative-changes_ISIMIP-projections_versus-temperature-change order: 4 value: name temperature: 2 type: country), (ranking-area: population-exposed-to-river-flood-relative-changes_ISIMIP-projections_versus-temperature-change order: 5 value: name temperature: 2 type: country).\n\
\n\
The countries that rank highest with regards to their relative change in {pop_indicator} towards the-end-of-the-century under a higher-emissions scenario (RCP6.0), in comparison to a situation without anthropogenic climate change, implying most severe impacts, are: (ranking-area: population-exposed-to-river-flood-relative-changes_ISIMIP-projections_versus-timeslices order: 1 value: name time: 2081-2100 scenario: rcp60 type: country), (ranking-area: population-exposed-to-river-flood-relative-changes_ISIMIP-projections_versus-timeslices order: 2 value: name time: 2081-2100 scenario: rcp60 type: country), (ranking-area: population-exposed-to-river-flood-relative-changes_ISIMIP-projections_versus-timeslices order: 3 value: name time: 2081-2100 scenario: rcp60 type: country), (ranking-area: population-exposed-to-river-flood-relative-changes_ISIMIP-projections_versus-timeslices order: 4 value: name time: 2081-2100 scenario: rcp60 type: country), (ranking-area: population-exposed-to-river-flood-relative-changes_ISIMIP-projections_versus-timeslices order: 5 value: name time: 2081-2100 scenario: rcp60 type: country).\n\
\n\
### Methodology\n\
\n\
#### What do we analyze?\n\
We analyze the {land_indicator} and the number of people exposed to {indicator_short} at different levels of global warming (0, 1, 2, and 3 degrees Celsius) and during different time periods. We cover the time before anthropogenic climate change started (1850), present-day (2001-2020), mid-century (2041-2060) and end-of-century (2081-2100). We compare the later periods against the climate conditions before anthropogenic climate change (1850).\n\
\n\
#### How do we calculate where and when a flood occurs?\n\
The calculation has several steps: 1) calculate (link: glossary/runoff text: runoff); 2) calculate daily river flow and its (link: glossary/annual-maximum text: annual maximum); 3) compare this annual maximum with the 100-year (link: glossary/return-level text: return level) which is calculated separately when the 100-year return level is exceeded, 4) calculate (link: glossary/flood-depth text: flood depth); and 5) calculate flooded land area fraction. All these steps are detailed below, after a short explanation of the spatial structure on which our models operate.\n\
\n\
#### What is the spatial structure of the models?\n\
The models we use cover the whole globe’s land area. The land area is divided into a grid. Each grid cell has a size of 0.5 degrees × 0.5 degrees (latitude by longitude). At the equator, this equals roughly 55 × 55 km; towards the North Pole or South Pole, where the land area covered per grid cell becomes smaller.\n\
\n\
#### How is runoff calculated?\n\
The calculation is done for each grid cell and each day. Information about temperature, precipitation, solar radiation, and other weather indicators is taken from the global climate models (GCMs) and used as input for the ISIMIP global hydrological models (GHMs). Additional spatial data, such as soil, land cover and water bodies are also inputted. Runoff is calculated as the difference between the amount of water coming in as rain or snow, and the amount of water going out, either through evapotranspiration from the surface and vegetation, or by seeping vertically into the ground. Runoff percolates horizontally through the ground (subsurface runoff) or flows on the surface (surface runoff) into the surface water bodies or river. The model calculates runoff as daily value for each grid cell.\n\
\n\
#### How is river flow calculated?\n\
Having calculated runoff in each grid cell, we use the global river model (link: glossary/camaflood text: CaMaFlood) to calculate the water flow once it is in the river. The river water flow is also known as discharge, and measured in cubic meters per second (m³/s). For each grid cell along the river, the amount of water flowing through the river is calculated by summing up the runoff coming from all grid cells located upstream. For each grid cell, we then calculate the annual maximum of the daily river flow values.\n\
\n\
#### How do we know whether a flood occurs?\n\
In our analysis, we assume that a flood occurs whenever the annual maximum daily river flow exceeds the so-called 100-year return level. This is the water flow that was exceeded only once every 100 years, on average, before anthropogenic climate change started. We only consider river flows larger than the 100-year return level, because we assume that for smaller flows, either no flooding occurs (e.g. protection measures such as levees prevent them) or the floods have minor impacts (e.g. people do not settle in these areas or the flood depth is very shallow). That is, we assume that societies have already adapted to more frequent events.\n\
\n\
#### How do we know how often floods occurred before anthropogenic climate change started?\n\
We use a separate model simulation in which the climate behaves as if there had been no human-made greenhouse gas emissions. This simulation runs for several centuries without any outside change, just letting the weather evolve naturally. We then calculate the maximum river flow level that occurs, on average, every 100 years in this simulation.\n\
\n\
#### How is flood depth calculated?\n\
Once there is a flood in a given grid cell and year, we obtain the flood depth from a calculation based on the unique relationship of flood depth with return level. This relationship between return level and flood depth is based on (link: glossary/calibrated-simulations text: calibrated simulations) from the global hydrological model (link: glossary/matsiro text: MATSIRO) in combination with CaMaFlood.\n\
\n\
#### How is the flooded land area fraction calculated?\n\
For each flood-affected grid cell, the flood-water volume is calculated from the flood depth and the size of the cell. This volume of water is then distributed onto a high-resolution elevation map (~100m x 100m at the equator). This map is part of CaMaFlood. The elevation map acts as a basin, with each point in the map assigned a height above sea-level.\n\
The portion of each 0.5 degree x 0.5 degree grid cell that is submerged is calculated. For example, if it is a mountainous area, all the flood water will concentrate in the narrow valleys, while the mountain peaks do not get flooded. Thus, only a part of the 0.5 degree x 0.5 degree grid cell will be submerged even during a large flood. On the contrary, if the area is very flat, then the flood water will spread out and potentially submerge the entire grid cell.\n\
\n\
#### How are the indicators {land_indicator} and number of people exposed to {indicator_short} calculated?\n\
To calculate the global land area affected by flooding, the flooded land area fractions are added up across all 0.5 degree x 0.5 degree grid cells worldwide, except for Antarctica and Greenland. To calculate the global number of people exposed to flooding, we first multiply the flooded land area fraction of each grid cell by the number of people living in that grid cell to estimate the number of people exposed to {indicator_short}, and then add up those numbers across all grid cells worldwide, except for Antarctica and Greenland.\n\
\n\
#### What else should I know about the methodology?\n\
We assume that the number of people living in an area, as well as the area’s land use and land cover (what fractions of the area are used for settlement, cropland, or pasture, or covered by forest), remain constant at the levels of year 2005 throughout the whole simulation. This is not meant to be realistic, but to isolate the influence of climate change from the influence of other changes.\n\
\n\
In the key messages we report the results for the median (the model in the middle) of the group of global hydrological models that ran simulations in (link: glossary/isimip2b text: ISIMIP2b). All model-specific results are presented in the figures and a discussion of the limitations of the analysis is included at the end of the report.\n\
\n\
A ranking of countries for each indicator is also provided to compare countries on the basis of their relative change in land area affected or number of people exposed under different levels of global warming and for various time horizons, compared to conditions without climate change. A ranking of 1 implies that the country experiences a change in the indicator higher than all other ranked countries, for example the strongest impacts from climate change; whereas a lower ranking entails comparatively less impacts.\n\
\n\
### Discussion\n\
The model simulations used for this report build on science that has been established through many peer-reviewed studies: e.g. by [Yamazaki et al. (2011)](https://doi.org/10.1029/2010WR009726),[Müller Schmied et al. (2016)](https://doi.org/10.5194/hess-20-2877-2016). Models are simplified representations of reality, hence model simulations come with limitations and uncertainties that have to be kept in mind. One major limitation of the global water models is the availability of global data sets that are needed to fully represent the global hydrological cycle. For example, many of the models do not consider glaciers which could influence {indicator_short} as well. Furthermore, the representation of the components of the hydrological cycle, such as soil hydrology, differ strongly between models (e.g. in terms of detail, but also the calculation approach) with large effects on runoff generation. Another major source of uncertainty are the climatic input data as they stem from climate models that have a coarser spatial resolution and their own (link: glossary/modelling-uncertainties text: modelling uncertainties). In particular, the adequate simulation of precipitation extremes is difficult for global climate models.\n\
\n\
The performance of the global water models themselves can be tested by using (link: glossary/observed-historical-weather-information text: observed historical weather information) as inputs, and comparing the simulated river flow to river flow observed at different stations along rivers. One general challenge associated with the simulation of hydrological processes lies in the representation of how vegetation cover affects evapotranspiration and other surface properties that play a role in flood onset. Moreover, this relationship may change within a given river basin, or with rising temperature and CO2 levels. For example, the effect of CO2 fertilization – the phenomenon through which photosynthesis, hence plant growth, should be enhanced in a CO2-richer atmosphere – is not represented in most water models although it would affect the plants’ water use, with consequences for runoff and river flow. Nevertheless, although these vegetation-related processes are critical for the projection of drought conditions and low-flow events, they are of less importance for projections of {indicator_short}. A close relationship indeed exists between precipitation and peak discharge during flood events, which is only moderately affected by evapotranspiration.\n\
\n\
The presented flood projections reflect the isolated effect of climate change, while their local manifestations are expected to also be influenced by direct human drivers like changes in irrigation, construction of new dams and reservoirs, levees and other flood protection infrastructure. The representation of these drivers is limited to (link: glossary/present-day-conditions text: present-day conditions), while their future changes are not explicitly modelled in the presented simulations. This serves the purpose of isolating the effect of anthropogenic climate change from other factors, but it means that actual flood exposure in the future could be more or less acute, depending on non-climatic human drivers, such as urbanization or adaptation.\n\
\n\
Our methodology assumes that every event where river flow exceeds the local 100-year return level is a flood. This is a simplification; flood protection measures may have a higher or lower protection standard in reality. Most parts of the world are protected only against lower-intensity events that occur more frequently than once in 100 years. This means that more floods would actually occur than in our projections. In a few parts of the world (mainly the USA and a few European countries), the opposite is true, meaning that protection measures could prevent all river flow events that are simulated to occur up to as rarely as once in 200 years.\n\
\n\
Finally, another caveat to keep in mind is that only a single {indicator_short} model (CaMaFlood) was used for the calculation of river flow and flooded area; and a single global hydrological model, MATSIRO, was used to derive the grid cell-specific relationship between return level and flood depth. It is, therefore, difficult to assess the uncertainty that arises from assumptions built into these models.\n\
\n\
Regarding climate models and water models, it is known that generally both types of models contribute substantially to the overall spread in projected climate change impacts on river flow and other water-related variables. Because this report presents the results of a combination of climate models and water models that ran simulations based on the same experiment protocol, and whose outputs are thus directly comparable, it captures at least some of this spread in the projections.""".format(
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
                    text = """This (link: glossary/climate-impact-assessment text: climate impact) assessment presents (link: glossary/projections text: projections) of the {land_indicator} and the number of people exposed to {indicator_short} in {country}, based on {impact_model_list} different (link: glossary/global-hydrological-models text: global hydrological models) (GHMs) and {climate_model_list} different global (link: glossary/climate-models text: climate models)(GCMs) participating in [ISIMIP](https://www.isimip.org/).\n\
\n\
Here, (link: glossary/river-floods text: {indicator_short}) refer to a situation where the daily (link: glossary/river-flow text: river flow) exceeds the so-called 100-year (link: glossary/return-level text: return level). For each (link: glossary/grid-cell text: grid cell), which covers an area of up to 50x50 square-kilometers affected to {indicator_short}, we calculate the percentage of area flooded by redistributing the (link: glossary/flood-volume text: flood volume) per cell in accordance variations in (link: glossary/surface-elevation text: surface elevation). To calculate the {land_indicator} for {country}, the percentage of area flooded are added up across all grid cells belonging to {country}. To calculate the number of people exposed to {indicator_short}, we first multiply the percentage of area flooded of each grid cell by the number of people living in that grid cell to estimate the number of people exposed to {indicator_short}, and then add up those numbers across all grid cells belonging to {country}.\n\
\n\
We analyze the {land_indicator} and the number of people exposed to {indicator_short} at different (link: glossary/levels-of-global-warming text: levels of global warming)(0, 1, 2, and 3 degrees Celsius) and during different time periods. We cover the time before (link: glossary/anthropogenic-climate-change text: anthropogenic climate change) started (conventionally set at 1850), present-day (2001-2020), mid-century (2041-2060) and end-of-century (2081-2100). We compare the later periods against the climate conditions before anthropogenic climate change started (1850). A ranking of countries for each indicator is provided to allow comparison between countries on the basis of their (link: glossary/relative-change text: relative change) in the land area affected or the number of people exposed under different levels of global warming and for various time horizons, compared to conditions before anthropogenic climate change started. Here, a ranking of 1 implies that the country experiences a change in the (link: glossary/indicator text: indicator) that is more than all other ranked countries, whereas a lower ranking entails comparatively less effects due to climate change.\n\
\n\
It is important to note that our (link: glossary/future-projections text: future projections) assume that the number of people living in an area, as well as the area’s (link: glossary/land-use text: land use) and (link: glossary/land-cover text: land cover), remain constant to that of the year 2005. This is not necessarily meant to be realistic, but to isolate the influence of climate change from the influence of other changes.\n\
\n\
In the key messages we report the results for the (link: glossary/median text: median) of the (link: glossary/model-ensemble text: model ensemble) of global hydrological models providing data to ISIMIP. The median represents the middle of the ensemble, meaning that 50% of the ensemble members provide higher numbers and 50% provide lower numbers. After the key message, which only references the median, you can find the model-specific results in the figures, a discussion of the methodology and the restrictions of the analysis at the end of the article.\n\
\n\
### Key messages\n\
* Without human-made greenhouse gas emissions, {land_tc_ov_md_0c}% of {country_apostrophe} land area and {pop_tc_ov_md_0c}% of {country_apostrophe} population would be affected by {indicator_short} each year, on average.\n\
* At today’s levels of 1 degrees Celsius of global warming the land area affected is {land_tc_rel_ov_md_1c_times} times as much: {land_tc_rel_ov_md_1c}% of the total land area, while the number of people affected is {pop_tc_rel_ov_md_1c_times} times as much: {pop_tc_ov_md_1c}% of the total population.\n\
* At 2 degrees Celsius of global warming, {country_apostrophe} {land_indicator} is projected to increase by a factor of {land_tc_rel_ov_md_2c} compared to a world without human-made greenhouse gas emissions, to {land_tc_ov_md_0c}%. Likewise, {country_apostrophe} {pop_indicator} is projected to increase by a factor {pop_tc_rel_ov_md_2c}, to {pop_tc_ov_md_0c}%.\n\
* Following the higher-emissions scenario (RCP6.0) which can entail over 3 degrees Celsius of global warming by the end of the century (2081-2100), this factor is projected to reach {land_rcp60_far_future_times} for the land area affected to {indicator_short} (to {land_rcp60_far_future_times}%) and {pop_rcp60_far_future_times} for the {pop_indicator} (to {pop_rcp60_far_future}%).\n\
* {country} ranks {rank_land_tc_rel_2c} with regards to its relative change in {land_indicator} at 2 degrees Celsius of global warming in comparison to a situation without anthropogenic climate change. For the relative change in {pop_indicator}, {country_apostrophe} ranking is {rank_pop_tc_rel_2c}.\n\
\n\
### Results\n\
The figures below shows the relative change in {country_apostrophe} land area affected by and {pop_indicator} in comparison to the time period before anthropogenic climate change. Results are shown both for the (link: glossary/historical-period text: historical time period) and for the (link: glossary/future-projections text: future projections) and can be visualized with regards to their change over time as well as with regards to their change in terms of global warming. Under the ‘change in terms of time’ setting, the change in land area affected by and {pop_indicator} over time is shown for 20-year (link: glossary/time-slices text: time-slices) from 1861-1880 until the end-of-the-century (2081-2100). Under the ‘change in terms of global warming’, the change in land area affected by and {pop_indicator} is shown for 20-year (link: glossary/time-slices text time-slices) representing increasing levels of global warming from 0 degrees Celsius up to 3 degrees Celsius compared to the time period before anthropogenic climate change started.\n\
\n\
In both cases, results are shown for all possible combinations of (link: glossary/global-hydrological-models text: global hydrological models) and (link: glossary/global-climate-models text: global climate models) (normal lines) as well as for the median of the model ensemble (thick line). The influence of (link: glossary/inter-annual-variability text: inter-annual variability) on the results is visualized by means of the shaded area in black. This inter-annual variability is only shown for the median model combination. For the future projections and under the ‘change in terms of time’ settings only, an additional distinction is made between the results of two future (link: glossary/emissions-trajectories text: emissions trajectories): a low-emissions trajectory limiting global mean temperature in the 21st century to below 2 degrees Celsius compared to before anthropogenic climate change started, called RCP2.6 (blue lines), and a higher-emissions scenario leading global mean temperature to above 3 degrees Celsius by 2100, compared to pre-climate change conditions, called RCP6.0 (red lines). The shaded areas in blue and red indicate the variety (or spread) in results between all combinations of global hydrological models and global climate models for these two emissions trajectories. A filtering menu top-right of the graph allows the user to select individual emissions trajectories, individual global climate models, and individual global hydrological models for visualization.\n\
\n\
By hovering over or clicking on a particular value in the figure additional details, such as the specific global climate model or hydrological used, behind the presented value become available. The visualization below the graph shows, for the selected model run under this time-period or temperature-change level, how {country} ranks in comparison to other countries on its relative change in land area affected by or {pop_indicator}.\n\
\n\
#### {land_indicator_capital}\n\
\n\
(line-plot: land-area-affected-by-drought-relative-changes_ISIMIP-projections_versus-temperature-change_{country_name},land-area-affected-by-drought-relative-changes_ISIMIP-projections_versus-timeslices_{country_name} first-temperature: 2 second-scenario: rcp26 second-time: 2141-2160)\n\
\n\
Without human-made greenhouse gas emissions, {land_tc_ov_md_0c}% of {country_apostrophe} land area would be affected by {indicator_short} each year, on average.\n\
\n\
Under the ‘change in terms of global warming’ setting the figure shows that at today’s level of 1 degrees Celsius of global warming {country_apostrophe} {land_indicator} is, on average, already {land_tc_rel_ov_md_1c_times} times (or {land_tc_rel_ov_md_1c}%) {land_tc_rel_ov_md_1c_times_higher_or_lower} and amount to {land_tc_ov_md_1c}% of the total land area. This level of change ranges from {minimum_land_tc_abs_ov_md_2c}% to {maximum_land_tc_abs_ov_md_2c}% for the individual combinations of global hydrological models and global climate models. At 2 degrees Celsius of global warming, {country_apostrophe} {land_indicator} is projected to change by a factor of {land_tc_rel_ov_md_2c_times} (or {land_tc_abs_ov_md_2c}%) in comparison to a world without human-made greenhouse gas emissions. Under these conditions, {land_tc_ov_md_2c}% of the total land area would be affected by {indicator_short} on a yearly basis, on average. Across the individual combinations of global hydrological models and global climate models this expected level of change ranges from {minimum_land_tc_abs_ov_md_2c}% up to {maximum_land_tc_abs_ov_md_2c}%.\n\
\n\
When presenting the ‘change in terms of time’, we find that when following the higher-emissions scenario (RCP6.0) towards the end-of-the-century (equivalent to over 3 degrees Celsius change) would result in a change in the {land_indicator} of, on average, a factor {land_rcp60_rel_far_future_times} ({land_rcp60_abs_far_future}%), towards: {land_rcp60_far_future}% of the total land area. Following the (link: glossary/climate-mitigation-emissions-scenario text: climate-mitigation emissions scenario)(RCP2.6) towards the end-of-the-century (entailing an average 2.5 degrees Celsius change) would result in a foreseen change in the {land_indicator} of, on average, a factor {land_rcp26_rel_far_future_times} ({land_rcp26_abs_far_future}%), {land_rcp26_far_future}% of the total land area being affected.\n\
\n\
Globally, the {land_indicator} each year, on average, is {world_land_tc_ov_md_0c}% in a situation without human-made greenhouse gas emissions. At 2 degrees Celsius global warming or by the end-of-the-century under a higher-emissions scenario (RCP6.0) these values are foreseen to increase globally by a factor {world_land_tc_rel_ov_md_2c_times} and {world_land_rcp60_rel_far_future_times}%, respectively.\n\
\n\
As such, {country} ranks {rank_land_tc_rel_2c} with regards to its relative change in {land_indicator} at 2 degrees Celsius of global warming in comparison to a situation without anthropogenic climate change. For the relative change in {land_indicator} towards the-end-of-the-century under a higher-emissions scenario (RCP6.0), {country_apostrophe} ranking is {rank_land_tc_rel_2081_2100}.\n\
\n\
#### {pop_indicator_capital}\n\
\n\
(line-plot: population-exposed-to-drought-relative-changes_ISIMIP-projections_versus-temperature-change_{country_name},population-exposed-to-drought-relative-changes_ISIMIP-projections_versus-timeslices_{country_name} first-temperature: 2 second-scenario: rcp26 second-time: 2141-2160)\n\
\n\
Without human-made greenhouse gas emissions, {pop_tc_ov_md_0c}% of {country_apostrophe} population would be exposed to {indicator_short} each year, on average.\n\
\n\
Under the ‘change in terms of global warming’ setting the figure shows that at today’s level of 1 degrees Celsius of global warming {country_apostrophe} {pop_indicator} is, on average, already {pop_tc_rel_ov_md_1c_times} times (or {pop_tc_rel_ov_md_1c}%) {pop_tc_rel_ov_md_1c_times_higher_or_lower}: {pop_tc_ov_md_1c}% of the total land area. This level of change ranges from {minimum_pop_tc_abs_ov_md_1c}% to {maximum_pop_tc_abs_ov_md_1c}% for the individual combinations of global hydrological models and global climate models. At 2 degrees Celsius of global warming, {country_apostrophe} {pop_indicator} is projected to change by a factor of {pop_tc_rel_ov_md_2c_times} (or {pop_tc_abs_ov_md_2c}%) in comparison to a world without human-made greenhouse gas emissions. Under these conditions, {pop_tc_ov_md_2c}% of the total population would be exposed to {indicator_short} on a yearly basis, on average. Across the individual combinations of global hydrological models and global climate models this expected level of change ranges from {minimum_pop_tc_abs_ov_md_2c}% up to {maximum_pop_tc_abs_ov_md_2c}%.\n\
\n\
When presenting the ‘change in terms of time’, we find that when following the higher-emissions scenario (RCP6.0) towards the end-of-the-century (equivalent to over 3 degrees Celsius change) would result in a foreseen change in the {pop_indicator} of, on average, a factor {pop_rcp60_rel_far_future_times} ({pop_rcp60_abs_far_future}%),{pop_rcp60_far_future}% of the total population. Following the climate-mitigation emissions scenario (RCP2.6) towards the end-of-the-century (entailing an average 2.5 degrees Celsius change) would result in a foreseen change in the {pop_indicator} of, on average, a factor {pop_rcp26_rel_far_future_times} ({pop_rcp26_abs_far_future}%), {pop_rcp26_far_future}% of the total population being exposed.\n\
\n\
Globally, the {pop_indicator} each year, on average, is {world_pop_tc_ov_md_0c}% in a situation without human-made greenhouse gas emissions. At 2 degrees of global warming or by the end-of-the-century under a higher-emissions scenario (RCP6.0) these values are foreseen to increase globally by {world_pop_tc_rel_ov_md_2c_times}% and {world_pop_rcp60_rel_far_future_times}% respectively.\n\
\n\
As such, {country} ranks {rank_pop_tc_rel_2c} with regards to its relative change in {pop_indicator} at 2 degrees Celsius of global warming in comparison to a situation without anthropogenic climate change. For the relative change in {pop_indicator} towards the-end-of-the-century under a business-as-usual emissions scenario, {country_apostrophe} ranking is {rank_pop_tc_rel_2081_2100}.\n\
\n\
### Methodology\n\
\n\
#### What do we analyze?\n\
We analyze the {land_indicator} and the number of people exposed to {indicator_short} at different levels of global warming (0, 1, 2, and 3 degrees Celsius) and during different time periods. We cover the time before anthropogenic climate change started (1850), present-day (2001-2020), mid-century (2041-2060) and end-of-century (2081-2100). We compare the later periods against the climate conditions before anthropogenic climate change (1850).\n\
\n\
#### How do we calculate where and when a flood occurs?\n\
The calculation has several steps: 1) calculate (link: glossary/runoff text: runoff); 2) calculate daily river flow and its (link: glossary/annual-maximum text: annual maximum); 3) compare this annual maximum with the 100-year (link: glossary/return-level text: return level) which is calculated separately when the 100-year return level is exceeded, 4) calculate (link: glossary/flood-depth text: flood depth); and 5) calculate flooded land area fraction. All these steps are detailed below, after a short explanation of the spatial structure on which our models operate.\n\
\n\
#### What is the spatial structure of the models?\n\
The models we use cover the whole globe’s land area. The land area is divided into a grid. Each grid cell has a size of 0.5 degrees × 0.5 degrees (latitude by longitude). At the equator, this equals roughly 55 × 55 km; towards the North Pole or South Pole, where the land area covered per grid cell becomes smaller.\n\
\n\
#### How is runoff calculated?\n\
The calculation is done for each grid cell and each day. Information about temperature, precipitation, solar radiation, and other weather indicators is taken from the global climate models (GCMs) and used as input for the ISIMIP global hydrological models (GHMs). Additional spatial data, such as soil, land cover and water bodies are also inputted. Runoff is calculated as the difference between the amount of water coming in as rain or snow, and the amount of water going out, either through evapotranspiration from the surface and vegetation, or by seeping vertically into the ground. Runoff percolates horizontally through the ground (subsurface runoff) or flows on the surface (surface runoff) into the surface water bodies or river. The model calculates runoff as daily value for each grid cell.\n\
\n\
#### How is river flow calculated?\n\
Having calculated runoff in each grid cell, we use the global river model (link: glossary/camaflood text: CaMaFlood) to calculate the water flow once it is in the river. The river water flow is also known as discharge, and measured in cubic meters per second (m³/s). For each grid cell along the river, the amount of water flowing through the river is calculated by summing up the runoff coming from all grid cells located upstream. For each grid cell, we then calculate the annual maximum of the daily river flow values.\n\
\n\
#### How do we know whether a flood occurs?\n\
In our analysis, we assume that a flood occurs whenever the annual maximum daily river flow exceeds the so-called 100-year return level. This is the water flow that was exceeded only once every 100 years, on average, before anthropogenic climate change started. We only consider river flows larger than the 100-year return level, because we assume that for smaller flows, either no flooding occurs (e.g. protection measures such as levees prevent them) or the floods have minor impacts (e.g. people do not settle in these areas or the flood depth is very shallow). That is, we assume that societies have already adapted to more frequent events.\n\
\n\
#### How do we know how often floods occurred before anthropogenic climate change started?\n\
We use a separate model simulation in which the climate behaves as if there had been no human-made greenhouse gas emissions. This simulation runs for several centuries without any outside change, just letting the weather evolve naturally. We then calculate the maximum river flow level that occurs, on average, every 100 years in this simulation.\n\
\n\
#### How is flood depth calculated?\n\
Once there is a flood in a given grid cell and year, we obtain the flood depth from a calculation based on the unique relationship of flood depth with return level. This relationship between return level and flood depth is based on (link: glossary/calibrated-simulations text: calibrated simulations) from the global hydrological model (link: glossary/matsiro text: MATSIRO) in combination with CaMaFlood.\n\
\n\
#### How is the flooded land area fraction calculated?\n\
For each flood-affected grid cell, the flood-water volume is calculated from the flood depth and the size of the cell. This volume of water is then distributed onto a high-resolution elevation map (~100m x 100m at the equator). This map is part of CaMaFlood. The elevation map acts as a basin, with each point in the map assigned a height above sea-level.\n\
The portion of each 0.5 degree x 0.5 degree grid cell that is submerged is calculated. For example, if it is a mountainous area, all the flood water will concentrate in the narrow valleys, while the mountain peaks do not get flooded. Thus, only a part of the 0.5 degree x 0.5 degree grid cell will be submerged even during a large flood. On the contrary, if the area is very flat, then the flood water will spread out and potentially submerge the entire grid cell.\n\
\n\
#### How are the indicators {land_indicator} and number of people exposed to {indicator_short} calculated?\n\
To calculate the land area affected by flooding for {country}, the flooded land area fractions are added up across all 0.5 degree x 0.5 degree grid cells belonging to {country}. To calculate the number of people exposed to flooding, we first multiply the flooded land area fraction of each grid cell by the number of people living in that grid cell to estimate the number of people exposed to {indicator_short}, and then add up those numbers across all grid cells belonging to {country}.\n\
\n\
#### What else should I know about the methodology?\n\
We assume that the number of people living in an area, as well as the area’s land use and land cover (what fractions of the area are used for settlement, cropland, or pasture, or covered by forest), remain constant at the levels of year 2005 throughout the whole simulation. This is not meant to be realistic, but to isolate the influence of climate change from the influence of other changes.\n\
\n\
In the key messages we report the results for the median (the model in the middle) of the group of global hydrological models that ran simulations in (link: glossary/isimip2b text: ISIMIP2b). All model-specific results are presented in the figures and a discussion of the limitations of the analysis is included at the end of the report.\n\
\n\
A ranking of countries for each indicator is also provided to compare countries on the basis of their relative change in land area affected or number of people exposed under different levels of global warming and for various time horizons, compared to conditions without climate change. A ranking of 1 implies that the country experiences a change in the indicator higher than all other ranked countries, for example the strongest impacts from climate change; whereas a lower ranking entails comparatively less impacts.\n\
\n\
### Discussion\n\
The model simulations used for this report build on science that has been established through many peer-reviewed studies: e.g. by [Yamazaki et al. (2011)](https://doi.org/10.1029/2010WR009726),[Müller Schmied et al. (2016)](https://doi.org/10.5194/hess-20-2877-2016). Models are simplified representations of reality, hence model simulations come with limitations and uncertainties that have to be kept in mind. One major limitation of the global water models is the availability of global data sets that are needed to fully represent the global hydrological cycle. For example, many of the models do not consider glaciers which could influence {indicator_short} as well. Furthermore, the representation of the components of the hydrological cycle, such as soil hydrology, differ strongly between models (e.g. in terms of detail, but also the calculation approach) with large effects on runoff generation. Another major source of uncertainty are the climatic input data as they stem from climate models that have a coarser spatial resolution and their own (link: glossary/modelling-uncertainties text: modelling uncertainties). In particular, the adequate simulation of precipitation extremes is difficult for global climate models.\n\
\n\
The performance of the global water models themselves can be tested by using (link: glossary/observed-historical-weather-information text: observed historical weather information) as inputs, and comparing the simulated river flow to river flow observed at different stations along rivers. One general challenge associated with the simulation of hydrological processes lies in the representation of how vegetation cover affects evapotranspiration and other surface properties that play a role in flood onset. Moreover, this relationship may change within a given river basin, or with rising temperature and CO2 levels. For example, the effect of CO2 fertilization – the phenomenon through which photosynthesis, hence plant growth, should be enhanced in a CO2-richer atmosphere – is not represented in most water models although it would affect the plants’ water use, with consequences for runoff and river flow. Nevertheless, although these vegetation-related processes are critical for the projection of drought conditions and low-flow events, they are of less importance for projections of {indicator_short}. A close relationship indeed exists between precipitation and peak discharge during flood events, which is only moderately affected by evapotranspiration.\n\
\n\
The presented flood projections reflect the isolated effect of climate change, while their local manifestations are expected to also be influenced by direct human drivers like changes in irrigation, construction of new dams and reservoirs, levees and other flood protection infrastructure. The representation of these drivers is limited to (link: glossary/present-day-conditions text: present-day conditions), while their future changes are not explicitly modelled in the presented simulations. This serves the purpose of isolating the effect of anthropogenic climate change from other factors, but it means that actual flood exposure in the future could be more or less acute, depending on non-climatic human drivers, such as urbanization or adaptation.\n\
\n\
Our methodology assumes that every event where river flow exceeds the local 100-year return level is a flood. This is a simplification; flood protection measures may have a higher or lower protection standard in reality. Most parts of the world are protected only against lower-intensity events that occur more frequently than once in 100 years. This means that more floods would actually occur than in our projections. In a few parts of the world (mainly the USA and a few European countries), the opposite is true, meaning that protection measures could prevent all river flow events that are simulated to occur up to as rarely as once in 200 years.\n\
\n\
Finally, another caveat to keep in mind is that only a single {indicator_short} model (CaMaFlood) was used for the calculation of river flow and flooded area; and a single global hydrological model, MATSIRO, was used to derive the grid cell-specific relationship between return level and flood depth. It is, therefore, difficult to assess the uncertainty that arises from assumptions built into these models.\n\
\n\
Regarding climate models and water models, it is known that generally both types of models contribute substantially to the overall spread in projected climate change impacts on river flow and other water-related variables. Because this report presents the results of a combination of climate models and water models that ran simulations based on the same experiment protocol, and whose outputs are thus directly comparable, it captures at least some of this spread in the projections.""".format(
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

    
