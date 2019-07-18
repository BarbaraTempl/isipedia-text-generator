#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 10:26:35 2019

@author: julian
"""



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
     
#input_foulder = '/home/julian/ISIPedia_DKRZ_Server/data_cube/'
#output_foulder = '/home/julian/ISIPedia_DKRZ_Server/data_cube/'

input_foulder = '/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/data_cube/'
output_foulder = '/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/data_cube/'

# Get the folder names, i.e the indicator names. 
indicator_names= os.listdir (input_foulder)

for indicator_name in indicator_names:
 if(indicator_name=='river-flood'):
    countries_rank = pd.read_excel('/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/Github/ISIPedia/Countries Names.xls')# Creating a rank for [‘overall‘][‘median_relative_changes’][6]
    country_names= os.listdir (input_foulder+indicator_name+'/ISIMIP-projections')

    land_json = {}
    pop_json = {}


    land_json['rank'] = {}          
    pop_json['rank'] = {}   
    
    land_json['variable'] = {}
    pop_json['variable'] = {}
    land_json['climate_model_list'] = {}
    pop_json['climate_model_list'] = {}
    land_json['impact_model_list'] = {}
    pop_json['impact_model_list'] = {}
    land_json['climate_scenario_list'] = {}
    pop_json['climate_scenario_list'] = {}
    land_json['temperature_list'] = {}
    pop_json['temperature_list'] = {}         
    land_json['timeslices_list'] = {}
    pop_json['timeslices_list'] = {}    
    
    land_json['rank']['temperature_list']= {}
    land_json['rank']['temperature_list']['_']= {}
    land_json['rank']['temperature_list']['absolute']= {}
    land_json['rank']['temperature_list']['relative']= {}   
    pop_json['rank']['temperature_list']= {}
    pop_json['rank']['temperature_list']['_']= {}
    pop_json['rank']['temperature_list']['absolute']= {}
    pop_json['rank']['temperature_list']['relative']= {}  
    land_json['rank']['timeslices_list']= {}
    land_json['rank']['timeslices_list']['_']= {}
    land_json['rank']['timeslices_list']['absolute']= {}
    land_json['rank']['timeslices_list']['relative']= {}   
    pop_json['rank']['timeslices_list']= {}
    pop_json['rank']['timeslices_list']['_']= {}
    pop_json['rank']['timeslices_list']['absolute']= {}
    pop_json['rank']['timeslices_list']['relative']= {}  
    #land_json['rank']['year_list']= {}
    #land_json['rank']['year_list']['_']= {}
    #land_json['rank']['year_list']['absolute']= {}
    #land_json['rank']['year_list']['relative']= {}   
    #pop_json['rank']['year_list']= {}
    #pop_json['rank']['year_list']['_']= {}
    #pop_json['rank']['year_list']['absolute']= {}
    #pop_json['rank']['year_list']['relative']= {}  

    land_json['rank']['temperature_list']['_']['overall'] = {}
    pop_json['rank']['temperature_list']['_']['overall'] = {}
    land_json['rank']['temperature_list']['absolute']['overall'] = {}
    pop_json['rank']['temperature_list']['absolute']['overall'] = {}
    land_json['rank']['temperature_list']['relative']['overall'] = {}
    pop_json['rank']['temperature_list']['relative']['overall'] = {}
    land_json['rank']['timeslices_list']['_']['piControl'] = {}
    land_json['rank']['timeslices_list']['_']['piControl']['overall'] = {}
    pop_json['rank']['timeslices_list']['_']['piControl'] = {}
    pop_json['rank']['timeslices_list']['_']['piControl']['overall'] = {}
    land_json['rank']['timeslices_list']['absolute']['piControl'] = {}
    land_json['rank']['timeslices_list']['absolute']['piControl']['overall'] = {}
    pop_json['rank']['timeslices_list']['absolute']['piControl'] = {}
    pop_json['rank']['timeslices_list']['absolute']['piControl']['overall'] = {}
    land_json['rank']['timeslices_list']['relative']['piControl'] = {}            
    land_json['rank']['timeslices_list']['relative']['piControl']['overall'] = {}
    pop_json['rank']['timeslices_list']['relative']['piControl'] = {}
    pop_json['rank']['timeslices_list']['relative']['piControl']['overall'] = {}

    land_json['rank']['timeslices_list']['_']['historical'] = {}
    land_json['rank']['timeslices_list']['_']['historical']['overall'] = {}
    pop_json['rank']['timeslices_list']['_']['historical'] = {}
    pop_json['rank']['timeslices_list']['_']['historical']['overall'] = {}
    land_json['rank']['timeslices_list']['absolute']['historical'] = {}
    land_json['rank']['timeslices_list']['absolute']['historical']['overall'] = {}
    pop_json['rank']['timeslices_list']['absolute']['historical'] = {}
    pop_json['rank']['timeslices_list']['absolute']['historical']['overall'] = {}
    land_json['rank']['timeslices_list']['relative']['historical'] = {}            
    land_json['rank']['timeslices_list']['relative']['historical']['overall'] = {}
    pop_json['rank']['timeslices_list']['relative']['historical'] = {}
    pop_json['rank']['timeslices_list']['relative']['historical']['overall'] = {}

    land_json['rank']['timeslices_list']['_']['rcp26'] = {}
    land_json['rank']['timeslices_list']['_']['rcp26']['overall'] = {}
    pop_json['rank']['timeslices_list']['_']['rcp26'] = {}
    pop_json['rank']['timeslices_list']['_']['rcp26']['overall'] = {}
    land_json['rank']['timeslices_list']['absolute']['rcp26'] = {}
    land_json['rank']['timeslices_list']['absolute']['rcp26']['overall'] = {}
    pop_json['rank']['timeslices_list']['absolute']['rcp26'] = {}
    pop_json['rank']['timeslices_list']['absolute']['rcp26']['overall'] = {}
    land_json['rank']['timeslices_list']['relative']['rcp26'] = {}            
    land_json['rank']['timeslices_list']['relative']['rcp26']['overall'] = {}
    pop_json['rank']['timeslices_list']['relative']['rcp26'] = {}
    pop_json['rank']['timeslices_list']['relative']['rcp26']['overall'] = {}

    land_json['rank']['timeslices_list']['_']['rcp60'] = {}
    land_json['rank']['timeslices_list']['_']['rcp60']['overall'] = {}
    pop_json['rank']['timeslices_list']['_']['rcp60'] = {}
    pop_json['rank']['timeslices_list']['_']['rcp60']['overall'] = {}
    land_json['rank']['timeslices_list']['absolute']['rcp60'] = {}
    land_json['rank']['timeslices_list']['absolute']['rcp60']['overall'] = {}
    pop_json['rank']['timeslices_list']['absolute']['rcp60'] = {}
    pop_json['rank']['timeslices_list']['absolute']['rcp60']['overall'] = {}
    land_json['rank']['timeslices_list']['relative']['rcp60'] = {}            
    land_json['rank']['timeslices_list']['relative']['rcp60']['overall'] = {}
    pop_json['rank']['timeslices_list']['relative']['rcp60'] = {}
    pop_json['rank']['timeslices_list']['relative']['rcp60']['overall'] = {}
 
    
    # Create a list of values for then to create the rank.
    country_names= os.listdir (input_foulder+indicator_name+'/ISIMIP-projections')
    for country_name in country_names:
      if(country_name != 'world'):
        if(country_name != 'oceans'):
           print(indicator_name+ " - " +country_name)  
                     
           
           # Land affected by INDICATOR
           json_land_temperature_change_absolute_changes = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/land-area-affected-by-'+indicator_name+'-absolute-changes_ISIMIP-projections_versus-temperature-change_'+country_name+'.json'
           json_land_timeslices_absolute_changes = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/land-area-affected-by-'+indicator_name+'-absolute-changes_ISIMIP-projections_versus-timeslices_'+country_name+'.json' 
           json_land_years_absolute_changes = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/land-area-affected-by-'+indicator_name+'-absolute-changes_ISIMIP-projections_versus-years_'+country_name+'.json'

           json_land_temperature_change = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/land-area-affected-by-'+indicator_name+'_ISIMIP-projections_versus-temperature-change_'+country_name+'.json'
           json_land_timeslices = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/land-area-affected-by-'+indicator_name+'_ISIMIP-projections_versus-timeslices_'+country_name+'.json' 
           json_land_years = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/land-area-affected-by-'+indicator_name+'_ISIMIP-projections_versus-years_'+country_name+'.json'

           json_land_temperature_change_relative_changes = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/land-area-affected-by-'+indicator_name+'-relative-changes_ISIMIP-projections_versus-temperature-change_'+country_name+'.json'
           json_land_timeslices_relative_changes = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/land-area-affected-by-'+indicator_name+'-relative-changes_ISIMIP-projections_versus-timeslices_'+country_name+'.json' 
           json_land_years_relative_changes = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/land-area-affected-by-'+indicator_name+'-relative-changes_ISIMIP-projections_versus-years_'+country_name+'.json'

           # Population exposed to INDICATOR
           json_pop_temperature_change_absolute_changes = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/population-exposed-to-'+indicator_name+'-absolute-changes_ISIMIP-projections_versus-temperature-change_'+country_name+'.json'
           json_pop_timeslices_absolute_changes = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/population-exposed-to-'+indicator_name+'-absolute-changes_ISIMIP-projections_versus-timeslices_'+country_name+'.json' 
           json_pop_years_absolute_changes = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/population-exposed-to-'+indicator_name+'-absolute-changes_ISIMIP-projections_versus-years_'+country_name+'.json'

           json_pop_temperature_change = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/population-exposed-to-'+indicator_name+'_ISIMIP-projections_versus-temperature-change_'+country_name+'.json'
           json_pop_timeslices = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/population-exposed-to-'+indicator_name+'_ISIMIP-projections_versus-timeslices_'+country_name+'.json' 
           json_pop_years = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/population-exposed-to-'+indicator_name+'_ISIMIP-projections_versus-years_'+country_name+'.json'

           json_pop_temperature_change_relative_changes = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/population-exposed-to-'+indicator_name+'-relative-changes_ISIMIP-projections_versus-temperature-change_'+country_name+'.json'
           json_pop_timeslices_relative_changes = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/population-exposed-to-'+indicator_name+'-relative-changes_ISIMIP-projections_versus-timeslices_'+country_name+'.json' 
           json_pop_years_relative_changes = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/population-exposed-to-'+indicator_name+'-relative-changes_ISIMIP-projections_versus-years_'+country_name+'.json'
               
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

           land_json['variable'] = data_land_timeslices['variable']
           pop_json['variable'] = data_pop_timeslices['variable']
           land_json['climate_model_list'] = data_land_timeslices['climate_model_list']
           pop_json['climate_model_list'] = data_pop_timeslices['climate_model_list']
           land_json['impact_model_list'] = data_land_timeslices['impact_model_list']
           pop_json['impact_model_list'] = data_pop_timeslices['impact_model_list']
           land_json['climate_scenario_list'] = data_land_timeslices['climate_scenario_list']
           pop_json['climate_scenario_list'] = data_pop_timeslices['climate_scenario_list']
           land_json['temperature_list'] = data_land_temperature_change['temperature_list']
           pop_json['temperature_list'] = data_pop_temperature_change['temperature_list']         
           land_json['timeslices_list'] = data_land_timeslices['timeslices_list']
           pop_json['timeslices_list'] = data_pop_timeslices['timeslices_list']
           #land_json['years_list'] = data_land_years['year_list']
           #pop_json['years_list'] = data_pop_years['year_list']

           land_json['rank']['temperature_list']['_']['overall'][country_name]= {} 
           pop_json['rank']['temperature_list']['_']['overall'][country_name] = {}            
           land_json['rank']['temperature_list']['absolute']['overall'][country_name]= {}              
           pop_json['rank']['temperature_list']['absolute']['overall'][country_name]= {}  
           land_json['rank']['temperature_list']['relative']['overall'][country_name]= {}  
           pop_json['rank']['temperature_list']['relative']['overall'][country_name]= {}   
           land_json['rank']['timeslices_list']['_']['piControl']['overall'][country_name]= {}   
           pop_json['rank']['timeslices_list']['_']['piControl']['overall'][country_name]= {}   
           land_json['rank']['timeslices_list']['absolute']['piControl']['overall'][country_name]= {}             
           pop_json['rank']['timeslices_list']['absolute']['piControl']['overall'][country_name]= {}   
           land_json['rank']['timeslices_list']['relative']['piControl']['overall'][country_name]= {}               
           pop_json['rank']['timeslices_list']['relative']['piControl']['overall'][country_name]= {}               

           land_json['rank']['timeslices_list']['_']['historical']['overall'][country_name]= {}   
           pop_json['rank']['timeslices_list']['_']['historical']['overall'][country_name]= {}   
           land_json['rank']['timeslices_list']['absolute']['historical']['overall'][country_name]= {}             
           pop_json['rank']['timeslices_list']['absolute']['historical']['overall'][country_name]= {}   
           land_json['rank']['timeslices_list']['relative']['historical']['overall'][country_name]= {}               
           pop_json['rank']['timeslices_list']['relative']['historical']['overall'][country_name]= {}               

           land_json['rank']['timeslices_list']['_']['rcp26']['overall'][country_name]= {}   
           pop_json['rank']['timeslices_list']['_']['rcp26']['overall'][country_name]= {}   
           land_json['rank']['timeslices_list']['absolute']['rcp26']['overall'][country_name]= {}             
           pop_json['rank']['timeslices_list']['absolute']['rcp26']['overall'][country_name]= {}   
           land_json['rank']['timeslices_list']['relative']['rcp26']['overall'][country_name]= {}               
           pop_json['rank']['timeslices_list']['relative']['rcp26']['overall'][country_name]= {}               

           land_json['rank']['timeslices_list']['_']['rcp60']['overall'][country_name]= {}   
           pop_json['rank']['timeslices_list']['_']['rcp60']['overall'][country_name]= {}   
           land_json['rank']['timeslices_list']['absolute']['rcp60']['overall'][country_name]= {}             
           pop_json['rank']['timeslices_list']['absolute']['rcp60']['overall'][country_name]= {}   
           land_json['rank']['timeslices_list']['relative']['rcp60']['overall'][country_name]= {}               
           pop_json['rank']['timeslices_list']['relative']['rcp60']['overall'][country_name]= {}   
           
           c=0
           while c < len(data_land_temperature_change['temperature_list']):
            land_json['rank']['temperature_list']['_']['overall'][country_name][data_land_temperature_change['temperature_list'][c]] = {}
            c=c+1
           c=0
  
           while c < len(data_pop_temperature_change['temperature_list']):
            pop_json['rank']['temperature_list']['_']['overall'][country_name][data_land_temperature_change['temperature_list'][c]]= {} 
            c=c+1 
           c=0

           while c < len(data_land_temperature_change_absolute_changes['temperature_list']):
            land_json['rank']['temperature_list']['absolute']['overall'][country_name][data_land_temperature_change['temperature_list'][c]]= {} 
            c=c+1
           c=0
 
           while c < len(data_pop_temperature_change_absolute_changes['temperature_list']):
            pop_json['rank']['temperature_list']['absolute']['overall'][country_name][data_pop_temperature_change['temperature_list'][c]]= {}  
            c=c+1
           c=0

           while c < len(data_land_temperature_change_relative_changes['temperature_list']): 
            land_json['rank']['temperature_list']['relative']['overall'][country_name][data_land_temperature_change['temperature_list'][c]]= {}                
            c=c+1
           c=0

           while c < len(data_pop_temperature_change_relative_changes['temperature_list']):
            pop_json['rank']['temperature_list']['relative']['overall'][country_name][data_pop_temperature_change['temperature_list'][c]]= {}   
            c=c+1
           cc=0
           while cc < len(data_land_timeslices['climate_scenario_list']):  
            c=0

            while c < len(data_land_timeslices['timeslices_list']):           
             land_json['rank']['timeslices_list']['_'][data_land_timeslices['climate_scenario_list'][cc]]['overall'][country_name][str(data_land_timeslices['timeslices_list'][c])]= {} 
             c=c+1
            c=0

            while c < len(data_pop_timeslices['timeslices_list']):           
             pop_json['rank']['timeslices_list']['_'][data_pop_timeslices['climate_scenario_list'][cc]]['overall'][country_name][str(data_pop_timeslices['timeslices_list'][c])]= {}   
             c=c+1
            c=0
 
            while c < len(data_land_timeslices_absolute_changes['timeslices_list']):
             land_json['rank']['timeslices_list']['absolute'][data_land_timeslices['climate_scenario_list'][cc]]['overall'][country_name][str(data_land_timeslices_absolute_changes['timeslices_list'][c])]= {} 
             c=c+1
            c=0

            while c < len(data_pop_timeslices_absolute_changes['timeslices_list']):
             pop_json['rank']['timeslices_list']['absolute'][data_pop_timeslices['climate_scenario_list'][cc]]['overall'][country_name][str(data_pop_timeslices_absolute_changes['timeslices_list'][c])]= {}  
             c=c+1
            c=0

            while c < len(data_land_timeslices_relative_changes['timeslices_list']):
             land_json['rank']['timeslices_list']['relative'][data_land_timeslices['climate_scenario_list'][cc]]['overall'][country_name][str(data_land_timeslices_relative_changes['timeslices_list'][c])]= {} 
             c=c+1
            c=0

            while c < len(data_pop_timeslices_relative_changes['timeslices_list']):
             pop_json['rank']['timeslices_list']['relative'][data_pop_timeslices['climate_scenario_list'][cc]]['overall'][country_name][str(data_pop_timeslices_relative_changes['timeslices_list'][c])]= {}  
             c=c+1
            cc=cc+1
            '''
            c=0
            land_json['rank']['year_list']['_'][data_land_years['timeslices_list'][cc]]['overall'] = {}
            land_json['rank']['year_list']['_'][data_land_years['climate_scenario_list'][cc]]['overall'][country_name]= {}   
            while c < len(data_land_years['year_list']):            
             land_json['rank']['year_list']['_'][data_land_years['climate_scenario_list'][cc]]['overall'][country_name][data_land_years['year_list'][c]]= {} 
             c=c+1
            c=0
            pop_json['rank']['year_list']['_'][data_land_years['climate_scenario_list'][cc]]['overall'] = {}
            pop_json['rank']['year_list']['_'][data_land_years['climate_scenario_list'][cc]]['overall']= {}   
            while c < len(data_pop_years['year_list']):  
             pop_json['rank']['year_list']['_'][data_land_years['climate_scenario_list'][cc]]['overall'][country_name][data_pop_years['year_list'][c]]= {}  
             c=c+1
            c=0
            land_json['rank']['year_list']['absolute'][data_land_years['climate_scenario_list'][cc]]['overall'] = {}
            land_json['rank']['year_list']['absolute'][data_land_years['climate_scenario_list'][cc]]['overall'][country_name]= {}   
            while c < len(data_land_years_absolute_changes['year_list']):
             land_json['rank']['year_list']['absolute'][data_land_years['climate_scenario_list'][cc]]['overall'][country_name][data_land_years_absolute_changes['year_list'][c]]= {} 
             c=c+1
            c=0
            pop_json['rank']['year_list']['absolute'][data_land_years['climate_scenario_list'][cc]]['overall'] = {}
            pop_json['rank']['year_list']['absolute'][data_land_years['climate_scenario_list'][cc]]['overall'][country_name]= {}   
            while c < len(data_pop_years_absolute_changes['year_list']):
             pop_json['rank']['year_list']['absolute'][data_land_years['climate_scenario_list'][cc]]['overall'][country_name][data_pop_years_absolute_changes['year_list'][c]] =  {}  
             c=c+1
            c=0
            land_json['rank']['year_list']['relative'][data_land_years['climate_scenario_list'][cc]]['overall'] = {}
            land_json['rank']['year_list']['relative'][data_land_years['climate_scenario_list'][cc]]['overall'][country_name]= {}   
            while c < len(data_land_years_relative_changes['year_list']):
             land_json['rank']['year_list']['relative'][data_land_years['climate_scenario_list'][cc]]['overall'][country_name][data_land_years_relative_changes['year_list'][c]]= {} 
             c=c+1
            c=0
            pop_json['rank']['year_list']['relative'][data_land_years['climate_scenario_list'][cc]]['overall'] = {}
            pop_json['rank']['year_list']['relative'][data_land_years['climate_scenario_list'][cc]]['overall'][country_name]= {}   
            while c < len(data_pop_years_relative_changes['year_list']):
             pop_json['rank']['year_list']['relative'][data_land_years['climate_scenario_list'][cc]]['overall'][country_name][data_pop_years_relative_changes['year_list'][c]]= {}  
             c=c+1  
            '''
                 
          
           c=0
           while c < len(data_land_temperature_change['temperature_list']):
            land_json['rank']['temperature_list']['_']['overall'][country_name][data_land_temperature_change['temperature_list'][c]] = data_land_temperature_change['data']['overall']['median'][c]
            c=c+1
           c=0
           while c < len(data_pop_temperature_change['temperature_list']):
            pop_json['rank']['temperature_list']['_']['overall'][country_name][data_land_temperature_change['temperature_list'][c]] = data_pop_temperature_change['data']['overall']['median'][c]     
            c=c+1 
           c=0
           while c < len(data_land_temperature_change_absolute_changes['temperature_list']):
            land_json['rank']['temperature_list']['absolute']['overall'][country_name][data_land_temperature_change['temperature_list'][c]] = data_land_temperature_change_absolute_changes['data']['overall']['median'][c]
            c=c+1
           c=0
           while c < len(data_pop_temperature_change_absolute_changes['temperature_list']):
            pop_json['rank']['temperature_list']['absolute']['overall'][country_name][data_pop_temperature_change['temperature_list'][c]] = data_pop_temperature_change_absolute_changes['data']['overall']['median'][c]     
            c=c+1
           c=0
           while c < len(data_land_temperature_change_relative_changes['temperature_list']):
            land_json['rank']['temperature_list']['relative']['overall'][country_name][data_land_temperature_change['temperature_list'][c]] = data_land_temperature_change_relative_changes['data']['overall']['median'][c]
            c=c+1
           c=0
           while c < len(data_pop_temperature_change_relative_changes['temperature_list']):
            pop_json['rank']['temperature_list']['relative']['overall'][country_name][data_pop_temperature_change['temperature_list'][c]] = data_pop_temperature_change_relative_changes['data']['overall']['median'][c]     
            c=c+1
           cc=0
           while cc < len(data_land_timeslices['climate_scenario_list']):  
            c=0
            while c < len(data_land_timeslices['timeslices_list']):           
             land_json['rank']['timeslices_list']['_'][data_land_timeslices['climate_scenario_list'][cc]]['overall'][country_name][str(data_land_timeslices['timeslices_list'][c])] = data_land_timeslices['data'][data_land_timeslices['climate_scenario_list'][cc]]['overall']['median'][c]
             c=c+1
            c=0
            while c < len(data_pop_timeslices['timeslices_list']):           
             pop_json['rank']['timeslices_list']['_'][data_pop_timeslices['climate_scenario_list'][cc]]['overall'][country_name][str(data_pop_timeslices['timeslices_list'][c])] = data_pop_timeslices['data'][data_land_timeslices['climate_scenario_list'][cc]]['overall']['median'][c]  
             c=c+1
            c=0
            while c < len(data_land_timeslices_absolute_changes['timeslices_list']):
             land_json['rank']['timeslices_list']['absolute'][data_land_timeslices['climate_scenario_list'][cc]]['overall'][country_name][str(data_land_timeslices_absolute_changes['timeslices_list'][c])] = data_land_timeslices_absolute_changes['data'][data_land_timeslices['climate_scenario_list'][cc]]['overall']['median'][c]
             c=c+1
            c=0
            while c < len(data_pop_timeslices_absolute_changes['timeslices_list']):
             pop_json['rank']['timeslices_list']['absolute'][data_pop_timeslices['climate_scenario_list'][cc]]['overall'][country_name][str(data_pop_timeslices_absolute_changes['timeslices_list'][c])] = data_pop_timeslices_absolute_changes['data'][data_land_timeslices['climate_scenario_list'][cc]]['overall']['median'][c]  
             c=c+1
            c=0
            while c < len(data_land_timeslices_relative_changes['timeslices_list']):
             land_json['rank']['timeslices_list']['relative'][data_land_timeslices['climate_scenario_list'][cc]]['overall'][country_name][str(data_land_timeslices_relative_changes['timeslices_list'][c])] = data_land_timeslices_relative_changes['data'][data_land_timeslices['climate_scenario_list'][cc]]['overall']['median'][c]
             c=c+1
            c=0
            while c < len(data_pop_timeslices_relative_changes['timeslices_list']):
             pop_json['rank']['timeslices_list']['relative'][data_pop_timeslices['climate_scenario_list'][cc]]['overall'][country_name][str(data_pop_timeslices_relative_changes['timeslices_list'][c])] = data_pop_timeslices_relative_changes['data'][data_land_timeslices['climate_scenario_list'][cc]]['overall']['median'][c]  
             c=c+1
            cc=cc+1    
            '''
            c=0
            while c < len(data_land_years['year_list']):            
             land_json['rank']['year_list']['_'][data_land_years['climate_scenario_list'][cc]]['overall'][data_land_years['year_list'][c]][country_name] = data_land_years['data'][data_land_years['climate_scenario_list'][cc]]['overall']['median'][c]
             c=c+1
            c=0
            while c < len(data_pop_years['year_list']):  
             pop_json['rank']['year_list']['_'][data_land_years['climate_scenario_list'][cc]]['overall'][data_pop_years['year_list'][c]][country_name] = data_pop_years['data'][data_land_years['climate_scenario_list'][cc]]['overall']['median'][c]    
             c=c+1
            c=0
            while c < len(data_land_years_absolute_changes['year_list']):
             land_json['rank']['year_list']['absolute'][data_land_years['climate_scenario_list'][cc]]['overall'][data_land_years_absolute_changes['year_list'][c]][country_name] = data_land_years_absolute_changes['data'][data_land_years['climate_scenario_list'][cc]]['overall']['median'][c]
             c=c+1
            c=0
            while c < len(data_pop_years_absolute_changes['year_list']):
             pop_json['rank']['year_list']['absolute'][data_land_years['climate_scenario_list'][cc]]['overall'][data_pop_years_absolute_changes['year_list'][c]][country_name] = data_pop_years_absolute_changes['data'][data_land_years['climate_scenario_list'][cc]]['overall']['median'][c]    
             c=c+1
            c=0
            while c < len(data_land_years_relative_changes['year_list']):
             land_json['rank']['year_list']['relative'][data_land_years['climate_scenario_list'][cc]]['overall'][data_land_years_relative_changes['year_list'][c]][country_name] = data_land_years_relative_changes['data'][data_land_years['climate_scenario_list'][cc]]['overall']['median'][c]
             c=c+1
            c=0
            while c < len(data_pop_years_relative_changes['year_list']):
             pop_json['rank']['year_list']['relative'][data_land_years['climate_scenario_list'][cc]]['overall'][data_pop_years_relative_changes['year_list'][c]][country_name] = data_pop_years_relative_changes['data'][data_land_years['climate_scenario_list'][cc]]['overall']['median'][c]    
             c=c+1  
            ''' 


    land_ranking_json = {}
    pop_ranking_json = {}
  
    land_ranking_json['variable'] = data_land_years['variable']
    pop_ranking_json['variable'] = data_pop_years['variable']
    land_ranking_json['climate_model_list'] = data_land_years['climate_model_list']
    pop_ranking_json['climate_model_list'] = data_pop_years['climate_model_list']
    land_ranking_json['impact_model_list'] = data_land_years['impact_model_list']
    pop_ranking_json['impact_model_list'] = data_pop_years['impact_model_list']
    land_ranking_json['climate_scenario_list'] = data_land_timeslices['climate_scenario_list']
    pop_ranking_json['climate_scenario_list'] = data_pop_timeslices['climate_scenario_list']
    land_ranking_json['temperature_list'] = data_land_temperature_change['temperature_list']
    pop_ranking_json['temperature_list'] = data_pop_temperature_change['temperature_list']         
    land_ranking_json['timeslices_list'] = data_land_timeslices['timeslices_list']
    pop_ranking_json['timeslices_list'] = data_pop_timeslices['timeslices_list']
    #land_ranking_json['years_list'] = data_land_years['year_list']
    #pop_ranking_json['years_list'] = data_pop_years['year_list']

    land_ranking_json['rank'] = {}          
    pop_ranking_json['rank'] = {}   
    land_ranking_json['rank']['temperature_list']= {}
    land_ranking_json['rank']['temperature_list']['_']= {}
    land_ranking_json['rank']['temperature_list']['absolute']= {}
    land_ranking_json['rank']['temperature_list']['relative']= {}   
    pop_ranking_json['rank']['temperature_list']= {}
    pop_ranking_json['rank']['temperature_list']['_']= {}
    pop_ranking_json['rank']['temperature_list']['absolute']= {}
    pop_ranking_json['rank']['temperature_list']['relative']= {}  
    land_ranking_json['rank']['timeslices_list']= {}
    land_ranking_json['rank']['timeslices_list']['_']= {}
    land_ranking_json['rank']['timeslices_list']['absolute']= {}
    land_ranking_json['rank']['timeslices_list']['relative']= {}   
    pop_ranking_json['rank']['timeslices_list']= {}
    pop_ranking_json['rank']['timeslices_list']['_']= {}
    pop_ranking_json['rank']['timeslices_list']['absolute']= {}
    pop_ranking_json['rank']['timeslices_list']['relative']= {}  
    #land_ranking_json['rank']['year_list']= {}
    #land_ranking_json['rank']['year_list']['_']= {}
    #land_ranking_json['rank']['year_list']['absolute']= {}
    #land_ranking_json['rank']['year_list']['relative']= {}   
    #pop_ranking_json['rank']['year_list']= {}
    #pop_ranking_json['rank']['year_list']['_']= {}
    #pop_ranking_json['rank']['year_list']['absolute']= {}
    #pop_ranking_json['rank']['year_list']['relative']= {}  

    land_ranking_json['rank']['temperature_list']['_']['overall'] = {}
    pop_ranking_json['rank']['temperature_list']['_']['overall'] = {}
    land_ranking_json['rank']['temperature_list']['absolute']['overall'] = {}
    pop_ranking_json['rank']['temperature_list']['absolute']['overall'] = {}
    land_ranking_json['rank']['temperature_list']['relative']['overall'] = {}
    pop_ranking_json['rank']['temperature_list']['relative']['overall'] = {}
    land_ranking_json['rank']['timeslices_list']['_']['piControl'] = {}
    land_ranking_json['rank']['timeslices_list']['_']['piControl']['overall'] = {}
    pop_ranking_json['rank']['timeslices_list']['_']['piControl'] = {}
    pop_ranking_json['rank']['timeslices_list']['_']['piControl']['overall'] = {}
    land_ranking_json['rank']['timeslices_list']['absolute']['piControl'] = {}
    land_ranking_json['rank']['timeslices_list']['absolute']['piControl']['overall'] = {}
    pop_ranking_json['rank']['timeslices_list']['absolute']['piControl'] = {}
    pop_ranking_json['rank']['timeslices_list']['absolute']['piControl']['overall'] = {}
    land_ranking_json['rank']['timeslices_list']['relative']['piControl'] = {}            
    land_ranking_json['rank']['timeslices_list']['relative']['piControl']['overall'] = {}
    pop_ranking_json['rank']['timeslices_list']['relative']['piControl'] = {}
    pop_ranking_json['rank']['timeslices_list']['relative']['piControl']['overall'] = {}

    land_ranking_json['rank']['timeslices_list']['_']['historical'] = {}
    land_ranking_json['rank']['timeslices_list']['_']['historical']['overall'] = {}
    pop_ranking_json['rank']['timeslices_list']['_']['historical'] = {}
    pop_ranking_json['rank']['timeslices_list']['_']['historical']['overall'] = {}
    land_ranking_json['rank']['timeslices_list']['absolute']['historical'] = {}
    land_ranking_json['rank']['timeslices_list']['absolute']['historical']['overall'] = {}
    pop_ranking_json['rank']['timeslices_list']['absolute']['historical'] = {}
    pop_ranking_json['rank']['timeslices_list']['absolute']['historical']['overall'] = {}
    land_ranking_json['rank']['timeslices_list']['relative']['historical'] = {}            
    land_ranking_json['rank']['timeslices_list']['relative']['historical']['overall'] = {}
    pop_ranking_json['rank']['timeslices_list']['relative']['historical'] = {}
    pop_ranking_json['rank']['timeslices_list']['relative']['historical']['overall'] = {}

    land_ranking_json['rank']['timeslices_list']['_']['rcp26'] = {}
    land_ranking_json['rank']['timeslices_list']['_']['rcp26']['overall'] = {}
    pop_ranking_json['rank']['timeslices_list']['_']['rcp26'] = {}
    pop_ranking_json['rank']['timeslices_list']['_']['rcp26']['overall'] = {}
    land_ranking_json['rank']['timeslices_list']['absolute']['rcp26'] = {}
    land_ranking_json['rank']['timeslices_list']['absolute']['rcp26']['overall'] = {}
    pop_ranking_json['rank']['timeslices_list']['absolute']['rcp26'] = {}
    pop_ranking_json['rank']['timeslices_list']['absolute']['rcp26']['overall'] = {}
    land_ranking_json['rank']['timeslices_list']['relative']['rcp26'] = {}            
    land_ranking_json['rank']['timeslices_list']['relative']['rcp26']['overall'] = {}
    pop_ranking_json['rank']['timeslices_list']['relative']['rcp26'] = {}
    pop_ranking_json['rank']['timeslices_list']['relative']['rcp26']['overall'] = {}

    land_ranking_json['rank']['timeslices_list']['_']['rcp60'] = {}
    land_ranking_json['rank']['timeslices_list']['_']['rcp60']['overall'] = {}
    pop_ranking_json['rank']['timeslices_list']['_']['rcp60'] = {}
    pop_ranking_json['rank']['timeslices_list']['_']['rcp60']['overall'] = {}
    land_ranking_json['rank']['timeslices_list']['absolute']['rcp60'] = {}
    land_ranking_json['rank']['timeslices_list']['absolute']['rcp60']['overall'] = {}
    pop_ranking_json['rank']['timeslices_list']['absolute']['rcp60'] = {}
    pop_ranking_json['rank']['timeslices_list']['absolute']['rcp60']['overall'] = {}
    land_ranking_json['rank']['timeslices_list']['relative']['rcp60'] = {}            
    land_ranking_json['rank']['timeslices_list']['relative']['rcp60']['overall'] = {}
    pop_ranking_json['rank']['timeslices_list']['relative']['rcp60'] = {}
    pop_ranking_json['rank']['timeslices_list']['relative']['rcp60']['overall'] = {}
    
    
    
    #%%
    #indicator_name = 'river-flood'
    # Create a list of values for then to create the rank.
    country_names= os.listdir (input_foulder+indicator_name+'/ISIMIP-projections')
    for country_name in country_names:
      # JUST NEED TO RUN ONCE THIS IS WHY I PICKED ONE COUNTRY  
      if(country_name == 'AFG'):
           #print(indicator_name+ " - " +country_name)  
           
            land_ranking_json['rank']['temperature_list']['_']['overall']= {} 
            pop_ranking_json['rank']['temperature_list']['_']['overall'] = {}            
            land_ranking_json['rank']['temperature_list']['absolute']['overall']= {}              
            pop_ranking_json['rank']['temperature_list']['absolute']['overall']= {}  
            land_ranking_json['rank']['temperature_list']['relative']['overall']= {}  
            pop_ranking_json['rank']['temperature_list']['relative']['overall']= {}   
            land_ranking_json['rank']['timeslices_list']['_']['piControl']['overall']= {}   
            pop_ranking_json['rank']['timeslices_list']['_']['piControl']['overall']= {}   
            land_ranking_json['rank']['timeslices_list']['absolute']['piControl']['overall']= {}             
            pop_ranking_json['rank']['timeslices_list']['absolute']['piControl']['overall']= {}   
            land_ranking_json['rank']['timeslices_list']['relative']['piControl']['overall']= {}               
            pop_ranking_json['rank']['timeslices_list']['relative']['piControl']['overall']= {}               
        
            land_ranking_json['rank']['timeslices_list']['_']['historical']['overall']= {}   
            pop_ranking_json['rank']['timeslices_list']['_']['historical']['overall']= {}   
            land_ranking_json['rank']['timeslices_list']['absolute']['historical']['overall']= {}             
            pop_ranking_json['rank']['timeslices_list']['absolute']['historical']['overall']= {}   
            land_ranking_json['rank']['timeslices_list']['relative']['historical']['overall']= {}               
            pop_ranking_json['rank']['timeslices_list']['relative']['historical']['overall']= {}               
        
            land_ranking_json['rank']['timeslices_list']['_']['rcp26']['overall']= {}   
            pop_ranking_json['rank']['timeslices_list']['_']['rcp26']['overall']= {}   
            land_ranking_json['rank']['timeslices_list']['absolute']['rcp26']['overall']= {}             
            pop_ranking_json['rank']['timeslices_list']['absolute']['rcp26']['overall']= {}   
            land_ranking_json['rank']['timeslices_list']['relative']['rcp26']['overall']= {}               
            pop_ranking_json['rank']['timeslices_list']['relative']['rcp26']['overall']= {}               
        
            land_ranking_json['rank']['timeslices_list']['_']['rcp60']['overall']= {}   
            pop_ranking_json['rank']['timeslices_list']['_']['rcp60']['overall']= {}   
            land_ranking_json['rank']['timeslices_list']['absolute']['rcp60']['overall']= {}             
            pop_ranking_json['rank']['timeslices_list']['absolute']['rcp60']['overall']= {}   
            land_ranking_json['rank']['timeslices_list']['relative']['rcp60']['overall']= {}               
            pop_ranking_json['rank']['timeslices_list']['relative']['rcp60']['overall']= {}               
             
            c=0
            while c < len(data_land_temperature_change['temperature_list']):
             land_ranking_json['rank']['temperature_list']['_']['overall'][data_land_temperature_change['temperature_list'][c]] = {}
             c=c+1
            c=0
          
            while c < len(data_pop_temperature_change['temperature_list']):
             pop_ranking_json['rank']['temperature_list']['_']['overall'][data_land_temperature_change['temperature_list'][c]]= {} 
             c=c+1 
            c=0
        
            while c < len(data_land_temperature_change_absolute_changes['temperature_list']):
             land_ranking_json['rank']['temperature_list']['absolute']['overall'][data_land_temperature_change['temperature_list'][c]]= {} 
             c=c+1
            c=0
         
            while c < len(data_pop_temperature_change_absolute_changes['temperature_list']):
             pop_ranking_json['rank']['temperature_list']['absolute']['overall'][data_pop_temperature_change['temperature_list'][c]]= {}  
             c=c+1
            c=0
        
            while c < len(data_land_temperature_change_relative_changes['temperature_list']): 
             land_ranking_json['rank']['temperature_list']['relative']['overall'][data_land_temperature_change['temperature_list'][c]]= {}                
             c=c+1
            c=0
        
            while c < len(data_pop_temperature_change_relative_changes['temperature_list']):
             pop_ranking_json['rank']['temperature_list']['relative']['overall'][data_pop_temperature_change['temperature_list'][c]]= {}   
             c=c+1
            cc=0
            while cc < len(data_land_timeslices['climate_scenario_list']):  
             c=0
        
             while c < len(data_land_timeslices['timeslices_list']):           
              land_ranking_json['rank']['timeslices_list']['_'][data_land_timeslices['climate_scenario_list'][cc]]['overall'][str(data_land_timeslices['timeslices_list'][c])]= {} 
              c=c+1
             c=0
        
             while c < len(data_pop_timeslices['timeslices_list']):           
              pop_ranking_json['rank']['timeslices_list']['_'][data_pop_timeslices['climate_scenario_list'][cc]]['overall'][str(data_pop_timeslices['timeslices_list'][c])]= {}   
              c=c+1
             c=0
         
             while c < len(data_land_timeslices_absolute_changes['timeslices_list']):
              land_ranking_json['rank']['timeslices_list']['absolute'][data_land_timeslices['climate_scenario_list'][cc]]['overall'][str(data_land_timeslices_absolute_changes['timeslices_list'][c])]= {} 
              c=c+1
             c=0
        
             while c < len(data_pop_timeslices_absolute_changes['timeslices_list']):
              pop_ranking_json['rank']['timeslices_list']['absolute'][data_pop_timeslices['climate_scenario_list'][cc]]['overall'][str(data_pop_timeslices_absolute_changes['timeslices_list'][c])]= {}  
              c=c+1
             c=0
        
             while c < len(data_land_timeslices_relative_changes['timeslices_list']):
              land_ranking_json['rank']['timeslices_list']['relative'][data_land_timeslices['climate_scenario_list'][cc]]['overall'][str(data_land_timeslices_relative_changes['timeslices_list'][c])]= {} 
              c=c+1
             c=0
        
             while c < len(data_pop_timeslices_relative_changes['timeslices_list']):
              pop_ranking_json['rank']['timeslices_list']['relative'][data_pop_timeslices['climate_scenario_list'][cc]]['overall'][str(data_pop_timeslices_relative_changes['timeslices_list'][c])]= {}  
              c=c+1
             cc=cc+1
             '''
             c=0
             land_ranking_json['rank']['year_list']['_'][data_land_years['timeslices_list'][cc]]['overall'] = {}
             land_ranking_json['rank']['year_list']['_'][data_land_years['climate_scenario_list'][cc]]['overall']= {}   
             while c < len(data_land_years['year_list']):            
              land_ranking_json['rank']['year_list']['_'][data_land_years['climate_scenario_list'][cc]]['overall'][data_land_years['year_list'][c]]= {} 
              c=c+1
             c=0
             pop_ranking_json['rank']['year_list']['_'][data_land_years['climate_scenario_list'][cc]]['overall'] = {}
             pop_ranking_json['rank']['year_list']['_'][data_land_years['climate_scenario_list'][cc]]['overall']= {}   
             while c < len(data_pop_years['year_list']):  
              pop_ranking_json['rank']['year_list']['_'][data_land_years['climate_scenario_list'][cc]]['overall'][data_pop_years['year_list'][c]]= {}  
              c=c+1
             c=0
             land_ranking_json['rank']['year_list']['absolute'][data_land_years['climate_scenario_list'][cc]]['overall'] = {}
             land_ranking_json['rank']['year_list']['absolute'][data_land_years['climate_scenario_list'][cc]]['overall']= {}   
             while c < len(data_land_years_absolute_changes['year_list']):
              land_ranking_json['rank']['year_list']['absolute'][data_land_years['climate_scenario_list'][cc]]['overall'][data_land_years_absolute_changes['year_list'][c]]= {} 
              c=c+1
             c=0
             pop_ranking_json['rank']['year_list']['absolute'][data_land_years['climate_scenario_list'][cc]]['overall'] = {}
             pop_ranking_json['rank']['year_list']['absolute'][data_land_years['climate_scenario_list'][cc]]['overall']= {}   
             while c < len(data_pop_years_absolute_changes['year_list']):
              pop_ranking_json['rank']['year_list']['absolute'][data_land_years['climate_scenario_list'][cc]]['overall'][data_pop_years_absolute_changes['year_list'][c]] =  {}  
              c=c+1
             c=0
             land_ranking_json['rank']['year_list']['relative'][data_land_years['climate_scenario_list'][cc]]['overall'] = {}
             land_ranking_json['rank']['year_list']['relative'][data_land_years['climate_scenario_list'][cc]]['overall']= {}   
             while c < len(data_land_years_relative_changes['year_list']):
              land_ranking_json['rank']['year_list']['relative'][data_land_years['climate_scenario_list'][cc]]['overall'][data_land_years_relative_changes['year_list'][c]]= {} 
              c=c+1
             c=0
             pop_ranking_json['rank']['year_list']['relative'][data_land_years['climate_scenario_list'][cc]]['overall'] = {}
             pop_ranking_json['rank']['year_list']['relative'][data_land_years['climate_scenario_list'][cc]]['overall']= {}   
             while c < len(data_pop_years_relative_changes['year_list']):
              pop_ranking_json['rank']['year_list']['relative'][data_land_years['climate_scenario_list'][cc]]['overall'][data_pop_years_relative_changes['year_list'][c]]= {}  
              c=c+1  
             '''
                
            c=0
            while c < len(data_land_temperature_change['temperature_list']):
              countries_rank = pd.read_excel('/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/Github/ISIPedia/Countries Names.xls')# Creating a rank for [‘overall‘][‘median_relative_changes’][6]
              country_names2= os.listdir (input_foulder+indicator_name+'/ISIMIP-projections')
              for country_name in country_names2:
               if(country_name != 'world'):
                if(country_name != 'oceans'):               
                   countries_rank.set_value(countries_rank.loc[countries_rank['Abbreviation'] == country_name]['Country_Name'].index[0] , 'Index_Rank', 100000*to_zero(land_json['rank']['temperature_list']['_']['overall'][country_name][data_land_temperature_change['temperature_list'][c]]))
                   #print(land_json['rank']['temperature_list']['_']['overall'][country_name][data_land_temperature_change['temperature_list'][c]])
                   #print(country_name, land_json['rank']['temperature_list']['_']['overall'][country_name][data_land_temperature_change['temperature_list'][c]])
              #print(countries_rank)
              countries_rank_sorted = pd.DataFrame(countries_rank.sort_values('Index_Rank', ascending=False).values)
              countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][0]][0].index[0] , 'Rank', 1) 
              b = 1
              while b < countries_rank_sorted.shape[0]:
               if countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]][2].values[0] == countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][2].values[0]:
                countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].index[0] , 'Rank', countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]]['Rank'].values[0]) 
               else: 
                countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].index[0] , 'Rank', countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]]['Rank'].values[0]+1) 
               b=b+1    
              b = 0
              while b < countries_rank_sorted.shape[0]:    
                  land_ranking_json['rank']['temperature_list']['_']['overall'][data_land_temperature_change['temperature_list'][c]][countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].values[0]] = countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]]['Rank'].values[0]
                  b=b+1  
              c=c+1

            print('1')
            c=0
            while c < len(data_pop_temperature_change['temperature_list']):
              countries_rank = pd.read_excel('/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/Github/ISIPedia/Countries Names.xls')# Creating a rank for [‘overall‘][‘median_relative_changes’][6]
              country_names2= os.listdir (input_foulder+indicator_name+'/ISIMIP-projections')
              for country_name in country_names2:
               if(country_name != 'world'):
                if(country_name != 'oceans'):               
                   countries_rank.set_value(countries_rank.loc[countries_rank['Abbreviation'] == country_name]['Country_Name'].index[0] , 'Index_Rank', 100000*to_zero(pop_json['rank']['temperature_list']['_']['overall'][country_name][data_land_temperature_change['temperature_list'][c]]))
              countries_rank_sorted = pd.DataFrame(countries_rank.sort_values('Index_Rank', ascending=False).values)
              countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][0]][0].index[0] , 'Rank', 1) 
              b = 1
              while b < countries_rank_sorted.shape[0]:
               if countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]][2].values[0] == countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][2].values[0]:
                countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].index[0] , 'Rank', countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]]['Rank'].values[0]) 
               else: 
                countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].index[0] , 'Rank', countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]]['Rank'].values[0]+1) 
               b=b+1    
              b = 0
              while b < countries_rank_sorted.shape[0]:    
                  pop_ranking_json['rank']['temperature_list']['_']['overall'][data_pop_temperature_change['temperature_list'][c]][countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].values[0]] = countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]]['Rank'].values[0]
                  b=b+1  
              c=c+1
            print('2')
            c=0
            while c < len(data_land_temperature_change_absolute_changes['temperature_list']):
              countries_rank = pd.read_excel('/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/Github/ISIPedia/Countries Names.xls')# Creating a rank for [‘overall‘][‘median_relative_changes’][6]
              country_names2= os.listdir (input_foulder+indicator_name+'/ISIMIP-projections')
              for country_name in country_names2:
               if(country_name != 'world'):
                if(country_name != 'oceans'):               
                   countries_rank.set_value(countries_rank.loc[countries_rank['Abbreviation'] == country_name]['Country_Name'].index[0] , 'Index_Rank', 100000*to_zero(land_json['rank']['temperature_list']['absolute']['overall'][country_name][data_land_temperature_change['temperature_list'][c]]))
              countries_rank_sorted = pd.DataFrame(countries_rank.sort_values('Index_Rank', ascending=False).values)
              countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][0]][0].index[0] , 'Rank', 1) 
              b = 1
              while b < countries_rank_sorted.shape[0]:
               if countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]][2].values[0] == countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][2].values[0]:
                countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].index[0] , 'Rank', countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]]['Rank'].values[0]) 
               else: 
                countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].index[0] , 'Rank', countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]]['Rank'].values[0]+1) 
               b=b+1    
              b = 0
              while b < countries_rank_sorted.shape[0]:    
                  land_ranking_json['rank']['temperature_list']['absolute']['overall'][data_land_temperature_change['temperature_list'][c]][countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].values[0]] = countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]]['Rank'].values[0]
                  b=b+1                     
              c=c+1
            
            print('3') 
            c=0
            while c < len(data_pop_temperature_change_absolute_changes['temperature_list']):
              countries_rank = pd.read_excel('/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/Github/ISIPedia/Countries Names.xls')# Creating a rank for [‘overall‘][‘median_relative_changes’][6]
              country_names2= os.listdir (input_foulder+indicator_name+'/ISIMIP-projections')
              for country_name in country_names2:
               if(country_name != 'world'):
                if(country_name != 'oceans'):               
                   countries_rank.set_value(countries_rank.loc[countries_rank['Abbreviation'] == country_name]['Country_Name'].index[0] , 'Index_Rank', 100000*to_zero(pop_json['rank']['temperature_list']['absolute']['overall'][country_name][data_pop_temperature_change['temperature_list'][c]]))
              countries_rank_sorted = pd.DataFrame(countries_rank.sort_values('Index_Rank', ascending=False).values)
              countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][0]][0].index[0] , 'Rank', 1) 
              b = 1
              while b < countries_rank_sorted.shape[0]:
               if countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]][2].values[0] == countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][2].values[0]:
                countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].index[0] , 'Rank', countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]]['Rank'].values[0]) 
               else: 
                countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].index[0] , 'Rank', countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]]['Rank'].values[0]+1) 
               b=b+1    
              b = 0
              while b < countries_rank_sorted.shape[0]:    
                  pop_ranking_json['rank']['temperature_list']['absolute']['overall'][data_pop_temperature_change['temperature_list'][c]][countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].values[0]] = countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]]['Rank'].values[0]
                  b=b+1                      
              c=c+1
            print('4')
            c=0
            while c < len(data_pop_temperature_change_absolute_changes['temperature_list']):
              countries_rank = pd.read_excel('/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/Github/ISIPedia/Countries Names.xls')# Creating a rank for [‘overall‘][‘median_relative_changes’][6]
              country_names2= os.listdir (input_foulder+indicator_name+'/ISIMIP-projections')
              for country_name in country_names2:
               if(country_name != 'world'):
                if(country_name != 'oceans'):               
                   countries_rank.set_value(countries_rank.loc[countries_rank['Abbreviation'] == country_name]['Country_Name'].index[0] , 'Index_Rank', 100000*to_zero(land_json['rank']['temperature_list']['relative']['overall'][country_name][data_land_temperature_change['temperature_list'][c]]))
              countries_rank_sorted = pd.DataFrame(countries_rank.sort_values('Index_Rank', ascending=False).values)
              countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][0]][0].index[0] , 'Rank', 1) 
              b = 1
              while b < countries_rank_sorted.shape[0]:
               if countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]][2].values[0] == countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][2].values[0]:
                countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].index[0] , 'Rank', countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]]['Rank'].values[0]) 
               else: 
                countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].index[0] , 'Rank', countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]]['Rank'].values[0]+1) 
               b=b+1    
              b = 0
              while b < countries_rank_sorted.shape[0]:    
                  land_ranking_json['rank']['temperature_list']['relative']['overall'][data_land_temperature_change['temperature_list'][c]][countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].values[0]] = countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]]['Rank'].values[0]
                  b=b+1 
              c=c+1
            print('5') 
            c=0
            while c < len(data_pop_temperature_change_absolute_changes['temperature_list']):
              countries_rank = pd.read_excel('/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/Github/ISIPedia/Countries Names.xls')# Creating a rank for [‘overall‘][‘median_relative_changes’][6]
              country_names2= os.listdir (input_foulder+indicator_name+'/ISIMIP-projections')
              for country_name in country_names2:
               if(country_name != 'world'):
                if(country_name != 'oceans'):               
                   countries_rank.set_value(countries_rank.loc[countries_rank['Abbreviation'] == country_name]['Country_Name'].index[0] , 'Index_Rank', 100000*to_zero(pop_json['rank']['temperature_list']['relative']['overall'][country_name][data_pop_temperature_change['temperature_list'][c]]))
              countries_rank_sorted = pd.DataFrame(countries_rank.sort_values('Index_Rank', ascending=False).values)
              countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][0]][0].index[0] , 'Rank', 1) 
              b = 1
              while b < countries_rank_sorted.shape[0]:
               if countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]][2].values[0] == countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][2].values[0]:
                countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].index[0] , 'Rank', countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]]['Rank'].values[0]) 
               else: 
                countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].index[0] , 'Rank', countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]]['Rank'].values[0]+1) 
               b=b+1    
              b = 0
              while b < countries_rank_sorted.shape[0]:    
                  pop_ranking_json['rank']['temperature_list']['relative']['overall'][data_pop_temperature_change['temperature_list'][c]][countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].values[0]] = countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]]['Rank'].values[0]
                  b=b+1 
              c=c+1
            c=0
 
            print('6')
            cc=0
            while cc < len(data_land_timeslices['climate_scenario_list']):  
             c=0
             while c < len(data_land_timeslices['timeslices_list']):           
              countries_rank = pd.read_excel('/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/Github/ISIPedia/Countries Names.xls')# Creating a rank for [‘overall‘][‘median_relative_changes’][6]
              country_names2= os.listdir (input_foulder+indicator_name+'/ISIMIP-projections')
              for country_name in country_names2:
               if(country_name != 'world'):
                if(country_name != 'oceans'):               
                   countries_rank.set_value(countries_rank.loc[countries_rank['Abbreviation'] == country_name]['Country_Name'].index[0] , 'Index_Rank', 100000*to_zero(land_json['rank']['timeslices_list']['_'][data_land_timeslices['climate_scenario_list'][cc]]['overall'][country_name][str(data_land_timeslices['timeslices_list'][c])]))
              countries_rank_sorted = pd.DataFrame(countries_rank.sort_values('Index_Rank', ascending=False).values)
              countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][0]][0].index[0] , 'Rank', 1) 
              b = 1
              while b < countries_rank_sorted.shape[0]:
               if countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]][2].values[0] == countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][2].values[0]:
                countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].index[0] , 'Rank', countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]]['Rank'].values[0]) 
               else: 
                countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].index[0] , 'Rank', countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]]['Rank'].values[0]+1) 
               b=b+1    
              b = 0
              while b < countries_rank_sorted.shape[0]:    
                  land_ranking_json['rank']['timeslices_list']['_'][data_land_timeslices['climate_scenario_list'][cc]]['overall'][str(data_land_timeslices['timeslices_list'][c])][countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].values[0]] = countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]]['Rank'].values[0]
                  b=b+1
              c=c+1
             print('7')
             c=0
             while c < len(data_pop_timeslices['timeslices_list']):           
              countries_rank = pd.read_excel('/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/Github/ISIPedia/Countries Names.xls')# Creating a rank for [‘overall‘][‘median_relative_changes’][6]
              country_names2= os.listdir (input_foulder+indicator_name+'/ISIMIP-projections')
              for country_name in country_names2:
               if(country_name != 'world'):
                if(country_name != 'oceans'):               
                   countries_rank.set_value(countries_rank.loc[countries_rank['Abbreviation'] == country_name]['Country_Name'].index[0] , 'Index_Rank', 100000*to_zero(pop_json['rank']['timeslices_list']['_'][data_pop_timeslices['climate_scenario_list'][cc]]['overall'][country_name][str(data_pop_timeslices['timeslices_list'][c])]))
              countries_rank_sorted = pd.DataFrame(countries_rank.sort_values('Index_Rank', ascending=False).values)
              countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][0]][0].index[0] , 'Rank', 1) 
              b = 1
              while b < countries_rank_sorted.shape[0]:
               if countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]][2].values[0] == countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][2].values[0]:
                countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].index[0] , 'Rank', countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]]['Rank'].values[0]) 
               else: 
                countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].index[0] , 'Rank', countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]]['Rank'].values[0]+1) 
               b=b+1    
              b = 0
              while b < countries_rank_sorted.shape[0]:    
                  pop_ranking_json['rank']['timeslices_list']['_'][data_land_timeslices['climate_scenario_list'][cc]]['overall'][str(data_pop_timeslices['timeslices_list'][c])][countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].values[0]] = countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]]['Rank'].values[0]
                  b=b+1 
              c=c+1
             print('8')
             c=0
             while c < len(data_land_timeslices_absolute_changes['timeslices_list']):
              countries_rank = pd.read_excel('/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/Github/ISIPedia/Countries Names.xls')# Creating a rank for [‘overall‘][‘median_relative_changes’][6]
              country_names2= os.listdir (input_foulder+indicator_name+'/ISIMIP-projections')
              for country_name in country_names2:
               if(country_name != 'world'):
                if(country_name != 'oceans'):               
                   countries_rank.set_value(countries_rank.loc[countries_rank['Abbreviation'] == country_name]['Country_Name'].index[0] , 'Index_Rank', 100000*to_zero(land_json['rank']['timeslices_list']['absolute'][data_land_timeslices['climate_scenario_list'][cc]]['overall'][country_name][str(data_land_timeslices_absolute_changes['timeslices_list'][c])]))
              countries_rank_sorted = pd.DataFrame(countries_rank.sort_values('Index_Rank', ascending=False).values)
              countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][0]][0].index[0] , 'Rank', 1) 
              b = 1
              while b < countries_rank_sorted.shape[0]:
               if countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]][2].values[0] == countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][2].values[0]:
                countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].index[0] , 'Rank', countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]]['Rank'].values[0]) 
               else: 
                countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].index[0] , 'Rank', countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]]['Rank'].values[0]+1) 
               b=b+1    
              b = 0
              while b < countries_rank_sorted.shape[0]:    
                  land_ranking_json['rank']['timeslices_list']['absolute'][data_land_timeslices['climate_scenario_list'][cc]]['overall'][str(data_pop_timeslices['timeslices_list'][c])][countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].values[0]] = countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]]['Rank'].values[0]
                  b=b+1
              c=c+1
             print('9')
             c=0
             while c < len(data_pop_timeslices_absolute_changes['timeslices_list']):
              countries_rank = pd.read_excel('/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/Github/ISIPedia/Countries Names.xls')# Creating a rank for [‘overall‘][‘median_relative_changes’][6]
              country_names2= os.listdir (input_foulder+indicator_name+'/ISIMIP-projections')
              for country_name in country_names2:
               if(country_name != 'world'):
                if(country_name != 'oceans'):               
                   countries_rank.set_value(countries_rank.loc[countries_rank['Abbreviation'] == country_name]['Country_Name'].index[0] , 'Index_Rank', 100000*to_zero(pop_json['rank']['timeslices_list']['absolute'][data_pop_timeslices['climate_scenario_list'][cc]]['overall'][country_name][str(data_pop_timeslices_absolute_changes['timeslices_list'][c])]))
              countries_rank_sorted = pd.DataFrame(countries_rank.sort_values('Index_Rank', ascending=False).values)
              countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][0]][0].index[0] , 'Rank', 1) 
              b = 1
              while b < countries_rank_sorted.shape[0]:
               if countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]][2].values[0] == countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][2].values[0]:
                countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].index[0] , 'Rank', countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]]['Rank'].values[0]) 
               else: 
                countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].index[0] , 'Rank', countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]]['Rank'].values[0]+1) 
               b=b+1    
              b = 0
              while b < countries_rank_sorted.shape[0]:    
                  pop_ranking_json['rank']['timeslices_list']['absolute'][data_land_timeslices['climate_scenario_list'][cc]]['overall'][str(data_pop_timeslices['timeslices_list'][c])][countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].values[0]] = countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]]['Rank'].values[0]
                  b=b+1
              c=c+1
             print('10')
             c=0
             while c < len(data_land_timeslices_relative_changes['timeslices_list']):
              countries_rank = pd.read_excel('/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/Github/ISIPedia/Countries Names.xls')# Creating a rank for [‘overall‘][‘median_relative_changes’][6]
              country_names2= os.listdir (input_foulder+indicator_name+'/ISIMIP-projections')
              for country_name in country_names2:
               if(country_name != 'world'):
                if(country_name != 'oceans'):               
                   countries_rank.set_value(countries_rank.loc[countries_rank['Abbreviation'] == country_name]['Country_Name'].index[0] , 'Index_Rank', 100000*to_zero(land_json['rank']['timeslices_list']['relative'][data_land_timeslices['climate_scenario_list'][cc]]['overall'][country_name][str(data_land_timeslices_relative_changes['timeslices_list'][c])]))
              countries_rank_sorted = pd.DataFrame(countries_rank.sort_values('Index_Rank', ascending=False).values)
              countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][0]][0].index[0] , 'Rank', 1) 
              b = 1
              while b < countries_rank_sorted.shape[0]:
               if countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]][2].values[0] == countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][2].values[0]:
                countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].index[0] , 'Rank', countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]]['Rank'].values[0]) 
               else: 
                countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].index[0] , 'Rank', countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]]['Rank'].values[0]+1) 
               b=b+1    
              b = 0
              while b < countries_rank_sorted.shape[0]:    
                  land_ranking_json['rank']['timeslices_list']['relative'][data_land_timeslices['climate_scenario_list'][cc]]['overall'][str(data_pop_timeslices['timeslices_list'][c])][countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].values[0]] = countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]]['Rank'].values[0]
                  b=b+1
              c=c+1
             print('11')
             c=0
             while c < len(data_pop_timeslices_relative_changes['timeslices_list']):
              countries_rank = pd.read_excel('/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/Github/ISIPedia/Countries Names.xls')# Creating a rank for [‘overall‘][‘median_relative_changes’][6]
              country_names2= os.listdir (input_foulder+indicator_name+'/ISIMIP-projections')
              for country_name in country_names2:
               if(country_name != 'world'):
                if(country_name != 'oceans'):               
                   countries_rank.set_value(countries_rank.loc[countries_rank['Abbreviation'] == country_name]['Country_Name'].index[0] , 'Index_Rank', 100000*to_zero(pop_json['rank']['timeslices_list']['relative'][data_pop_timeslices['climate_scenario_list'][cc]]['overall'][country_name][str(data_pop_timeslices_relative_changes['timeslices_list'][c])]))
              countries_rank_sorted = pd.DataFrame(countries_rank.sort_values('Index_Rank', ascending=False).values)
              countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][0]][0].index[0] , 'Rank', 1) 
              b = 1
              while b < countries_rank_sorted.shape[0]:
               if countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]][2].values[0] == countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][2].values[0]:
                countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].index[0] , 'Rank', countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]]['Rank'].values[0]) 
               else: 
                countries_rank_sorted.set_value(countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].index[0] , 'Rank', countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b-1]]['Rank'].values[0]+1) 
               b=b+1    
              b = 0
              while b < countries_rank_sorted.shape[0]:    
                  pop_ranking_json['rank']['timeslices_list']['relative'][data_land_timeslices['climate_scenario_list'][cc]]['overall'][str(data_pop_timeslices['timeslices_list'][c])][countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]][0].values[0]] = countries_rank_sorted.loc[countries_rank_sorted[0] == countries_rank_sorted[0][b]]['Rank'].values[0]
                  b=b+1
              c=c+1
             cc=cc+1    
            print('12')
            '''
             c=0
             while c < len(data_land_years['year_list']):            
              land_ranking_json['rank']['year_list']['_'][data_land_years['climate_scenario_list'][cc]]['overall'][data_land_years['year_list'][c]][country_name] = data_land_years['data'][data_land_years['climate_scenario_list'][cc]]['overall']['median'][c]
              c=c+1
             c=0
             while c < len(data_pop_years['year_list']):  
              pop_ranking_json['rank']['year_list']['_'][data_land_years['climate_scenario_list'][cc]]['overall'][data_pop_years['year_list'][c]][country_name] = data_pop_years['data'][data_land_years['climate_scenario_list'][cc]]['overall']['median'][c]    
              c=c+1
             c=0
             while c < len(data_land_years_absolute_changes['year_list']):
              land_ranking_json['rank']['year_list']['absolute'][data_land_years['climate_scenario_list'][cc]]['overall'][data_land_years_absolute_changes['year_list'][c]][country_name] = data_land_years_absolute_changes['data'][data_land_years['climate_scenario_list'][cc]]['overall']['median'][c]
              c=c+1
             c=0
             while c < len(data_pop_years_absolute_changes['year_list']):
              pop_ranking_json['rank']['year_list']['absolute'][data_land_years['climate_scenario_list'][cc]]['overall'][data_pop_years_absolute_changes['year_list'][c]][country_name] = data_pop_years_absolute_changes['data'][data_land_years['climate_scenario_list'][cc]]['overall']['median'][c]    
              c=c+1
             c=0
             while c < len(data_land_years_relative_changes['year_list']):
              land_ranking_json['rank']['year_list']['relative'][data_land_years['climate_scenario_list'][cc]]['overall'][data_land_years_relative_changes['year_list'][c]][country_name] = data_land_years_relative_changes['data'][data_land_years['climate_scenario_list'][cc]]['overall']['median'][c]
              c=c+1
             c=0
             while c < len(data_pop_years_relative_changes['year_list']):
              pop_ranking_json['rank']['year_list']['relative'][data_land_years['climate_scenario_list'][cc]]['overall'][data_pop_years_relative_changes['year_list'][c]][country_name] = data_pop_years_relative_changes['data'][data_land_years['climate_scenario_list'][cc]]['overall']['median'][c]    
              c=c+1  
            '''   

            
            
  #%%          
            
import json            

land_json = json.dumps(land_ranking_json, ensure_ascii=False)            
pop_json = json.dumps(pop_ranking_json, ensure_ascii=False)              
            
with open('/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/data_cube/land_ranking_river-flood.json', 'w') as fp:
    json.dump(land_json, fp)            

with open('/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/data_cube/pop_ranking_river-flood.json', 'w') as fp:
    json.dump(pop_json, fp)                        
            
            
            
            
            
            
            
            
            
            
            
        #%%              
           # ADD THE 3 CLIMATE MODELS AND 8 IMPACT MODELS      

           for cml in data_land_years['climate_model_list']:
            for iml in data_land_years['impact_model_list']:  

             for tl in data_land_years['temperature_list']:
               c=0
               while c < len():
                 land_ranking_json['rank']['temperature_list']['_'][cml][iml][country_name] = data_land_temperature_change['data']['run'][cml][iml]['median'][tl]
                 c=c+1  
               c=0
               while c < len():
                 pop_ranking_json['rank']['temperature_list']['_'][cml][iml][country_name] = data_pop_temperature_change['data']['run'][cml][iml]['median'][tl]
                 c=c+1  
               c=0
               while c < len():
                 land_ranking_json['rank']['temperature_list']['absolute'][cml][iml][country_name] = data_land_temperature_change_absolute_changes['data']['run'][cml][iml]['median'][tl]
                 c=c+1  
               c=0
               while c < len():
                 pop_ranking_json['rank']['temperature_list']['absolute'][cml][iml][country_name] = data_pop_temperature_change_absolute_changes['data']['run'][cml][iml]['median'][tl] 
                 c=c+1  
               c=0
               while c < len():
                 land_ranking_json['rank']['temperature_list']['relative'][cml][iml][country_name] = data_land_temperature_change_relative_changes['data']['run'][cml][iml]['median'][tl]
                 c=c+1  
               c=0
               while c < len():
                 pop_ranking_json['rank']['temperature_list']['relative'][cml][iml][country_name] = data_pop_temperature_change_relative_changes['data']['run'][cml][iml]['median'][tl]                           
                 c=c+1  
               c=0
               while c < len():
  

             for tsl in data_land_years['timeslices_list']: 
               c=0
               while c < len():
                 land_ranking_json['rank']['timeslices_list']['_'][cml][iml][country_name] = data_land_timeslices['data']['run'][cml][iml]['median'][tl]
                 c=c+1  
               c=0
               while c < len():
                 pop_ranking_json['rank']['timeslices_list']['_'][cml][iml][country_name] = data_pop_timeslices['data']['run'][cml][iml]['median'][tl] 
                 c=c+1  
               c=0
               while c < len():
                 land_ranking_json['rank']['timeslices_list']['absolute'][cml][iml][country_name] = data_land_timeslices_absolute_changes['data']['run'][cml][iml]['median'][tl]
                 c=c+1  
               c=0
               while c < len():
                 pop_ranking_json['rank']['timeslices_list']['absolute'][cml][iml][country_name] = data_pop_timeslices_absolute_changes['data']['run'][cml][iml]['median'][tl] 
                 c=c+1  
               c=0
               while c < len():
                 land_ranking_json['rank']['timeslices_list']['relative'][cml][iml][country_name] = data_land_timeslices_relative_changes['data']['run'][cml][iml]['median'][tl]
                 c=c+1  
               c=0
               while c < len():
                 pop_ranking_json['rank']['timeslices_list']['relative'][cml][iml][country_name] = data_pop_timeslices_relative_changes['data']['run'][cml][iml]['median'][tl]                  
                 c=c+1  

      
             for yl in data_land_years['year_list']:           
               c=0
               while c < len():
                 land_ranking_json['rank']['year_list']['_'][cml][iml][country_name] = data_land_years['data']['run'][cml][iml]['median'][tl]
                 c=c+1  
               c=0
               while c < len():
                 pop_ranking_json['rank']['year_list']['_'][cml][iml][country_name] = data_pop_years['data']['run'][cml][iml]['median'][tl]  
                 c=c+1  
               c=0
               while c < len():
                 land_ranking_json['rank']['year_list']['absolute'][cml][iml][country_name] = data_land_years_absolute_changes['data']['run'][cml][iml]['median'][tl]
                 c=c+1  
               c=0
               while c < len():
                 pop_ranking_json['rank']['year_list']['absolute'][cml][iml][country_name] = data_pop_years_absolute_changes['data']['run'][cml][iml]['median'][tl]   
                 c=c+1  
               c=0
               while c < len():
                 land_ranking_json['rank']['year_list']['relative'][cml][iml][country_name] = data_land_years_relative_changes['data']['run'][cml][iml]['median'][tl]
                 c=c+1  
               c=0
               while c < len():
                 pop_ranking_json['rank']['year_list']['relative'][cml][iml][country_name] = data_pop_years_relative_changes['data']['run'][cml][iml]['median'][tl]                   
                 c=c+1  





           for cml in data_land_years['climate_model_list']:
            for iml in data_land_years['impact_model_list']:  

             for tl in data_land_years['temperature_list']:

                 land_ranking_json['rank']['temperature_list']['_'][cml][iml][country_name] = data_land_temperature_change['data']['run'][cml][iml]['median'][tl]
                 c=c+1  

                 pop_ranking_json['rank']['temperature_list']['_'][cml][iml][country_name] = data_pop_temperature_change['data']['run'][cml][iml]['median'][tl]
                 c=c+1  

                 land_ranking_json['rank']['temperature_list']['absolute'][cml][iml][country_name] = data_land_temperature_change_absolute_changes['data']['run'][cml][iml]['median'][tl]
                 c=c+1  

                 pop_ranking_json['rank']['temperature_list']['absolute'][cml][iml][country_name] = data_pop_temperature_change_absolute_changes['data']['run'][cml][iml]['median'][tl] 
                 c=c+1  

                 land_ranking_json['rank']['temperature_list']['relative'][cml][iml][country_name] = data_land_temperature_change_relative_changes['data']['run'][cml][iml]['median'][tl]
                 c=c+1  

                 pop_ranking_json['rank']['temperature_list']['relative'][cml][iml][country_name] = data_pop_temperature_change_relative_changes['data']['run'][cml][iml]['median'][tl]                           
                 c=c+1  

                 tl = tl + 1
             for tsl in data_land_years['timeslices_list']: 

                 land_ranking_json['rank']['timeslices_list']['_'][cml][iml][country_name] = data_land_timeslices['data']['run'][cml][iml]['median'][tl]
                 c=c+1  

                 pop_ranking_json['rank']['timeslices_list']['_'][cml][iml][country_name] = data_pop_timeslices['data']['run'][cml][iml]['median'][tl] 
                 c=c+1  

                 land_ranking_json['rank']['timeslices_list']['absolute'][cml][iml][country_name] = data_land_timeslices_absolute_changes['data']['run'][cml][iml]['median'][tl]
                 c=c+1  

                 pop_ranking_json['rank']['timeslices_list']['absolute'][cml][iml][country_name] = data_pop_timeslices_absolute_changes['data']['run'][cml][iml]['median'][tl] 
                 c=c+1  

                 land_ranking_json['rank']['timeslices_list']['relative'][cml][iml][country_name] = data_land_timeslices_relative_changes['data']['run'][cml][iml]['median'][tl]
                 c=c+1  

                 pop_ranking_json['rank']['timeslices_list']['relative'][cml][iml][country_name] = data_pop_timeslices_relative_changes['data']['run'][cml][iml]['median'][tl]                  
                 c=c+1  

                 tsl = tsl + 1
             for yl in data_land_years['year_list']:           

                 land_ranking_json['rank']['year_list']['_'][cml][iml][country_name] = data_land_years['data']['run'][cml][iml]['median'][tl]
                 c=c+1  

                 pop_ranking_json['rank']['year_list']['_'][cml][iml][country_name] = data_pop_years['data']['run'][cml][iml]['median'][tl]  
                 c=c+1  

                 land_ranking_json['rank']['year_list']['absolute'][cml][iml][country_name] = data_land_years_absolute_changes['data']['run'][cml][iml]['median'][tl]
                 c=c+1  

                 pop_ranking_json['rank']['year_list']['absolute'][cml][iml][country_name] = data_pop_years_absolute_changes['data']['run'][cml][iml]['median'][tl]   
                 c=c+1  

                 land_ranking_json['rank']['year_list']['relative'][cml][iml][country_name] = data_land_years_relative_changes['data']['run'][cml][iml]['median'][tl]
                 c=c+1  

                 pop_ranking_json['rank']['year_list']['relative'][cml][iml][country_name] = data_pop_years_relative_changes['data']['run'][cml][iml]['median'][tl]                   
                 c=c+1  

                 yl = yl + 1





















#%%

    # Sort the list, i.e. create the rank.
    #country_names= os.listdir (input_foulder+indicator_name+'/ISIMIP-projections')
    #for country_name in country_names:
    #  if(country_name != 'oceans'):       
    #countries_rank = pd.read_excel('/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/Github/ISIPedia/Countries Names.xls')# Creating a rank for [‘overall‘][‘median_relative_changes’][6]
    #if(indicator_name == 'land-area-affected-by-crop-failure'):    
    #country_names= os.listdir (input_foulder+indicator_name+'/ISIMIP-projections')
    #for country_name in country_names:
    #    if(len(country_name) == 3):
    #     json_temperature_change = input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/'+indicator_name+'_ISIMIP-projections_'+country_name+'_versus-temperature-change.json'
    #     json_timeslices =         input_foulder+indicator_name+'/ISIMIP-projections/'+country_name+'/'+indicator_name+'_ISIMIP-projections_'+country_name+'_versus-timeslices.json'
           
    #     json_server = open(json_temperature_change).read()
    #     json_server = json_server.replace('.,','.0,')
    #     json_server = json_server.replace('.]','.0]')

    #     json_local = open('/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/intermediate.json', 'w')
    #     json_local.write(json_server)
    #     json_local.close()     

    #     with open('/home/julian/Documents/My ASUS (antigo)/IIASA/Water Group/ISIpedia/intermediate.json') as f:
    #       data = json.load(f)    
    #     if (country_name != 'world'):




    #%%


