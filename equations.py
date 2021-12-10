import streamlit as st


def household():
    noofmembers=st.number_input("Enter Number of Members in your Household",min_value=1)
    electricity=st.number_input("Enter the kWh of Electricity Used")
    naturalgas=st.number_input("Enter kWh of Natural Gas Used ")
    heatingoil=st.number_input("Enter Litres of Heating Oil Used")
    coal=st.number_input("Enter Metric Tons of Coal Used")
    lpg=st.number_input("Enter Litres of LPG Used")
    propane=st.number_input("Enter Litres of Propane Used")
    woodenpellets=st.number_input("Enter Metric Tons of Wooden Pellets Used")
    f_electicity=((electricity/1000)*0.7080)
    f_naturalgas=((naturalgas/100)*0.02)
    f_heatingoil=((heatingoil/100)*0.27)
    f_coal=(coal*2.88)
    f_lpg=((lpg/100)*0.17)
    f_propane=((propane/100)*0.16)
    f_woodenpellets=(woodenpellets*0.07)
    total=(f_electicity+f_coal+f_heatingoil+f_lpg+f_naturalgas+f_propane+f_woodenpellets)/(noofmembers)
    st.title('Your Carbon Footprint is'+" "+str(total)+" "+"Metric Tonnes")

def publictransport():
    bus=((st.number_input("Enter the Distance Travelled in Bus")/1000)*0.10)
    coach=((st.number_input("Enter the Distance Travelled in Coach")/1000)*0.03)
    localtrain=((st.number_input("Enter the Distance Travelled in Local")/1000)*0.04)
    longdistancetrain=((st.number_input("Enter the Distance Travelled in Long Distance Train")/10000)*0.05)
    tram=((st.number_input("Enter the Distance Travelled in tram")/1000)*0.03)
    subway=((st.number_input("Enter the Distance Travelled in subway")/1000)*0.03)
    taxi=((st.number_input("Enter the Distance Travelled in taxi")/50)*0.01)
    total1=(bus+coach+localtrain+longdistancetrain+tram+subway+taxi)
    st.title('Your Carbon Footprint is'+" "+str(total1)+" "+"Metric Tonnes")
    
def carcarbonfootprint():
    carsize = st.selectbox(
    'Select Car Size',
    ('Sports car or large SUV (35 mpg)', 'Small or medium SUV, or MPV (46 mpg)','City, small, medium, large or estate car (52 mpg)','Enter Custom mpg'))
    carmileage = st.selectbox(
    'Select 12-month car mileage',
    ('Choose an Option','Low (6,000 miles)', 'Average (9,000 miles)','High (12,000 miles)','Enter Custom milage'))
    
    if carsize=='Sports car or large SUV (35 mpg)':
        size=35
    if carsize=='Small or medium SUV, or MPV (46 mpg)':
        size=46
    if carsize=='City, small, medium, large or estate car (52 mpg)':
        size=52

    if carmileage=='Choose an Option':
        mileage=0
    if carmileage=='Low (6,000 miles)':
        mileage=6000
    if carmileage=='Average (9,000 miles)':
        mileage=9000
    if carmileage=='High (12,000 miles)':
        mileage=12000

        
    carfootprint123=(((((mileage/size)*14.3)/1000)*0.907185)/1)
    st.title('Your Carbon Footprint is'+" "+str(carfootprint123)+" "+"Metric Tonnes")
    
def food():
    food1 = st.selectbox(
    'How much of the food that you eat is organic?',
    ('None','Some', 'Most','All'))
    food2 = st.selectbox(
    'How much meat/dairy do you eat personally?',
    ('Above-average meat/dairy','Average meat/dairy', 'Below-average meat/dairy','Lacto-vegetarian','Vegan'))
    food3 = st.selectbox(
    'How much of your food is produced locally?',
    ('Very little (much foreign / out of season food)','Average', 'Above average','Almost all'))
    food4 = st.selectbox(
    'How much of your food is packaged or processed?',
    ('Above average','Average', 'Below average','Very little'))
    food5 = st.selectbox(
    'How much do you compost potato peelings, leftover and unused food etc?',
    ('None','Some','All'))

    if food1=='None':
        organic=0.7
    if food1=='Some':
        organic=0.5
    if food1=='Most':
        organic=0.2
    if food1=='All':
        organic=0

    if food2=='Above-average meat/dairy':
        meat=0.6
    if food2=='Average meat/dairy':
        meat=0.4
    if food2=='Below-average meat/dairy':
        meat=0.25
    if food2=='Lacto-vegetarian':
        meat=0.1
    if food2=='Vegan':
        meat=0

    if food3=='Very little (much foreign / out of season food)':
       foodmiles=0.5
    if food3=='Average':
       foodmiles=0.3
    if food3=='Above average':
       foodmiles=0.2
    if food3=='Almost all':
       foodmiles=0.1
        
    if food4=='Above average':
        package=0.6
    if food4=='Average':
        package=0.4
    if food4=='Below average':
        package=0.2
    if food4=='Very little':
        package=0.05
        
    if food5=='None':
        composting=0.2
    if food5=='Some':
        composting=0.1
    if food5=='All':
        composting=0
    
    total=(organic+meat+foodmiles+package+composting)
    st.title('Your Carbon Footprint is'+" "+str(total)+" "+"Tonnes")