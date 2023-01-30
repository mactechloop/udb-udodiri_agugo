import streamlit as st
import json
import csv
import pandas as pd
import firebase_admin
from firebase_admin import db
import string
import random

def generateRandom():
    N = 7
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

    return res


st.title("""Assessment of Anthropometric Status
""")

st.text("___"*100)

st.subheader(""" Dear Respondents,
""")

st.write("""This is a Community/Public Health Nutrition Research intended to gather information on the “Nutritional Status and Prevalence of Malnutrition among IDPs (6-60years) in Nigeria and Effect of Nutrition Education on Eating Behaviour of target Population”
Your cooperation is needed to obtain anthropometric measurements as a parameter to be assessed.   
All information is purely for research purpose, and shall be kept confidential. 
No name is required. 
""")

st.write("""
    Thank you for your attention. 
""")

st.text("___"*100)

state = st.selectbox('State', ('Abuja', 'Bayelsa', 'Brono'))

st.text("___"*100)


st.subheader("Section A: Personal Data")

a1 = st.selectbox('Age', ('A (6-8)', 'B (9-11)', 'C (12-14)', 'D (15-17)',
'E (18-20)', 'F (21-25)', 'G (26-30)', 'H (31-45)', 'I (46-50)', 'J (51-55)', 'K (55-60)'))
a2 = st.selectbox('Gender', ('A (male)', 'B (female)'))

user_age_cat = ''
if a1[0] in ['A', 'B']:
   user_age_cat = "School Children"
elif a1[0] in ['C', 'D', 'E']:
    user_age_cat = 'Adolescent'
elif a1[0] in ['F', 'G', 'H', 'I', 'J', 'K']:
    user_age_cat = 'Adult'
    
st.text("___"*100)

st.subheader("SECTION B: Anthropometric Indices of Respondents")
l1 = st.number_input('Height (M)')
l2 = st.number_input('Weight (KG)')
l3 = st.number_input('Waist circumference (CM)')
l4 = st.number_input('Hip circumference (CM)')

if st.button("Submit Questionnare"):

    try:
        height = l1 * l1
        bmi = l2 / height
        wthr = l3 / l4
    except:
        bmi = 0
        wthr = 0

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
            "Age": a1[0],
            "Sex": a2[0],
            "State" : state,
            "Age Category" : user_age_cat,
            "Height" : l1,
            "Weight" : l2,
            "Waist Circumference" : l3,
            "Hip Circumference" : l4,
            "BMI" : bmi,
            "WTHR" : wthr
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
    st.info('Your BMI is --> ' + str(bmi))
    st.info('Your Waist-to-hip-ratio is --> ' + str(wthr))

