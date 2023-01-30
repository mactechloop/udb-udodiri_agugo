import streamlit as st
import json
import csv
import pandas as pd
import firebase_admin
from firebase_admin import db
import string
import random
import datetime

def generateRandom():
    N = 7
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

    return res


st.title("""Assessment of Soci-demographic and Food Consumption Pattern""")

st.text("___"*100)

st.subheader(""" Dear Respondents,
""")

st.write("""This is a Community/Public Health Nutrition Research intended to gather information on the 
“Nutritional Status and Prevalence of Malnutrition among IDPs (6-60years) in Nigeria and Effect of Nutrition Education on Eating Behaviour of target Population”
In line with the research objectives, data on socio-demographic status, food consumption pattern and causes of malnutrition at households is required. 
Information obtained from this questionnaire is strictly for research purpose and will be kept confidential.
Please, answer all questions in each section below.
""")

st.write("""
    Thank you for your attention. 
""")

st.text("___"*100)

st.subheader("Population Record")

a1 = st.date_input(
    "Date of administration of questionnaire",
    datetime.date(2019, 7, 6))
a2 = st.text_input("Site of interview")
a3 = st.selectbox('State', ('Abuja', 'Bayelsa', 'Brono'))
a4 = st.text_input("LGA")
a5 = st.text_input("Type of shelter")
a6 = st.text_input("Name of IDP Camp")
a7 = st.text_input("Household Number")
a8 = st.text_input("Interviewer\'s Name")
a9 = st.text_input("Mortality rate…Crude/ moderate/low")

st.text("___"*100)
st.subheader("Section A: Socio-demographic data of households")


b1 = st.selectbox('Age of household head', ('A (18-25)', 'B (26-35)', 'C (36-50)', 'D ( > 50)'))
b2 = st.selectbox('Gender', ('A (male)', 'B (female)'))
b3 = st.selectbox('Educational Background', ('A (FSLC)', 'B (SSCE)', 'C (graduate)', 'D (none)'))
b4 = st.selectbox('Status of household head', ('A (Father)', 'B (Mother)', 'C (Relation)', 'D (Sibling)'))
b5 = st.selectbox('Duration in camp', ('A ( < 6months)', 'B (6months to 1year)', 'C ( > 2years)', 'D (not sure)'))
b6 = st.selectbox('Occupation', ('A (Civil servant)', 'B (trader)', 'C (farmer)', 'D (other)'))
b7 = st.selectbox('Any income level', ('A (Yes)', 'B (No)'))
b8 = st.selectbox('Income Level', ('A ( < N10,000)', 'B (N20,000-N50,000)', 'C (N50,000-N80,000)', 'D ( > N80,000)'))
b9 = st.selectbox('Household size (male and female)', ('A (1-2)', 'B (3-5)', 'C (5-7)', 'D ( > 5)'))
b10 = st.selectbox('Common nutritional/health problem', ('A (edema )', 'B (underweight)', 'C (overweight)', 'D (wasting )'))
b11 = st.selectbox('Population mostly affected', ('A (Preschool (6months-5yrs))', 'B (School children (6yrs-11yrs))', 
'C (Adolescents (11yrs-18yrs))', 'D (Adults (18yrs-60yrs))'))
b12 = st.selectbox('Mortality rate', ('A (2-4 daily)', 'B (2-4 weekly)', 'C (2-5 monthly)', 'D (not sure)'))

st.text("___"*100)

