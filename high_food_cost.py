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


st.title("Food Cost on Food Choice & BMI")

st.text("___"*100)

st.write("""
## Dear madam/sir,
""")

st.write("""
    In partial fulfilment of the requirement for the award of bachelor in science (B.Sc.) in human nutrition and dietetics, 
    I ……. with registration number …… is conducting a study on ‘Food Cost on Food Choice & BMI status of …..”. 
    Information obtained from this questionnaire is strictly for research purpose and will be kept confidential. 
    Please, answer all questions in each section below.
""")

st.write("""
    Thank you for your attention. 
""")

st.text("___"*100)

st.subheader("Section A: Socio-Economic Status of respondents ")

a1 = st.selectbox('Age', ('A (15-24)', 'B (25-34)', ' C (35-44)', 'D (45-59)'))
a2 = st.selectbox('Sex', ('A (male)', 'B (female)', 'C (other)'))
a3 = st.selectbox('Sponsor', ('A (both parents)', 'B (single parent)', 'C (relative)', 'D (self sponsor)'))
a4 = st.selectbox('Edu./Qualification of Sponsor', ('A (FSLC)', 'B (SSCE)', 'C (graduate)', 'D (none)'))
a5 = st.selectbox('Sponsor\'s Occupation', ('A (Trader)', 'B (Farmer)', 'C (Civil servant)', 'D (Other)'))
a6 = st.selectbox('Family income (monthly)', ('A ( ≤ N50,000)', 'B (N60,000-N80,000)', 'C (N90,000 -N110,000)', 'D ( ≥ N120,000)'))
a7 = st.selectbox('Religion', ('A (Traditional religion)', 'B (Christianity)', 'C (Islam)', 'D (other)'))
a8 = st.selectbox('Family Size', ('A (2-3)', 'B (4-6)', 'C (7-10)', 'D ( > 10)'))

st.text("___"*100)  

st.subheader("SECTION B: Food Choice")

st.text("___"*100)

b1 = st.selectbox('(1) How often do you purchase food?', ('A (Daily)', 'B (Weekly)', 'C (every other day)', 'D (monthly)'))
b2 = st.selectbox('(2) How much do you spend on food in a month', ('A ( < N10,000)', 'B (N10,000- N20,000)', 'C (N20,000- N30,000)', 'D ( > N40,000)'))
b3 = st.selectbox('(3) How many times do you eat in a day?', ('A (Once)', 'B (Twice)', 'C (Thrice)', 'D (Not Sure)'))
b4 = st.selectbox('(4) Which of these food groups constitute your regular breakfast?', ('A (Grains/cereals)', 'B (Legumes)', 'C (Root & Tuber)', 'D (Noodles)'))
b5 = st.selectbox('(5) Reason For Food Choice', ('A (Cheap)', 'B (Available)', 'C (Easy to Cook)', 'D (Taste)'))
b6 = st.selectbox('(6) Which of these food groups constitute your regular lunch?', ('A (Grains/cereals)', 'B (Legumes)', 'C (Root & Tuber)', 'D (Noodles)'))
b7 = st.selectbox('(7) Reason For Food Choice', ('A (Cheap)', 'B (Available)', 'C (Easy to Cook)', 'D (Taste)'))
b8 = st.selectbox('(8) Which of these food groups constitute your regular dinner?', ('A (Grains/cereals)', 'B (Legumes)', 'C (Root & Tuber)', 'D (Noodles)'))
b9 = st.selectbox('(9) Reason For Food Choice', ('A (Cheap)', 'B (Available)', 'C (Easy to Cook)', 'D (Taste)'))
b10 = st.selectbox('(10) How often do you take snacks?', ('A (Every day)', 'B (Twice a week)', 'C (Thrice a day)', 'D (Not sure)'))
b11 = st.selectbox('(11) What type of snacks do you consume regularly ', (' A (Soft drink/malt  & doughnut/ pie/bun)', 'B (Soft drink/malt & biscuits)',
'C (Banana & groundnut / Cucumber &groundnut)', 'D (Garri, sugar  & groundnut/Garri & salt)'))
b12 = st.selectbox('(12) Reason for choice of snack', ('A (Cheap)', 'B (Available)', 'C (Taste)', 'D (Not sure)'))
b13 = st.selectbox('(13) How often do you eat fruits and vegetables? ', ('A (Every day)', 'B (Twice a week)', 'C (Thrice a day)', 'D (Not sure)'))
b14 = st.selectbox('(14) What type of  fruits and vegetables do you consume regularly ', ('A (Citrus fruits & leafy veg.)', 'B (Yellow/orange coloured fruits &veg.)', 
'C (Fruits and veg. in season)', 'D (None)'))
b15 = st.selectbox('(15) Reason for choice of fruits and vegetable', ('A (Cheap)', 'B (Available)', 'C (Taste)', 'D (Not sure)'))
b16 = st.selectbox('(16) If your answer to question 14 is None, Why?', ('A (Causes stomach cramp)', 'B (Causes frequent stooling) ', 'C (Increases my ulcer pain)', 'D (Dislike fruits and veg.)'))

