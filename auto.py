import streamlit as st
st.header('General Information')
company_name   = st.text_input('Name of Organization',key='company_name')
contact_person = st.text_input('Contact Person',key='contact_person')
address        = st.text_input('Address',key='address')
phone          = st.text_input('Phone',key='phone')
fax            = st.text_input('Fax',key='fax')
email          = st.text_input('E-mail',key='email')
st.header('Organizational Information')
org_type      = st.radio('Type of Organization',['Manufacturing','R&D','Institution','Office Building','Others'],key='org_type')
if org_type=='Others':
    org_type=st.text_input('Please specify the type of organization',key='others')
process_description = st.file_uploader('Brief description of process (Please attach a process flow chart or block diagram water entry &amp; exit points)',key='process_description')
if org_type=='Manufacturing':
    product_num=st.number_input('Please enter the number of products manufactured',step=1,key='product_num')
    product_list={}
    while product_num:
        product_name=st.text_input('Please enter the name of the product',key=str('product_list'+str(product_num)))
        production_rates=[]
        product_list[product_name]={}
        production_rate_last_year=st.text_input('Please enter the annual production rate last year',key=str('production_rate_last_year'+str(product_num)))
        production_rate_this_year=st.text_input('Please enter the annual production rate in the current year',key=str('production_rate_this_year'+str(product_num)))
        production_rates.append(production_rate_last_year)
        production_rates.append(production_rate_this_year)
        product_list[product_name]=production_rates
        product_num-=1
total_employees  = st.number_input('Please enter the number of employees you have in total',step=1,key='total_employees')
permanent        = st.number_input(f'Out of the total {total_employees} employees, how many of them are permanent employees?',step=1,key='Permanent_employees')
temp             = st.number_input(f'Out of the total {total_employees} employees, how many of them are temporary employees?',step=1,key='Temp_employees')
guest            = st.number_input('How many Guests/Visitors do you have?',step=1,key='guests')
shifts_per_day   = st.number_input('Number of shifts per day',step=1)
op_days_per_week = st.number_input('Number of operating days per week',step=1)
st.header('Water Consumption and Treatment Details')
total_water_consumption_2021_2022 = st.number_input('What was your total annual water consumption in  (m\u00b3/day)?',key='total_water_2021_2022')
industrial_water_consumption_2021_2022 = st.number_input(f'Out of {total_water_consumption_2021_2022}, how much of it was used for industrial purposes (m\u00b3/day)?',key='industrial_water_2021_2022')
domestic_water_consumption_2021_2022 = st.number_input(f'Out of {total_water_consumption_2021_2022}, how much of it was used for domestic purposes(Includes canteen, irrigation, drinking etc) (m\u00b3/day)?',key='domestic_water_2021_2022')
total_water_consumption_2022_2023 = st.number_input('What is total annual water consumption last year (m\u00b3/day)?',key='total_water_2022_2023')
industrial_water_consumption_2022_2023 = st.number_input(f'Out of {total_water_consumption_2022_2023}, how much of it was used for industrial purposes (m\u00b3/day)?',key='industrial_water_2022_2023')
domestic_water_consumption_2022_2023 = st.number_input(f'Out of {total_water_consumption_2022_2023}, how much of it was used for domestic purposes(Includes canteen, irrigation, drinking etc) (m\u00b3/day)?',key='domestic_water_2022_2023')
water_sources = st.text_input('Please enter the names of water sources(Borewell, river, municipal,etc.)',key='water_sources')
raw_water_cost = st.number_input('Please enter the per m\u00b3 cost of raw water',key='raw_water_cost')
domestic_water_cost = st.number_input('Please enter the per m\u00b3 cost of domestic water',key='domestic_water_cost')
soft_water_cost = st.number_input('Please enter the per m\u00b3 cost of soft water',key='soft_water_cost')
raw_water_description        = st.file_uploader('Please enter the analytical report of raw water (pH, Turbidity, TSS, TDS, Total hardness, chlorides, sulphates, silica, fluoride, iron, sodium)(Pl. attach report of analysis for all sources of water)',key='Raw_water_description')
water_treatment_plant_scheme = st.file_uploader('Please attach the Water Treatment Plant scheme (Please attach schematic diagram with brief description)',key='water_treatment_plant_description')
industrial_water_make_up={}
st.write('**Please enter the break-up of Industrial Water Consumption (m\u00b3/day)**')
industrial_water_consumption_breakup={}
industrial_water_consumption_breakup['process'] = st.number_input('Process',key='industrial_water_process')
industrial_water_consumption_breakup['cooling_tower_make_up'] = st.number_input('Cooling tower make up',key='industrial_water_cooling_tower')
industrial_water_consumption_breakup['boiler_make_up'] = st.number_input('Boiler make up',key='industrial_boiler_make_up')
industrial_water_consumption_breakup['evaporative_coolers'] = st.number_input('Evaporative Coolers',key='industrial_boiler_evaportive_coolers')
industrial_water_consumption_breakup['dm_plant_feed'] = st.number_input('DM Plant feed',key='industrial_dm_plant_feed')
industrial_water_consumption_breakup['plant_equipment_washings'] = st.number_input('Plant Equipment washings',key='industrial_plant_equipment_washings')
others_ind=st.radio('Is there any other form of water consumption?',['Yes','No'],key='industrial_water_consumption_others')
if others_ind=='Yes':
    industrial_water_consumption_breakup['Others']=[]
    consumption_type_ind=st.text_input('Please specify the type of water consumption',key='water_consumption_type')
    consumption_amount = st.number_input('Please enter the amount of water consumption',key='water_consumption_others_amount')
    industrial_water_consumption_breakup['Others'].append(consumption_type_ind)
    industrial_water_consumption_breakup['Others'].append(consumption_amount)
