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
             country_apostrophe   = data_land_years['region']+'\''
           else:
             country_apostrophe   = data_land_years['region']+'\'s'
             
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
           world_land_tc_ov_md_1c_times = round((to_zero(data_land_temperature_change['data']['overall']['median'][2]/100)+1),3)


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

           world_rank_land_tc_rel_2c        = '(ranking-value: land-area-affected-by-river-flood-relative-changes_ISIMIP-projections_AFG value: position)' #Should show ranking with regards to relative change in land area affected under 2 degrees temperature change
           world_rank_land_tc_rel_2c_high_or_low = 'high'#Can we make this flexible to the outcome: e.g. if the ranking is  <100 it is ‘high’, if the ranking is >100 it is ‘low’. Probably CDLX should provide this information. Or we need to calculate the rankings ourselves.
           world_rank_land_rcp60_rel_far_future  = '(ranking-value: land-area-affected-by-river-flood-relative-changes_ISIMIP-projections_AFG value: position)'
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
           world_pop_tc_rel_ov_md_1c_times = round((to_zero(data_pop_temperature_change_relative_changes['data']['overall']['median'][2]/100)+1),3)
           world_pop_tc_rel_ov_md_2c_times = round((to_zero(data_pop_temperature_change_relative_changes['data']['overall']['median'][4]/100)+1),3)

           world_pop_tc_ov_md_0c           = round(to_zero(data_pop_temperature_change['data']['overall']['median'][0]),3) 
           world_pop_tc_ov_md_1c           = round(to_zero(data_pop_temperature_change['data']['overall']['median'][2]),3) 
           world_pop_tc_ov_md_2c           = round(to_zero(data_pop_temperature_change['data']['overall']['median'][4]),3) 
           #world_pop_substract_2_and_1     = round(pop_tc_ov_md_2c - pop_tc_ov_md_1c,3)

           world_pop_tc_rel_ov_md_2c       = round(to_zero(data_pop_temperature_change_relative_changes['data']['overall']['median'][4]),3) 

           world_pop_pc_abs_today          = round(to_zero(data_pop_timeslices_absolute_changes['data']['rcp60']['overall']['median'][17]),3)
           world_pop_pc_abs_far_future     = round(to_zero(data_pop_timeslices_absolute_changes['data']['piControl']['overall']['median'][21]),3)
           world_pop_pc_rel_far_future     = round(to_zero(data_pop_timeslices_relative_changes['data']['piControl']['overall']['median'][21]),3)

           world_pop_rcp26_abs_far_future  = round(to_zero(data_pop_timeslices_absolute_changes['data']['rcp26']['overall']['median'][21]),3)
           world_pop_rcp60_abs_far_future  = round(to_zero(data_pop_timeslices_absolute_changes['data']['rcp60']['overall']['median'][21]),3)
           world_pop_rcp26_rel_far_future  = round(to_zero(data_pop_timeslices_relative_changes['data']['rcp26']['overall']['median'][21]),3)
           world_pop_rcp60_rel_far_future  = round(to_zero(data_pop_timeslices_relative_changes['data']['rcp60']['overall']['median'][21]),3)
           world_pop_rcp26_far_future      = round(to_zero(data_pop_timeslices['data']['rcp26']['overall']['median'][21]),3)
           world_pop_rcp60_far_future      = round(to_zero(data_pop_timeslices['data']['rcp60']['overall']['median'][21]),3)
           world_pop_rcp60_far_future_times = round((to_zero(data_pop_timeslices['data']['rcp60']['overall']['median'][21])/100+1),3)
           world_pop_rcp60_rel_far_future_times = round((to_zero(data_pop_timeslices_relative_changes['data']['rcp60']['overall']['median'][21])/100+1),3)

           world_rank_pop_tc_rel_2c       = '(ranking-value: population-exposed-to-river-flood-relative-changes_ISIMIP-projections_AFG value: position)'# Should show ranking with regards to relative change in population exposed under 2 degrees temperature change
           world_rank_pop_tc_rel_2c_high_or_low = 'high'#Can we make this flexible to the outcome: e.g. if the ranking is  <100 it is ‘high’, if the ranking is >100 it is ‘low’. Probably CDLX should provide this information. Or we need to calculate the rankings ourselves.
           world_rank_pop_rcp60_rel_far_future  = '(ranking-value: population-exposed-to-river-flood-relative-changes_ISIMIP-projections_AFG value: position)'
           world_rank_pop_rcp60_rel_far_future_high_or_low = 'high' 
    
           text = """This climate impact assessment presents projections of the land area affected by and people exposed to {indicator_short} at the global scale based on 8 different global hydrological models (GHMs) and 4 global climate models ((link: glossary/global-climate-models text: GCMs)) participating in [ISIMIP](https://www.isimip.org/).\n\
\n\
\n\
### Methodology\n\
We compare the areas affected by and people exposed to {indicator_short} under different levels of global warming (0, 1, 2, and 3 degrees Celsius) or time horizons starting from pre-industrial level in 1850 to present-day (2001-2020), mid of the century  (2041-2060), and end of the century (2081-2100 ) to a scenario without climate change, i.e. pre-industrial climate conditions.\n\
\n\
The area affected by or people exposed to {indicator_short} is restricted to locations and people living in locations where water flows in a river reach (known as discharge and measured in m3/s) are higher than the level reached only once in 100 years on average in hydrological simulations assuming pre-industrial climate conditions (100-year return level).\n\
\n\
The calculation follows a series of steps: First, information about daily temperature and precipitation as well as other weather indicators such as radiation from the global climate simulations is used as input for the hydrological simulations within ISIMIP. The global hydrological models calculate the associated runoff for a global latitude x longitude grid of 0.5° x 0.5° resolution i.e. grid cells of about 50 km x 50 km at the equator. Here, runoff is the difference between the amount of water gained by precipitation and the amount of water lost by evapotranspiration from the surface and vegetation or by entering the ground. It represents the water that can leave the grid cell laterally and feed into a river.\n\
\n\
To calculate where the water actually flows we used the global river model CaMaFlood. It translates the daily runoff into daily discharge which is the amount of water flowing through each grid cell accounting for all neighbouring grid cells. For each grid cell and each year we calculated the annual maximum of the daily discharge values. A grid cell is considered to be affected by flooding if this annual maximum discharge is higher than the 100-year-return level, i.e. the level only reached once within 100 years on average within a several hundreds of years long pre-industrial simulations generated within ISIMIP. Whenever the discharge within a grid cell is higher than this level (e.g. reaches a 200 year return level) we translated the associated return level into the fraction of the grid cell that is actually flooded by looking into a look-up table linking return levels to the fraction of the grid cell that is flooded. This look-up-table has been generated by more detailed and calibrated hydrological simulations by the hydrological model MATSIRO whose discharge levels have been translated into flooded areas by using CaMaFlood to distribute the associated water using high resolution elevation maps (~100 m x 100 m).\n\
\n\
To calculate the total global land area affected by flooding the fractions are added up across all 0.5° x 0.5° grid cells (excluding Antarctica and Greenland). Multiplying, at each grid cell, with the number of people living in the grid cell yields the number of people exposed to {indicator_short}.\n\
\n\
It is important to note that our future projections assume fixed present-day socio-economic conditions including land use patterns or population distributions. They are fixed at reported data for the year 2005. In the key messages we report the results for the median of the ensemble of hydrological models providing data to ISIMIP. The median represents the middle of the ensemble, i.e. 50% of the ensemble members provide higher numbers and 50% provide lower numbers. After the key message only referring to the median you can find all the model-specific results in the Figures and a discussion of the restrictions of the analysis at the end of the article.\n\
\n\
A comparison of the change in land area affected by and {pop_indicator} per country was provided by means of a ranking. Here, countries are ranked on the basis of their relative change in land area affected or population exposed under different levels of global warming and time horizons. A high ranking means here that for the respective country of interest a relative high change in land area affected or population exposed was found in comparison to other countries studied.\n\
\n\
\n\
### Land area affected by {indicator_short}\n\
\n\
#### Key messages\n\
* Under pre-industrial climate conditions {world_land_tc_ov_md_0c}% of the global land area is affected by {indicator_short}.\n\
* According to the simulations the global land area affected by {indicator_short} has increased by a factor of {world_land_tc_rel_ov_md_1c} at today\'s levels of 1°C of global warming.\n\
* At 2°C, the global land area affected by {indicator_short} is projected to increase by a factor {world_land_tc_rel_ov_md_2c} compared to the pre-industrial level in 1850.\n\
* Under the business-as-usual high-emission scenario RCP6.0 scenario this factor is projected to reach {world_land_rcp60_rel_far_future} by the end of the century (2081-2100).\n\
\n\
(line-plot: {land_indicator}-relative-changes_ISIMIP-projections_world)\n\
\n\
\n\
#### Change in land area affected by {indicator_short}\n\
Under present-day conditions (2001-2020), {world_land_pc_abs_today} of the global land area is affected by {indicator_short}. Under a 2°C warming scenario relative to the pre-industrial level in 1850, this fraction is projected to change to {world_land_pc_abs_today}%. Following a low- and high- emission scenario (RCP2.6 and RCP6.0) towards the end of the century (2081-2100), this fraction is projected to change to {world_land_rcp26_far_future}% and {world_land_rcp26_far_future}% of the land area affected by {indicator_short}, respectively.\n\
\n\
At 2°C of global warming the land area affected by {indicator_short} is projected to increase by {world_land_substract_2_and_1}% of the global land area in absolute terms. This means an increase by a factor of {world_land_tc_rel_ov_md_2c} compared to the pre-industrial climate in 1850. Climate change projections towards the end of the century are foreseen to increase the land area affected by {indicator_short} by {world_land_pc_rel_far_future}% of the global land area in absolute terms or a factor of {world_land_pc_rel_far_future} in relative terms compared to the simulations assuming pre-industrial climate in 1850.\n\
\n\
(world-ranking-map: land-area-affected-by-river-flood-relative-changes_ISIMIP-projections)\n\
\n\
(ranking-text: {land_indicator}-relative-changes_ISIMIP-projections_world)\n\
\n\
\n\
### {pop_indicator_capital}\n\
\n\
#### Key messages\n\
* Under pre-industrial climate conditions  {world_pop_tc_ov_md_0c}% of the population is exposed to {indicator_short}.\n\
* According to the simulations the global population exposed to {indicator_short} has increased by a factor of {world_pop_tc_rel_ov_md_1c} at today\'s levels of 1°C of global warming.\n\
* At 2°C the global population exposed to {indicator_short} is projected to increase by a factor of {world_pop_tc_rel_ov_md_2c} compared to the pre-industrial level in 1850.\n\
* Countries facing the largest relative change in {pop_indicator} under 2°C change are: Country1, Country2, Country3, Country4, and Country5.\n\
* Under our business-as-usual high-emission scenario RCP6.0 scenario this factor is projected to reach {world_pop_rcp60_rel_far_future} by the end of the century (2081-2100).\n\
\n\
Countries facing the largest relative change in population exposed to {indicator_short} under the business-as-usual high-emission scenario (RCP6.0) are: Country1, Country2, Country3, Country4, and Country5.\n\
\n\
(line-plot: {pop_indicator}-relative-changes_ISIMIP-projections_world)\n\
\n\
\n\
#### Change in {pop_indicator}\n\
Under present-day conditions (2001-2020), {world_pop_pc_abs_today}% of the global population is exposed to {indicator_short}. Under a 2°C warming scenario relative to the pre-industrial level in 1850, this fraction is projected to change to {world_pop_pc_abs_today}%. Following a low- and high- emission scenario (RCP2.6 and RCP6.0) towards the end of the century (2081-2100), this fraction is projected to change to {world_pop_rcp26_far_future}% and {world_pop_rcp26_far_future}% of the land area affected by {indicator_short}, respectively.\n\
\n\
At 2°C of global warming the population exposed to {indicator_short} is projected to increase by {world_pop_substract_2_and_1}% of the global population in absolute terms. This means an increase by a factor of {world_pop_tc_rel_ov_md_2c} compared to the pre-industrial climate in 1850. Climate change projections towards the end of the century are foreseen to increase the population exposed to {indicator_short} by {world_pop_pc_rel_far_future}% of the global population in absolute terms or a factor of {world_pop_pc_rel_far_future}  in relative terms compared to the simulations assuming pre-industrial climate in 1850.\n\
\n\
\n\
### Discussion\n\
The model simulations are subject to some weaknesses or specific assumptions that have to be kept in mind. They could stem from the provided climate input data, weaknesses in the representation of the hydrological processes or restricted knowledge or representation of other than climate drivers of {indicator_short}.\n\
\n\
Main restriction regarding the climate input data: The global scale climate simulations are known to not provide an adequate representation of convection driven relatively local extreme precipitation events causing flash floods.\n\
\n\
The performance of the hydrological models themselves can be tested by forcing the models by observed historical weather information and compare the calculated discharge to discharge recorded at different stations along rivers. If you select Model evaluation under Assessment type you can generate a report on the performances of the individual models in reproducing observed hydrological conditions given observed historical climate conditions. A general challenge associated with the simulation of hydrological processes is the representation of vegetation cover that affects evapotranspiration and surface properties and may change in a given river basin under rising temperature and CO2 levels affecting CO2 fertilization. For example the effect of CO2 fertilization, i.e. increased plant growth under a more CO2 rich atmosphere,  is not represented in most of the hydrological models although it is important regarding plants\' water use efficiency. However, while it has turned out that these vegetation related processes are critical when it comes to the projection of drought conditions and low flow events, projections of {indicator_short} may be less affected as there is a quite close relationship between precipitation and peak discharge only moderately modulated by evapotranspiration.\n\
\n\
However, the flood projections are expected to be more severely influenced by changes in irrigation, construction of new dams and reservoirs, levees and other flood protection infrastructure that are not explicitly modelled. Instead our methodology assumes that every event where discharge exceeds the local 100-year return level is a flood. In reality, flood protection measures that are in place may have a higher or lower protection standard. Most parts of the world are protected only against more frequent events, which means that more floods would actually occur than in our simulations. In a few parts of the world (mainly the USA and a few European countries) the opposite is true.  As mentioned above, any future changes in human influences on the water cycle are not included in the models. However, even present-day conditions are not represented in detail.\n\
\n\
Another caveat to keep in mind is that a single {indicator_short} model (CaMa-Flood) was used for the calculation of discharge and flooded area. It is therefore difficult to assess the error margin/uncertainty that arises from assumptions built into that model. For GCMs and GHMs, it is known that generally both types of models contribute substantially to the overall spread in projected climate change impacts.""".format(
                   indicator_short=indicator_short,country=country,
                   land_indicator_capital=land_indicator_capital,                
                   world_land_tc_ov_md_0c=world_land_tc_ov_md_0c,world_land_tc_rel_ov_md_1c=world_land_tc_rel_ov_md_1c,world_land_tc_rel_ov_md_2c=world_land_tc_rel_ov_md_2c,
                   world_land_rcp60_rel_far_future=world_land_rcp60_rel_far_future,world_land_pc_abs_today=world_land_pc_abs_today,world_land_substract_2_and_1=world_land_substract_2_and_1,
                   world_land_tc_ov_md_1c=world_land_tc_ov_md_1c,world_land_rcp26_far_future=world_land_rcp26_far_future,world_land_rcp60_far_future=world_land_rcp60_far_future,          
                   world_land_tc_ov_md_2c=world_land_tc_ov_md_2c,land_indicator_raw=land_indicator_raw,
                   world_land_pc_abs_far_future=world_land_pc_abs_far_future,land_indicator=land_indicator,
                   world_land_pc_rel_far_future=world_land_pc_rel_far_future,
                   
                   pop_indicator_capital=pop_indicator_capital,                  
                   world_pop_tc_ov_md_0c=world_pop_tc_ov_md_0c,world_pop_tc_rel_ov_md_1c=world_pop_tc_rel_ov_md_1c,world_pop_tc_rel_ov_md_2c=world_pop_tc_rel_ov_md_2c,
                   world_pop_rcp60_rel_far_future=world_pop_rcp60_rel_far_future,world_pop_pc_abs_today=world_pop_pc_abs_today,world_pop_substract_2_and_1=world_pop_substract_2_and_1,
                   world_pop_tc_ov_md_1c=world_pop_tc_ov_md_1c,world_pop_rcp26_far_future=world_pop_rcp26_far_future,world_pop_rcp60_far_future=world_pop_rcp60_far_future,          
                   world_pop_tc_ov_md_2c=world_pop_tc_ov_md_2c,pop_indicator_raw=pop_indicator_raw,
                   world_pop_pc_abs_far_future=world_pop_pc_abs_far_future,pop_indicator=pop_indicator,
                   world_pop_pc_rel_far_future=world_pop_pc_rel_far_future                   
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
                     country_apostrophe   = data_land_years['region']+'\''
                   else:
                     country_apostrophe   = data_land_years['region']+'\'s'
                     
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
                   land_tc_rel_ov_md_1c_times = round((to_zero(data_land_temperature_change_relative_changes['data']['overall']['median'][2])/100+1),3)
                   if land_tc_rel_ov_md_1c_times < 1:
                      land_tc_rel_ov_md_1c_times_higher_or_lower = 'higher'
                   else:
                      land_tc_rel_ov_md_1c_times_higher_or_lower = 'lower'
                   land_tc_rel_ov_md_2c_times = ((round(to_zero(data_land_temperature_change_relative_changes['data']['overall']['median'][4]),3))/100)+1
                      
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
                   land_rcp60_rel_far_future_times = round((to_zero(data_land_timeslices_relative_changes['data']['rcp60']['overall']['median'][21])/100+1),3)
                   land_rcp26_rel_far_future_times = round((to_zero(data_land_timeslices_relative_changes['data']['rcp26']['overall']['median'][21])/100+1),3)
        
        
                   rank_land_tc_rel_2c        = 'ranking-value: land-area-affected-by-river-flood-relative-changes_ISIMIP-projections_AFG value: position' #Should show ranking with regards to relative change in land area affected under 2 degrees temperature change
        
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
                
                   rank_pop_tc_rel_2c       = 'ranking-value: land-area-affected-by-river-flood-relative-changes_ISIMIP-projections_AFG value: position'# Should show ranking with regards to relative change in population exposed under 2 degrees temperature change
        
                   
                   # Writing the text. 
        
                   if (country_name != 'world'): 
                    text = """This climate impact assessment presents projections of the {land_indicator} and number of people exposed to {indicator_short} in {country}, based on {impact_model_list} different global hydrological models ((link:glossary/global-hydrological-models text: GHMs) and {climate_model_list} different global climate models ((link: glossary/global-climate-models text: GCMs)) participating in [ISIMIP](https://www.isimip.org/).\n\
\n\
Here, {indicator_short} (link: glossary/river-floods)refer to a situation where the daily river flow exceeds the so-called 100 year return level (link: glossary/return-level). For each grid cell (link: glossary/grid-cell) affected to {indicator_short} (link: glossary/river-floods), we calculate the percentage of area flooded by redistributing the total flood volume (link: glossary/flood-volume) per cell in accordance to within grid cell variations in surface elevation (link: glossary/surface-elevation). To calculate the {land_indicator} for {country}, the percentage of area flooded are added up across all grid cells belonging to {country}. To calculate the number of people exposed to {indicator_short}, we first multiply the percentage of area flooded of each grid cell by the number of people living in that grid cell to estimate the number of people exposed to {indicator_short}, and then add up those numbers across all grid cells belonging to {country}.\n\
\n\
We analyze the {land_indicator} and the number of people exposed to {indicator_short} at different levels of global warming (0, 1, 2, and 3 degrees Celsius) and during different time periods. We cover the time before anthropogenic climate change started (1850), present-day (2001-2020), mid-century (2041-2060) and end-of-century (2081-2100). We compare the later periods against the climate conditions before climate change started (1850). A ranking of countries for each indicator is provided to allow comparison between countries on the basis of their relative change in land area affected or number of people exposed under different levels of global warming and for various time horizons, compared to conditions before anthropogenic climate change started. Here, a ranking of 1 implies that the country experiences a change in the indicator that is higher than all other ranked countries, whereas a lower ranking entails comparatively less impacts due to climate change.\n\
\n\
It is important to note that our future projections assume that the number of people living in an area, as well as the area\'s land use (link: glossary/land-use) and land cover (link: glossary/land-cover), remain constant at the levels of year 2005. This is not meant to be realistic, but to isolate the influence of climate change from the influence of other changes.\n\
\n\
In the key messages we report the results for the median of the ensemble of global hydrological models providing data to ISIMIP. The median represents the middle of the ensemble, i.e. 50% of the ensemble members provide higher numbers and 50% provide lower numbers. After the key message only referring to the median you can find the model-specific results in the figures and a discussion of the methodology and the restrictions of the analysis at the end of the article.\n\
\n\
### Key messages\n\
* Without human-made greenhouse gas emissions, {land_tc_ov_md_0c}% of {country}'s land area and {pop_tc_ov_md_0c}% of {country_apostrophe} population would be affected by {indicator_short} each year, on average.\n\
* At today\'s levels of 1°C of global warming the land area affected is {land_tc_rel_ov_md_1c_times} times as much: {land_tc_rel_ov_md_1c}% of the total land area, while the number of people affected is {pop_tc_rel_ov_md_1c_times} times as much: {pop_tc_ov_md_1c}% of the total population.\n\
* At 2°C of global warming, {country_apostrophe} {land_indicator} is projected to increase by a factor of {land_tc_rel_ov_md_2c} compared to a world without human-made greenhouse gas emissions, to {land_tc_ov_md_0c}%. Likewise, {country_apostrophe} {pop_indicator} is projected to increase by a factor {pop_tc_rel_ov_md_2c}, to {pop_tc_ov_md_0c}%.\n\
* Following the business-as-usual emissions scenario (RCP6.0) up to over 4 degrees Celsius of global warming by the end of the century (2081-2100), this factor is projected to reach {land_rcp60_far_future_times} for the land area affected to {indicator_short} (to {land_rcp60_far_future_times}%) and {pop_rcp60_far_future_times} for the {pop_rcp60_far_future}.\n\
* {country} ranks (rank_land_tc_rel_2c) with regards to its relative change in {land_indicator} at 2°C of global warming in comparison to a situation without anthropogenic climate change. For the relative change in {pop_indicator}, {country_apostrophe} ranking is (rank_pop_tc_rel_2c).\n\
\n\
### Results\n\
\n\
#### {land_indicator_capital}\n\
The figure below shows the relative change in {country_apostrophe} {land_indicator} in comparison to the time period before anthropogenic climate change started. Results are shown both for the historical period and for the future projections and can be visualized with regards to their change over time as well as with regards to their change in terms of global warming. Under the “change in terms of time” setting, the change in {land_indicator} through time is shown for 20-year time-slices from 1861-1880 until the end-of-the-century (2081-2100). Under the “change in terms of global warming”, the change in {land_indicator} is shown for 20-year time-slices representing increasing levels of global warming from 0 degrees Celsius up to 3 degrees Celsius compared to the time period before anthropogenic climate change started. In both cases, results are shown for all possible combinations of global hydrological model and global climate model (normal lines) as well as for the median of the ensemble (thick line). The influence of inter-annual variability on the results is visualized by means of the shaded area in black. This inter-annual variability is only shown for the median model combination. For the future projections and under the “change in terms of time” settings only, an additional distinction is made between the results of two emissions trajectories: RCP2.6 (blue lines) RCP6.0 (red lines). The shaded areas in blue and red indicate the variety in results for individual combinations of global hydrological model and global climate model for these two emissions trajectories. A filtering menu top-right of the graph allows the user to select individual emissions trajectories, individual global climate models, and individual global hydrological models for visualization.\n\
\n\
By hovering over or clicking on a particular value in the figure additional details behind the presented value become available. The visualization below the graph shows, moreover, for the selected model run under this time-period or temperature-change level how {country} ranks in comparison to other countries on its relative change in {land_indicator}.\n\
\n\
(line-plot: land-area-affected-by-river-flood-relative-changes_ISIMIP-projections_world)\n\
\n\
Without human-made greenhouse gas emissions, {land_tc_ov_md_0c}% of {country_apostrophe} land area would be affected by {indicator_short} each year, on average. Under the “change in terms of global warming” setting the figure shows that at today\'s level of 1°C of global warming {country_apostrophe} {land_indicator} is, on average, already {land_tc_rel_ov_md_1c_times} times {land_tc_rel_ov_md_1c_times_higher_or_lower} (or {land_tc_rel_ov_md_1c}%): {land_tc_ov_md_1c}% of the total land area. This level of change ranges from {minimum_land_tc_abs_ov_md_1c}% to {maximum_land_tc_abs_ov_md_1c}%  for the individual combinations of global hydrological models and global climate models. At 2°C of global warming, {country_apostrophe} {land_indicator} is projected to change by a factor of {land_tc_rel_ov_md_2c_times} (or {land_tc_abs_ov_md_2c}%) in comparison to a world without human-made greenhouse gas emissions. Under these conditions, {land_tc_ov_md_2c}% of the total land area would be affected by {indicator_short} on a yearly basis, on average. Across the individual combinations of global hydrological models and global climate models this expected level of change ranges from {minimum_land_tc_abs_ov_md_2c}% up to {maximum_land_tc_abs_ov_md_2c}%.\n\
\n\
When presenting the “change in terms of time”, we find that when following the business-as-usual emissions scenario (RCP6.0) towards the end-of-the-century (equivalent to up to over 4 degrees Celsius change) would result in a foreseen change in the {land_indicator} of, on average, a factor {land_rcp60_rel_far_future_times} ({land_rcp60_abs_far_future}%), towards: {land_rcp60_far_future}% of the total land area. Following the climate-mitigation emissions scenario (RCP2.6) towards the end-of-the-century (equivalent to on average 2.5 degrees Celsius change) would result in a foreseen change in the {land_indicator} of, on average, a factor {land_rcp26_rel_far_future_times} ({land_rcp26_abs_far_future}%), towards: {land_rcp26_far_future}% of the total land area.\n\
\n\
Globally, the {land_indicator} by each year, on average, is {world_land_tc_ov_md_0c}% in a situation without human-made greenhouse gas emissions. At 2 degrees Celsius global warming or by the end-of-the-century under a business-as-usual emissions scenario (RCP6.0) these values are foreseen to increase globally by {world_land_tc_rel_ov_md_2c_times}% and {world_land_rcp60_rel_far_future_times}% respectively. As such, {country} ranks {world_rank_land_tc_rel_2c} with regards to its relative change in {land_indicator} at 2°C of global warming in comparison to a situation without anthropogenic climate change. This indicates comparatively {world_rank_land_tc_rel_2c_high_or_low} impacts due to climate change in comparison to other countries. For the relative change in {land_indicator} towards the-end-of-the-century under a business-as-usual emissions scenario, {country_apostrophe} ranking is {world_rank_land_rcp60_rel_far_future}. This indicates comparatively {world_rank_land_rcp60_rel_far_future_high_or_low} impacts due to climate change in comparison to other countries.\n\
\n\
#### {pop_indicator_capital}\n\
The figure below shows the relative change in {country_apostrophe} {pop_indicator} in comparison to the time period before anthropogenic climate change started. Results are shown both for the historical period and for the future projections and can be visualized with regards to their change over time as well as with regards to their change in terms of global warming. Under the “change in terms of time” setting, the change in {pop_indicator} through time is shown for 20-year time-slices from 1861-1880 until the end-of-the-century (2081-2100). Under the “change in terms of global warming”, the change in {pop_indicator} is shown for 20-year time-slices representing increasing levels of global warming from 0 degrees Celsius up to 3 degrees Celsius compared to the time period before anthropogenic climate change started. In both cases, results are shown for all possible combinations of global hydrological model and global climate model (normal lines) as well as for the median of the ensemble (thick line). The influence of inter-annual variability on the results is visualized by means of the shaded area in black. This inter-annual variability is only shown for the median model combination. For the future projections and under the “change in terms of time” settings only, an additional distinction is made between the results of two emissions trajectories: RCP2.6 (blue lines) RCP6.0 (red lines). The shaded areas in blue and red indicate the variety in results for individual combinations of global hydrological model and global climate model for these two emissions trajectories. A filtering menu top-right of the graph allows the user to select individual emissions trajectories, individual global climate models, and individual global hydrological models for visualization.\n\
\n\
By hovering over or clicking on a particular value in the figure additional details behind the presented value become available. The visualization below the graph shows, moreover, for the selected model run under this time-period or temperature-change level how {country} ranks in comparison to other countries on its relative change in {pop_indicator}.\n\
\n\
(line-plot: population-exposed-to-river-flood-relative-changes_ISIMIP-projections_world)\n\
\n\
Without human-made greenhouse gas emissions, {pop_tc_ov_md_0c}% of {country_apostrophe} population would be exposed to {indicator_short} each year, on average. Under the “change in terms of global warming” setting the figure shows that at today\'s level of 1°C of global warming {country_apostrophe} {pop_indicator} is, on average, already {pop_tc_rel_ov_md_1c_times} times {pop_tc_rel_ov_md_1c_times_higher_or_lower} (or {pop_tc_rel_ov_md_1c}%): {pop_tc_ov_md_1c}% of the total land area. This level of change ranges from {minimum_pop_tc_abs_ov_md_1c} to {maximum_pop_tc_abs_ov_md_1c} for the individual combinations of global hydrological models and global climate models. At 2°C of global warming, {country_apostrophe} {pop_indicator} is projected to change by a factor of {pop_tc_rel_ov_md_2c_times} (or {pop_tc_abs_ov_md_2c}%) in comparison to a world without human-made greenhouse gas emissions. Under these conditions, {pop_tc_ov_md_2c}% of the total population would be exposed to {indicator_short} on a yearly basis, on average. Across the individual combinations of global hydrological models and global climate models this expected level of change ranges from {minimum_pop_tc_abs_ov_md_2c}% up to {maximum_pop_tc_abs_ov_md_2c}%.\n\
\n\
When presenting the “change in terms of time”, we find that when following the business-as-usual emissions scenario (RCP6.0) towards the end-of-the-century (equivalent to up to over 4 degrees Celsius change) would result in a foreseen change in the {pop_indicator} of, on average, a factor {pop_rcp60_rel_far_future_times} ({pop_rcp60_abs_far_future}%), towards: {pop_rcp60_far_future}% of the total population. Following the climate-mitigation emissions scenario (RCP2.6) towards the end-of-the-century (equivalent to on average 2.5 degrees Celsius change) would result in a foreseen change in the {pop_indicator} of, on average, a factor {pop_rcp26_rel_far_future_times} ({pop_rcp26_abs_far_future}%), towards: {pop_rcp26_far_future}% of the total population.\n\
\n\
Globally, the {pop_indicator} each year, on average, is {world_pop_tc_ov_md_0c}% in a situation without human-made greenhouse gas emissions. At 2 degrees Celsius of global warming or by the end-of-the-century under a business-as-usual emissions scenario (RCP6.0) these values are foreseen to increase globally by {world_pop_tc_rel_ov_md_2c_times}% and {world_pop_rcp60_rel_far_future_times}% respectively. As such, {country} ranks {world_rank_pop_tc_rel_2c} with regards to its relative change in {pop_indicator} at 2°C of global warming in comparison to a situation without anthropogenic climate change. This indicates comparatively {world_rank_pop_tc_rel_2c_high_or_low} impacts due to climate change in comparison to other countries. For the relative change in {pop_indicator} towards the-end-of-the-century under a business-as-usual emissions scenario, {country_apostrophe} ranking is {world_rank_pop_rcp60_rel_far_future}. This indicates comparatively {world_rank_pop_rcp60_rel_far_future_high_or_low} impacts due to climate change in comparison to other countries.\n\
\n\
### Methodology\n\
\n\
#### What do we analyze?\n\
We analyze the {land_indicator} and the number of people exposed to {indicator_short} at different levels of global warming (0, 1, 2, and 3 degrees Celsius) and during different time periods. We cover the time before anthropogenic climate change started (1850), present-day (2001-2020), mid-century (2041-2060) and end-of-century (2081-2100). We compare the later periods against the climate conditions before climate change started (1850).\n\
\n\
#### How do we calculate where and when a flood occurs?\n\
The calculation has several steps: 1) calculate runoff; 2) calculate daily river flow and its annual maximum; 3) compare this annual maximum with the 100 year return level, which is calculated separately; when the 100 year return level is exceeded, 4) calculate flood depth; and 5) calculate flooded land area fraction. All these steps will be explained below, after a short explanation of the spatial structure on which our models operate.\n\
\n\
#### What is the spatial structure of the models?\n\
The models we use cover the whole globe\'s land area. They divide the land area into rectangles (also called grid cells). These rectangles have a size of 0.5° × 0.5° (latitude by longitude). At the equator, this equals roughly 55 × 55 km; towards the North Pole or South Pole, the land area covered per grid cell becomes smaller.\n\
\n\
#### How is runoff calculated?\n\
The calculation is done for each grid cell and each day. Information about temperature, precipitation, solar radiation, and other weather indicators is taken from the global climate models (GCMs) and used as input for the ISI-MIP global hydrological models (GHMs). Additional spatial input data include soil, land cover and water bodies. The water models then calculate runoff. Runoff is the difference between the amount of water coming in as rain or snow, and the amount of water going out either through evapotranspiration from the surface and vegetation, or by seeping vertically into the ground. Runoff percolates horizontally through the ground (subsurface runoff) or flows on the surface (surface runoff) into the surface water bodies or river.\n\
\n\
#### How is river flow calculated?\n\
Having calculated runoff in each grid cell, we use the global river model CaMaFlood to calculate the water flow once it is in the river. The river water flow is also known as discharge, and measured in cubic meters per second (m³/s). For each grid cell along the river, the amount of water flowing through the river is calculated by summing up the runoff coming from all grid cells located upstream. For each grid cell and each year we then calculate the annual maximum of the daily river flow values.\n\
\n\
#### How do we know whether a flood occurs?\n\
In our analysis, we assume that a flood occurs whenever the annual maximum daily river flow exceeds the so-called 100 year return level. This is the water flow that was exceeded only once every 100 years, on average, before anthropogenic climate change started. We only consider river flows larger than the 100 year return level because we assume that for smaller flows, either no flooding occurs (e.g. protection measures such as levees prevent them) or the floods have minor impacts (e.g. people do not settle in these areas or the flood depth is very shallow). That is, we assume that societies have already adapted to more frequent events.\n\
\n\
#### How do we know how often floods occurred before anthropogenic climate change started?\n\
We use a separate model simulation in which the climate behaves as if there had been no human-made greenhouse gas emissions. This simulation runs for several centuries without any outside change, just letting the weather evolve naturally. We then calculate the maximum river flow level that occurs, on average, every 100 years in this simulation.\n\
\n\
#### How is flood depth calculated?\n\
Once there is a flood in a given grid cell and year, we obtain the flood depth from a unique relationship between return level and flood depth that is calculated beforehand for each grid cell. This relationship between return level and flood depth is based on calibrated simulations from the global water model MATSIRO in combination with CaMaFlood.\n\
\n\
#### How is the flooded land area fraction calculated?\n\
For each affected grid cell, the flood water volume is calculated from the flood depth and the size of the cell. This volume of water is then distributed onto a high-resolution map of surface elevation. This map is part of the CaMaFlood model. It has a resolution of about ~100m x 100m at the equator, and indicates for every point its elevation above sea level. All points within the 0.5° x 0.5° grid cell get filled with water according to their relative elevation. Then, the portion of the 0.5° x 0.5° grid cell that is submerged is calculated. For example, if it is a mountainous area, all the flood water will concentrate in the narrow valleys, while the mountain peaks do not get flooded. Thus, only a part of the 0.5° x 0.5° grid cell will be submerged even during a large flood. On the contrary, if the area is very flat, then the flood water will spread out and potentially submerge the entire grid cell.\n\
\n\
#### How are the indicators {land_indicator} and number of people exposed to {indicator_short} calculated?\n\
To calculate the land area affected by flooding for {country}, the flooded land area fractions are added up across all 0.5° x 0.5° grid cells belonging to {country}. To calculate the number of people exposed to flooding, we first multiply the flooded land area fraction of each grid cell by the number of people living in that grid cell to estimate the number of people exposed to {indicator_short}, and then add up those numbers across all grid cells belonging to {country}.\n\
\n\
#### What else should I know about the methodology?\n\
We assume that the number of people living in an area, as well as the area\'s land use and land cover (what fractions of the area are used for settlement, cropland, or pasture, or covered by forest), remain constant at the levels of year 2005 throughout the whole simulation. This is not meant to be realistic, but to isolate the influence of climate change from the influence of other changes.\n\
\n\
In the key messages we report the results for the median (the model in the middle) of the group of global water models that ran simulations in ISIMIP2b. All model-specific results are presented in the figures and a discussion of the limitations of the analysis is included at the end of the report.\n\
\n\
A ranking of countries for each indicator is also provided to compare countries on the basis of their relative change in land area affected or number of people exposed under different levels of global warming and for various time horizons, compared to conditions without climate change. A ranking of 1 implies that the country experiences a change in the indicator higher than all other ranked countries, i.e., the strongest impacts from climate change; whereas a lower ranking entails comparatively less impacts.\n\
\n\
### Discussion\n\
The model simulations used for this report build on science that has been established through many peer-reviewed studies: e.g. by [Yamazaki et al. (2011)]( https://doi.org/10.1029/2010WR009726),[Müller Schmied et al. (2016)](https://doi.org/10.5194/hess-20-2877-2016). Models are simplified representations of reality, hence model simulations come with limitations and uncertainties that have to be kept in mind. One major limitation of the global water models is the availability of available global data sets that are needed to fully represent the global hydrological cycle. For example, many of the models do not consider glaciers which could influence {indicator_short} as well. Furthermore, the representation of the components of the hydrological cycle, such as soil hydrology, differ strongly between models (e.g. in terms of detail and depth but also the calculation approach) with large effects on runoff generation. Another major source of uncertainty are the climatic input data as they stem from climate models that have a coarser spatial resolution and modelling uncertainties by themselves. In particular, the adequate simulation of precipitation extremes is difficult for global climate models.\n\
\n\
The performance of the global water models themselves can be tested by using observed historical weather information as inputs, and comparing the simulated river flow to river flow observed at different stations along rivers. One general challenge associated with the simulation of hydrological processes lies in the representation of how vegetation cover affects evapotranspiration and other surface properties that play a role in flood onset. Moreover, this relationship may change within a given river basin, or with rising temperature and CO2 levels. For example, the effect of CO2 fertilization – the phenomenon through which photosynthesis, hence plant growth, should be enhanced in a CO2-richer atmosphere – is not represented in most water models although it would affect the plants’ water use, with consequences for runoff and river flow. These vegetation-related processes are critical for the projection of drought conditions and low-flow events, but are of less importance for projections of {indicator_short}. A close relationship exists between precipitation and peak discharge during flood events, which is only moderately affected by evapotranspiration.\n\
\n\
The presented flood projections reflect the isolated effect of climate change, while their local manifestations are expected to also be influenced by direct human drivers like changes in irrigation, construction of new dams and reservoirs, levees and other flood protection infrastructure. The representation of these drivers is limited to present-day conditions, while their future changes are not explicitly modelled in the presented simulations. This serves the purpose of isolating the effect of climate human-made change from other factors, but it means that actual flood exposure in the future is simulated less realistically than in simulations that would include these other factors, and hence represent adaptation to climate change.\n\
\n\
Our methodology assumes that every event where river flow exceeds the local 100 year return level is a flood. This is a simplification; flood protection measures may have a higher or lower protection standard in reality. Most parts of the world are protected only against lower-intensity events that occur more frequently than once in a hundred years. This means that more floods would actually occur than in our projections. In a few parts of the world (mainly the USA and a few European countries), the opposite is true, meaning that protection measures could prevent all river flow events that are simulated to occur up to as rarely as once in 200 years (for example) from materialising into a flood.\n\
\n\
Finally, another caveat to keep in mind is that only a single {indicator_short} model (CaMaFlood) was used for the calculation of river flow and flooded area; and a single water model, MATSIRO, was used to derive the grid cell-specific relationship between return level and flood depth. It is therefore difficult to assess the uncertainty that arises from assumptions built into these models.\n\
\n\
Regarding climate models and water models, it is known that generally both types of models contribute substantially to the overall spread in projected climate change impacts on river flow and other water-related variables. Because this report presents the results of a combination of climate models and water models that ran simulations based on the same experiment protocol, and whose outputs are thus directly comparable, it captures at least some of this spread in the projections.\n\
\n\
For more information, please consult the detailed report on the performance of the global hydrological models at simulating {indicator_short}, available from the “Create Report” page.""".format(
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

    
