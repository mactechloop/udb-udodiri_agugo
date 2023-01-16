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


st.title("""Food Consumption Pattern on Anthropometric (BMI &Waist-To-Hip-Ratio) Status of Subjects/Respondents
""")

st.text("___"*100)

st.subheader(""" Dear madam/sir,
""")

st.write(""" In partial fulfillment of the requirement for the award of bachelor in science (B.Sc.) in human nutrition and dietetics, 
I ……. with registration number …… is conducting a study on “Food Consumption Pattern of ……….. on Anthropometric Status of…..”. 
Information obtained from this questionnaire is strictly for research purpose and will be kept confidential. 
Please, answer all questions in each section below
""")

st.write("""
    Thank you for your attention. 
""")

st.text("___"*100)


st.subheader("SECTION A: Socio-Demographic Characteristics of Respondents")

a1 = st.selectbox('Age', ('A (18-25)', 'B (26-35)', 'C (36-50)', 'D ( > 50)'))
a2 = st.selectbox('Sex', ('A (male)', 'B (female)', 'C (other)'))
a3 = st.selectbox('Marital Status', ('A (single)', 'B (married)', 'C (divorced)', 'D (widow)'))
a4 = st.selectbox('Education Qualification', ('A (FSLC)', 'B (SSCE)', 'C (graduate)', 'D (none)'))
a5 = st.selectbox('Religion', ('A (Traditional religion)', 'B (Christianity)', 'C (Islam)', 'D (other)'))
a6 = st.selectbox('Family Size', ('A (2-3)', 'B (4-5)', 'C (6-9)', 'D ( > 9)'))

st.text("___"*100)

st.subheader("SECTION B: Food Consumption Pattern of Respondents")
st.write("""
	How often do you consume the following foods in the table below;
""")

st.text("___"*100)

st.write("""
##### Diary Product
""")

