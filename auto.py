import streamlit as st
st.header('General Information')
company_name   = st.text_input('Name of the company')
contact_person = st.text_input('Contact Person')
address        = st.text_input('Address')
phone          = st.text_input('Phone')
fax            = st.text_input('Fax')
email          = st.text_input('E-mail')
st.header('Organizational Information')
org_type      = st.radio('Type of Organization',['Manufacturing','R&D','Institution','Office Building','Others'],key='Manufacturing')
if org_type=='Others':
    org_type=st.text_input('Please specify the type of organization')
process_description = st.file_uploader('Brief description of process (Please attach a process flow chart or block diagram water entry &amp; exit points)')
if org_type=='Manufacturing':
    manu_num = st.number_input('How many manufacturing items did they list?',step=1)
    product_list=[]
    while manu_num:
        product_list.append(st.text_input('Product name',key=f'{manu_num}'))
        manu_num-=1
if st.button('Please click here to enter the number of employees you have'):
    permanent = st.number_input('Permanent',step=1)
    temp      = st.number_input('Temporary/Contract',step=1)
    guest     = st.number_input('Guests/Visitors',step=1)
shifts_per_day = st.number_input('Number of shifts per day',step=1)
op_days_per_week = st.number_input('Number of operating days per week',step=1)
st.header('Water Consumption and Treatment Details')
if (st.button('Please press here to enter the total water consumption per annum (m\u00b3/annum)')):
    industrial_water_consumption = st.number_input('Industrial (cooling, process & utilities)',step=1)
    domestic_water_consumption   = st.number_input('Domestic (Includes canteen, irrigation, drinking etc)',step=1) 
if (st.button('Please press here to enter the details of water sources')):
    industrial_water_sources = st.number_input('Industrial (cooling, process & utilities)',step=1)
    domestic_water_sources   = st.number_input('Domestic (Includes canteen, irrigation, drinking etc)',step=1) 
raw_water_cost = st.number_input('Cost of Raw water (Rs./ m\u00b3)',step=1)
domestic_water_cost = st.number_input('Cost of domestic water (Rs./ m\u00b3)',step=1)
soft_water_cost = st.number_input('Cost of soft water (Rs./ m\u00b3)',step=1)
raw_water_description        = st.file_uploader('Analytical report of raw water (pH, Turbidity, TSS, TDS, Total hardness, chlorides, sulphates, silica, fluoride, iron, sodium)(Pl. attach report of analysis for all sources of water)')
water_treatment_plant_scheme = st.file_uploader('Water Treatment Plant scheme (Please attach schematic diagram with brief description)')
if st.button('Break-Up of Industrial Water Consumption (m\u00b3/day)'):
    process = st.number_input('Process')
    cooling_tower_make_up = st.number_input('Cooling tower make up')
    boiler_make_up = st.number_input('Boiler make up')
    evaporative_coolers = st.number_input('Evaporative Coolers')
    dm_plant_feed = st.number_input('DM Plant feed')
    plant_equipment_washings = st.number_input('Plant Equipment washings')
    if st.button('Others(Please Specify)'):
        num=st.number_input('How many others specified?')
        con_amount=[]
        while num:
            con_type = st.text_input('Enter the type of water consumption')
            con_amount.append(con_type)
            num-=1
discharge = st.radio('Are all discharges metered(yes/no)',['Yes','No'])
waste_water_treatment_plant_scheme       = st.file_uploader('Waste Water Treatment Plant scheme (Please attach schematic diagram with brief description)')
captive_power_plant       = st.file_uploader('Details of captive power plant')
if st.button('Please click here to list the water conservation projects implemented in the past'):
    cons_num = st.number_input('How many conservation projects are mentioned?')
    cons_projects = []
    while cons_num:
        cons_projects.append(st.text_input('Mention the project'))
if st.button('Please click here to give the details of rainwater harvesting'):
    roof_top_area   = st.number_input('Roof top area(m\u00b2)')
    paved_area      = st.number_input('Paved area(m\u00b2)')
    unpaved_area    = st.number_input('Unpaved area(m\u00b2)')



        
    