user_points_metered = st.radio('Are all user points metered?',['Yes','No'],key='User_points_metered')
st.write('**Please enter the break-up of domestic Water Consumption (m\u00b3/day)**')
domestic_water_consumption_breakup={}
domestic_water_consumption_breakup['Canteen'] = st.number_input('Canteen',key='doemstic_water_canteen')
domestic_water_consumption_breakup['Toilets'] = st.number_input('Toilets/Urinals',key='domestic_water_toilets')
domestic_water_consumption_breakup['Showers'] = st.number_input('Showers',key='domestic_water_showers')
others_dom=st.radio('Is there any other form of water consumption?',['Yes','No'],key='domestic_water_consumption_others')
if others_dom=='Yes':
    domestic_water_consumption_breakup['Others']=[]
    consumption_type_dom=st.text_input('Please specify the type of water consumption',key='dom_water_consumption_type')
    consumption_amount_dom = st.number_input('Please enter the amount of water consumption',key='dom_water_consumption_others_amount')
    industrial_water_consumption_breakup['Others'].append(consumption_type_dom)
    industrial_water_consumption_breakup['Others'].append(consumption_amount_dom)
irrigation_water_consumption=st.number_input('What is the amount of water consumption for Landscape/Irrigation/Gardening(m\u00b3/day)')
irrigation_type=st.radio('What is the type of irrigation technique used?',['Conventional','Drip Irrigation','Sprinkler','Others(Please Specify)'],key='irrigation_type')
if irrigation_type=='Others(Please Specify)':
    irrigation_type=st.text_input('Please specify the type of irrigation',key='irrigation_type_others')
irrigation_schedule = st.radio('Please specify the schedule of irrigation',['Daily','Others(Please Specify)'],key='irrigation_schedule')
if irrigation_schedule=='Others(Please Specify)':
    irrigation_schedule=st.text_input('Please specify the schedule of irrigation',key='irrigation_schedule_others')
irrigation_area = st.number_input('Please enter the area of irrigation(in acres or m\u00b2)',key='irrigation_area')
st.header('Waste Water Generation and Treatment Details')
total_waste_water = st.number_input('What is the total amount of waste water discharge? (m\u00b3/day)',key='totla_waste_water_discharge')
waste_industrial_effluent = st.number_input('How much of this waste water is coming from industrial effluent?',key='waste_water_industrial')
waste_domestic = st.number_input('How much of this waste water is coming from domestic sources?',key='waste_water_domestic')
waste_water_report = st.file_uploader('Please attach an analytical report of waste water (pH,TSS,TDS,chlorides, sulphates, Oil & grease, COD, BOD)',key='waste_water_file_upload')
waste_water_industrial_effluent_report = st.file_uploader('Please attach an analytical report of waste water coming from industrial effluents',key='industrial_waste_water_file_upload')
waste_water_domestic_report = st.file_uploader('Please attach an analytical report of waste water coming from domestic sources',key='domestic_waste_water_file_upload')
st.write('**Please write the break-up of waste water(m\u00b3/day)')
waste_cooling_tower_blow_down = st.number_input('Cooling tower blow down',key='waste_cooling_tower_blowdown')
waste_boiler_blow_down = st.number_input('Boiler blow down',key='waste_boiler_blowdown')
waste_dm_plant_regeneration = st.number_input('DM Plant Regeneration',key='dm_plant_regeneration')
waste_process = st.number_input('Process',key='waste_process')
waste_sewage  = st.number_input('Sewage',key='waste_sewage')
waste_others  = st.radio('Do you have any other source of waste water?',['Yes','No'],key='waste_others')
if waste_others=='Yes':
    waste_others_type=st.text_input('Please specify the type of waste water discharge?',key='waste_water_discharge_type')
    waste_others_volume=st.number_input('Please enter the amount of waste water usage in others',key='waste_water_amount')
discharge_metered = st.radio('Are all discharges metered?',['Yes','No'],key='discharge_metered')
waste_water_treatment_scheme = st.file_uploader('Please upload a report of WasteWater Treatment Plant Scheme (Please attach scehematic diagram with brief description)',key='waste_water_treamtment_plant_scheme')
captive_power_plant = st.file_uploader('Please specify the details of captive power plant',key='captive+power_plant_schematic')
water_conservation_projects_number = st.number_input('How many water conservation projects have been implemented so far?',step=1,key='water_conservation_number')
water_conservation_projects_list=[]
while water_conservation_projects_number:
    project_name=st.file_uploader('Please enter the details of the project',key='water_conservation_project_detail'+str(water_conservation_projects_number))
    water_conservation_projects_list.append(project_name)
    water_conservation_projects_number-=1
rainwater_harvesting = st.radio('Are you doing rain water harvesting?',['Yes','No'],key='rain_water_harvesting')
harvesting_roof_top_area = st.number_input('What is the rooftop area (m\u00b2)',key='water_harvesting_rooftop_area')
harvesting_paved_area = st.number_input('What is the paved area (m\u00b2)',key='water_harvesting_paved_area')
harvesting_unpaved_area = st.number_input('What is the unpaved area (m\u00b2)',key='water_harvesting_unpaved_area')
available_empty_land = st.number_input('How much empty land area is available for storage, watershed development?(m\u00b2)',key='empty_land_area')


        
    