st.subheader("Section B: Food Consumption Pattern of Households")
c1 = st.selectbox('(1) How often do you purchase food?', ('A (Daily)', 'B (Weekly)', 'C (every other day)', 'D (monthly)'))
c2 = st.selectbox('(2) How much do you spend on food in a month', ('A ( < N10,000)', 'B (N10,000- N20,000)', 'C (N20,000- N30,000)', 'D ( > N40,000)'))
c3 = st.selectbox('(3) How many times do you eat in a day?', ('A (Once)', 'B (Twice)', 'C (Thrice)', 'D (Not Sure)'))
c4 = st.selectbox('(4) Which of these food groups constitute your regular breakfast?', ('A (Grains/cereals)', 'B (Legumes)', 'C (Root & Tuber)', 'D (Noodles)'))
c5 = st.selectbox('(5) Reason For Food Choice', ('A (Cheap)', 'B (Available)', 'C (Easy to Cook)', 'D (Taste)'))
c6 = st.selectbox('(6) Which of these food groups constitute your regular lunch?', ('A (Grains/cereals)', 'B (Legumes)', 'C (Root & Tuber)', 'D (Noodles)'))
c7 = st.selectbox('(7) Reason For Food Choice', ('A (Cheap)', 'B (Available)', 'C (Easy to Cook)', 'D (Taste)'))
c8 = st.selectbox('(8) Which of these food groups constitute your regular dinner?', ('A (Grains/cereals)', 'B (Legumes)', 'C (Root & Tuber)', 'D (Noodles)'))
c9 = st.selectbox('(9) Reason For Food Choice', ('A (Cheap)', 'B (Available)', 'C (Easy to Cook)', 'D (Taste)'))
c10 = st.selectbox('(10) How often do you take snacks?', ('A (Every day)', 'B (Twice a week)', 'C (Thrice a day)', 'D (Not sure)'))
c11 = st.selectbox('(11) What type of snacks do you consume regularly ', (' A (Soft drink/malt  & doughnut/ pie/bun)', 'B (Soft drink/malt & biscuits)',
'C (Banana & groundnut / Cucumber &groundnut)', 'D (Garri, sugar  & groundnut/Garri & salt)'))
c12 = st.selectbox('(12) Reason for choice of snack', ('A (Cheap)', 'B (Available)', 'C (Taste)', 'D (Not sure)'))
c13 = st.selectbox('(13) How often do you eat fruits and vegetables? ', ('A (Every day)', 'B (Twice a week)', 'C (Thrice a day)', 'D (Not sure)'))
c14 = st.selectbox('(15) Reason for choice of fruits and vegetable', ('A (Cheap)', 'B (Available)', 'C (Taste)', 'D (Not sure)'))
c15 = st.selectbox('(16) Do you skip meals? ', ('A (Yes)', 'B (No)'))
c16 = st.selectbox('(17) How often do you skip meal', ('A (Daily)', 'B (Weekly)', 'C (monthly)', 'D (not sure)'))
c17 = st.selectbox('(18) Reason for skipping meals', ('A (Loss of appetite)', 'B (No food) ', 'C (Busy)', 'D (Not sure)'))

st.text("___"*100)

st.subheader("Section C: Possible Causes of Malnutrition at the Households")
d1 = st.selectbox('Environment', ('A (Flooded )', 'B (Sloppy)', 'C (Normal )', 'D (Undefined)'))
d2 = st.selectbox('Accommodation/shelter', ('A (Spacious and decent)', 'B (Jam-packed but decent)', 'C (Spacious but not decent )',
 'D (Jam-packed and not decent)'))
d3 = st.selectbox('Source of water ', ('A (Stream)', 'B (Water supply)', 'C (Very poor )', 'D (Undefined)'))
d4 = st.selectbox('Sanitation', ('A (Hygienic)', 'B (Unhygienic)', 'C (Borehole)', 'D (Man power))'))
d5 = st.selectbox('Access to food', ('A (Adequate)', 'B (Insufficient)', 'C (Very poor )', 'D (Moderate)'))
d6 = st.selectbox('Access to health facilities (clinic, health workers, nurses, doctors)', ('A (Adequate)', 'B (Insufficient)', 'C (Very poor )', 'D (Moderate)'))
d7 = st.selectbox('Access to school facilities ', ('A (Adequate)', 'B (Insufficient)', 'C (Very poor )', 'D (Moderate)'))
d8 = st.selectbox('Access to good toilet facilities', ('A (Adequate)', 'B (Insufficient)', 'C (Very poor )', 'D (Moderate)'))
d9 = st.selectbox('Intervention programmes (government sponsored/ NGOs)', ('A (Adequate)', 'B (Insufficient)', 'C (Very poor )', 'D (Moderate)'))
d10 = st.selectbox('Relevance of interventions ', ('A (Relevant)', 'B (Not relevant)', 'C (Fair )', 'D (Undefined)'))
d11 = st.selectbox('Beneficiaries of interventions', ('A (Infants)', 'B (Women)', 'C (Children )', 'D (Every household member)'))
d12 = st.selectbox('Effectiveness of interventions', ('A (Adequate)', 'B (Good)', 'C (Fair )', 'D (Poor)'))
d13 = st.selectbox('Sustainability of interventions ', ('A (Adequate)', 'B (Good)', 'C (Fair )', 'D (Poor)'))
d14 = st.selectbox('Financial capability', ('A (Adequate)', 'B (Inadequate)', 'C (Low )', 'D (Very Low)'))
d15 = st.selectbox('Financial support', ('A (Adequate)', 'B (Good)', 'C (Fair )', 'D (Poor)'))
d16 = st.selectbox('Gender inequality', ('A (High)', 'B (Very high)', 'C (Moderate )', 'D (Low)'))
d17 = st.selectbox('Gender violence (rape, abuse etc)', ('A (High)', 'B (Very high)', 'C (Moderate )', 'D (Low)'))

