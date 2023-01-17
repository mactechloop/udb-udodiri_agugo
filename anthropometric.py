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


st.title("""Anthropometric (BMI &Waist-To-Hip-Ratio) Status of Subjects/Respondents
""")

st.text("___"*100)

st.subheader(""" Dear madam/sir,
""")

st.write("""In partial fulfillment of the requirement for the award of bachelor in science (B.Sc.) in human nutrition and dietetics, 
I ……. with registration number …… is conducting a study on ‘Anthropometric (BMI &waist-to-hip-ratio) status of …..”. 
Information obtained from this questionnaire is strictly for research purpose and will be kept confidential. 
Please, answer all questions in each section below.
""")

st.write("""
    Thank you for your attention. 
""")

st.text("___"*100)


st.subheader("SECTION A: Personal Data")

a1 = st.selectbox('Age', ('A (18-25)', 'B (26-35)', 'C (36-50)', 'D ( > 50)'))
a2 = st.selectbox('Sex', ('A (male)', 'B (female)'))
a3 = st.selectbox('Occupation', ('A (trader)', 'B (farmer)', 'C (civil servant)', 'D (banker)'))
a4 = st.selectbox('If your answer in question 3 is ‘C’, designation:', 
    ('A (administrative staff)', 'B (secretary)', 'C (cleaner/messenger)', 'D (other)'))

st.text("___"*100)

st.subheader("SECTION B: Anthropometric Indices of Respondents")
l1 = st.number_input('Height (M)')
l2 = st.number_input('Weight (kG)')
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

    
    ref2 = db.reference("/Users/kycSunj6OASdyDgWnL6FTdEQbh23/Questionnaires/UDV77h6e/Count")
    a = ref2.get()
    n_a = int(a) + 1

    myData = {
        generateRandom() : {
            "Age": a1[0],
            "Sex": a2[0],
            "Occupation": a3[0],
            "Designation For Question 3" : a4[0],
            "Height" : l1,
            "Weight" : l2,
            "Waist Circumference" : l3,
            "Hip Circumference" : l4
        }
    }

    with open("jsondata.json", "w") as sd:
        json.dump(myData, sd)

    with open("jsondata.json", "w") as sd:
                json.dump(myData, sd)

    ref2.set(str(n_a))


    ref = db.reference("/Users/kycSunj6OASdyDgWnL6FTdEQbh23/Questionnaires/UDV77h6e/CollectedData/" + generateRandom())
    with open("jsondata.json", "r") as f:
        file_contents = json.load(f)

    for key, value in file_contents.items():
        ref.set(value)

        

    st.success('Data added Successfully')  
    st.info('Your BMI is --> ' + str(bmi))
    st.info('Your Waist-to-hip-ratio is --> ' + str(wthr))