st.text("___"*100)

st.subheader("SECTION C: Anthropometric Measurement")
c1 = st.number_input('Weight (KG)', min_value=0)
c2 = st.number_input('Height (M)', min_value=0)



if st.button("Submit Questionnare"):
    try:
        hei = c2 * c2
        bmi = c1 / hei
    except:
        bmi = 0

    if firebase_admin._DEFAULT_APP_NAME not in firebase_admin._apps:
        cred_obj = firebase_admin.credentials.Certificate('qdataapp-firebase.json')
        firebase_admin.initialize_app(cred_obj, {
        'databaseURL':"https://qdataapp-default-rtdb.firebaseio.com/"
        })

    
    ref2 = db.reference("/Users/kycSunj6OASdyDgWnL6FTdEQbh23/Questionnaires/UDpEOQgo/Count")
    a = ref2.get()
    n_a = int(a) + 1



    myData = {
        generateRandom() : {
            "Age": a1[0],
            "Sex": a2[0],
            "Sponsor": a3[0],
            "Edu or Qualification of Sponsor" : a4[0],
            "Sponsor's Occupation" : a4[0],
            "Family income (monthly)" : a6[0],
            "Religion" : a7[0],
            "Family Size" : a8[0],
            "How often do you purchase food" : b1[0],
            "How much do you spend on food in a month" : b2[0],
            "How many times do you eat in a day" : b3[0],
            "Which of these food groups constitute your regular breakfast" : b4[0],
            "Reason For Food Choice (Breakfast)" : b5[0],
            "Which of these food groups constitute your regular lunch" : b6[0],
            "Reason For Food Choice (Lunch)" : b7[0],
            "Which of these food groups constitute your regular dinner" : b8[0],
            "Reason For Food Choice" : b9[0],
            "How often do you take snacks" : b10[0],
            "What type of snacks do you consume regularly" : b11[0],
            "Reason for choice of snack" : b12[0],
            "How often do you eat fruits and vegetables" : b13[0],
            "What type of  fruits and vegetables do you consume regularly" : b14[0],
            "Reason for choice of fruits and vegetable" : b15[0],
            "If your answer to question 14 is None, Why" : b16[0],
            "height" : c1,
            "weight" : c2
        }
    }

    with open("jsondata.json", "w") as sd:
        json.dump(myData, sd)

    with open("jsondata.json", "w") as sd:
                json.dump(myData, sd)

    ref2.set(str(n_a))


    ref = db.reference("/Users/kycSunj6OASdyDgWnL6FTdEQbh23/Questionnaires/UDpEOQgo/CollectedData/" + generateRandom())
    with open("jsondata.json", "r") as f:
        file_contents = json.load(f)

    for key, value in file_contents.items():
        ref.set(value)

        

    st.success('Data added Successfully')  
    st.info('Your BMI is --> ' + str(bmi))