b1 = st.selectbox('Milk', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
b2 = st.selectbox('Yoghurt', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
b3 = st.selectbox('Cheese', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))

st.text("___"*100)

st.write("""
##### Fats
""")

c1 = st.selectbox('Butter', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
c2 = st.selectbox('Vegetable Oil', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
c3 = st.selectbox('Palm Oil', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
c4 = st.selectbox('Margarine ', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))

st.text("___"*100)

st.write("""
##### Meat / fish/poultry 
""")

d1 = st.selectbox('Beef', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
d2 = st.selectbox('Pork', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
d3 = st.selectbox('Chicken', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
d4 = st.selectbox('Turkey ', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
d5 = st.selectbox('Ice fish', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
d6 = st.selectbox('Catfish', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
d7 = st.selectbox('Sea fish', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
d8 = st.selectbox('Crayfish ', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
d9 = st.selectbox('Prawn', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
d10 = st.selectbox('Stock fish', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))

st.text("___"*100)

st.write("""
##### Processed food/ grains						
""")

e1 = st.selectbox('Biscuits', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
e2 = st.selectbox('Bread', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
e3 = st.selectbox('Noodles', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
e4 = st.selectbox('Spaghetti ', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
e5 = st.selectbox('Rice', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
e6 = st.selectbox('Oat', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
e7 = st.selectbox('Maize', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
e8 = st.selectbox('Maize pudding / pap ', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))


st.text("___"*100)

st.write("""
##### Roots and Tuber						
""")

f1 = st.selectbox('Fufu', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
f2 = st.selectbox('Garri', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
f3 = st.selectbox('Yam', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
f4 = st.selectbox('African salad ', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
f5 = st.selectbox('Cocoyam', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
f6 = st.selectbox('Sweet potatoe', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
f7 = st.selectbox('Irish potatoe', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
f8 = st.selectbox('Plantain', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))

st.text("___"*100)

st.write("""
##### Alcohol/ Sweetened drinks 						
""")

g1 = st.selectbox('Soft drinks/malt', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
g2 = st.selectbox('Can juice', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
g3 = st.selectbox('Sachet alcoholic bitters', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
g4 = st.selectbox('Squadron ', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
g5 = st.selectbox('Red wine', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))


st.text("___"*100)

st.write("""
##### Legumes 						
""")

h1 = st.selectbox('Peas', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
h2 = st.selectbox('Beans/pudding/akara', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
h3 = st.selectbox('Green beans', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
h4 = st.selectbox('Soybean ', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
h5 = st.selectbox('Groundnut', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))


st.text("___"*100)

st.write("""
##### Vitamin A rich fruits and vegetables 						
""")

i1 = st.selectbox('Water melon', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
i2 = st.selectbox('Pawpaw', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
i3 = st.selectbox('Carrot', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
i4 = st.selectbox('Fresh tomatoes ', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
i5 = st.selectbox('Yellow Pepper', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))


st.text("___"*100)

st.write("""
##### Other vegetables/fruits					
""")

j1 = st.selectbox('Green leafy vegetables', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
j2 = st.selectbox('Pineapple', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
j3 = st.selectbox('Cucumber', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
j4 = st.selectbox('Banana ', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
j5 = st.selectbox('Tangerine', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
j6 = st.selectbox('Water leaf', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
j7 = st.selectbox('Bitter leaf', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
j8 = st.selectbox('Veg. for black soup', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
j9 = st.selectbox('Avocado', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
j10 = st.selectbox('Orange', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
j11 = st.selectbox('Green/red pepper', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
j12 = st.selectbox('Onions ', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
j13 = st.selectbox('Radish', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
j14 = st.selectbox('Beetroot', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
j15 = st.selectbox('Okra ', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))

st.text("___"*100)

st.write("""
##### Spices/nuts/sees 						
""")

k1 = st.selectbox('Ginger', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
k2 = st.selectbox('Garlic', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
k3 = st.selectbox('Scent leaf', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
k4 = st.selectbox('Utazi  (bitter local spice)', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
k5 = st.selectbox('Coconut', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
k6 = st.selectbox('Tigernut', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))
k7 = st.selectbox('Pumpkin', ('A (Once a day)', 'B (2-3 times daily)', 'C (2-3 times a week)', 'D (4-5 times a week)', 'D (6-7 times a week)', 'E (None)'))


st.text("___"*100)

st.subheader("SECTION C: Anthropometric Indices of Respondents")
l1 = st.number_input('Height (CM)', min_value=0)
l2 = st.number_input('Weight (CM)', min_value=0)
l3 = st.number_input('Waist circumference (CM)', min_value=0)
l4 = st.number_input('Hip circumference (CM)', min_value=0)

if st.button("Submit Questionnare"):

    try:
        bmi = l2 / l1
        wthr = l3 / l4
    except:
        bmi = 0
        wthr = 0

    if firebase_admin._DEFAULT_APP_NAME not in firebase_admin._apps:
        cred_obj = firebase_admin.credentials.Certificate('qdataapp-firebase.json')
        firebase_admin.initialize_app(cred_obj, {
        'databaseURL':"https://qdataapp-default-rtdb.firebaseio.com/"
        })

    
    ref2 = db.reference("/Users/kycSunj6OASdyDgWnL6FTdEQbh23/Questionnaires/UD2XG6RM/Count")
    a = ref2.get()
    n_a = int(a) + 1

    myData = {
        generateRandom() : {
            "Age": a1[0],
            "Sex": a2[0],
            "Marital Status": a3[0],
            "Education Qualification" : a4[0],
            "Religion" : a5[0],
            "Family Size" : a6[0],
            "Milk" : b1[0],
            "Yoghurt" : b2[0],
            "Cheese" : b3[0],
            "Butter" : c1[0],
            "Vegetable Oil" : c2[0],
            "Palm Oil" : c3[0],
            "Margarine" : c4[0],
            "Beef" : d1[0],
            "Pork" : d2[0],
            "Chicken" : d3[0],
            "Turkey" : d4[0],
            "Ice Fish" : d5[0],
            "Cat Fish" : d6[0],
            "Sea Fish" : d7[0],
            "Crayfish" : d8[0],
            "Prawn" : d9[0],
            "Stock Fish" : d10[0],
            "Biscuits" : e1[0],
            "Bread" : e2[0],
            "Noodles" : e3[0],
            "Spaghetti" : e4[0],
            "Rice" : e5[0],
            "Oat" : e6[0],
            "Maize" : e7[0],
            "Maize pudding or Pap" : e8[0],
            "Fufu" : f1[0],
            "Garri" : f2[0],
            "Yam" : f3[0],
            "African Salad" : f3[0],
            "Cocoyam" : f5[0],
            "Sweet Potatoe" : f6[0],
            "Irish Potatoe" : f7[0],
            "Plantain" : f8[0],
            "Soft drinks or malt" : g1[0],
            "Can juice" : g2[0],
            "Sachet alcoholic bitters" : g3[0],
            "Squadron" : g4[0],
            "Red Wine" : g5[0],
            "Peas" : h1[0],
            "Beans or pudding or akara" : h2[0],
            "Green Beans" : h3[0],
            "Soybean" : h4[0],
            "Soybean" : h5[0],
            "Water Melon" : i1[0],
            "Pawpaw" : i2[0],
            "Carrot" : i3[0],
            "Fresh Tomatoe" : i4[0],
            "Yellow Pepper" : i5[0],
            "Green leafy vegetables" : j1[0],
            "Pineapple" : j2[0],
            "Cucumber" : j3[0],
            "Banana" : j4[0],
            "Tangerine" : j5[0],
            "Water Leaf" : j6[0],
            "Bitter Leaf" : j7[0],
            "Vegetable for black soup" : j8[0],
            "Avocado" : j9[0],
            "Orange" : j10[0],
            "Green or red pepper" : j11[0],
            "Onions" : j12[0],
            "Raddish" : j13[0],
            "Beetroot" : j14[0],
            "Okra" : j15[0],
            "Ginger" : k1[0],
            "Garlic" : k2[0],
            "Scent Leaf" : k3[0],
            "Utazi  bitter local spice" : k4[0],
            "Coconut" : k5[0],
            "Tigernut" : k6[0],
            "Pumpkin" : k7[0],
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


    ref = db.reference("/Users/kycSunj6OASdyDgWnL6FTdEQbh23/Questionnaires/UD2XG6RM/CollectedData/" + generateRandom())
    with open("jsondata.json", "r") as f:
        file_contents = json.load(f)

    for key, value in file_contents.items():
        ref.set(value)

        

    st.success('Data added Successfully')  
    st.info('Your BMI is --> ' + str(bmi) + 'kg/m2')
    st.info('Your Waist-to-hip-ratio is --> ' + str(wthr))