if st.button("Submit Questionnare"):


    if firebase_admin._DEFAULT_APP_NAME not in firebase_admin._apps:
        cred_obj = firebase_admin.credentials.Certificate('qdataapp-firebase.json')
        firebase_admin.initialize_app(cred_obj, {
        'databaseURL':"https://qdataapp-default-rtdb.firebaseio.com/"
        })

    
    ref2 = db.reference("/Users/g4WDG6gkkhPpTOeoP3szUJf9L603/Questionnaires/hhBT3w7Y/Count")
    a = ref2.get()
    n_a = int(a) + 1

    myData = {
        generateRandom() : {
            "Date of administration of questionnaire ": str(a1),
            "Site of interview": a2,
            "State" : a3,
            "LGA" : a4,
            "Type of shelter": a5,
            "Name of IDP Camp" : a6,
            "Household Number" : a7,
            "Interviewer’s Name" : a8,
            "Mortality rate Crude or moderate or low" : a9,
            "Age of household head": b1[0],
            "Gender": b2[0],
            "Educational Background": b3[0],
            "Status of household head" : b4[0],
            "Duration in camp" : b5[0],
            "Occupation" : b6[0],
            "Any income level" : b7[0],
            "Income Level" : b8[0],
            "Household size (male and female)" : b9[0],
            "Common nutritional or health problem" : b10[0],
            "Population mostly affected" : b11[0],
            "Mortality Rate" : b12[0],
            "How often do you purchase food" : c1[0],
            "How much do you spend on food in a month" : c2[0],
            "How many times do you eat in a day" : c3[0],
            "Which of these food groups constitute your regular breakfast" : c4[0],
            "Reason for food choice (Breakfast)" : c5[0],
            "Which of these food groups constitute your regular lunch" : c6[0],
            "Reason for food choice (Lunch)" : c7[0],
            "Which of these food groups constitute your regular dinner" : c8[0],
            "Reason for food choice (Dinner)" : c9[0],
            "How often do you take snacks" : c10[0],
            "What type of snacks do you consume regularly " : c11[0],
            "Reason for choice of snack " : c12[0],
            "How often do you eat fruits and vegetables" : c13[0],
            "Reason for choice of fruits and vegetable" : c14[0],
            "Do you skip meals" : c15[0],
            "How often do you skip meal" : c16[0],
            "Reason for skipping meals" : c17[0],
            "Environment" : d1[0],
            "Accommodation orshelter" : d2[0],
            "Source of water" : d3[0],
            "Sanitation" : d4[0],
            "Access to food" : d5[0],
            "Access to health facilities (clinic, health workers, nurses, doctors)" : d6[0],
            "Access to school facilities" : d7[0],
            "Access to good toilet facilities" : d8[0],
            "Intervention programmes (government sponsored or NGOs)" : d9[0],
            "Relevance of interventions" : d10[0],
            "Beneficiaries of interventions" : d11[0],
            "Effectiveness of interventions" : d12[0],
            "Sustainability of interventions" : d13[0],
            "Financial capability" : d14[0],
            "Financial support" : d15[0],
            "Gender inequality " : d16[0],
            "Gender violence (rape, abuse etc)" : d17[0],
        }
    }

    with open("jsondata.json", "w") as sd:
        json.dump(myData, sd)

    with open("jsondata.json", "w") as sd:
                json.dump(myData, sd)

    ref2.set(str(n_a))


    ref = db.reference("/Users/g4WDG6gkkhPpTOeoP3szUJf9L603/Questionnaires/hhBT3w7Y/CollectedData/" + generateRandom())
    with open("jsondata.json", "r") as f:
        file_contents = json.load(f)

    for key, value in file_contents.items():
        ref.set(value)

        

    st.success('Data added Successfully')  
