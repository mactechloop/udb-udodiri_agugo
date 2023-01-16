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

st.title("Food Access among Students Households (Weighed Food Intake)")

st.text("___"*100)

st.write("""
## Dear madam/sir,
""")

st.write("""
    In partial fulfillment of the requirement for the award of bachelor in science (B.Sc.) in human nutrition and dietetics, 
    I ……. with registration number …… is conducting a study on ‘Food Access among Student Households using Weighed Food Intake Method …..”. 
    Information obtained from this questionnaire is strictly for research purpose and will be kept confidential. 
    Please, answer all questions in each section below.

""")

st.write("""
    Thank you for your attention. 
""")


st.text("___"*100)

st.subheader("Section A: Personal Data")

a1 = st.selectbox('Age', ('A (15-24)', 'B (25-34)', 'C (35-44)', 'D (45-59)'))
a2 = st.selectbox('Sex', ('A (male)', 'B (female)', 'C (other)'))
a3 = st.selectbox('Level', ('A (100)', 'B (200)', 'C (300)', 'D (400-500)'))
a4 = st.selectbox('Household Size', ('A (2-3)', 'B (4-5)', 'C ( > 5)', 'D (1)'))

st.text("___"*100)

st.subheader("Section B: Weighed Food Intake")
st.write("""
 Weight of food consumed by respondents at the household
""")

st.text("___"*100)

st.write("""
##### Diary Product
""")

b1 = st.selectbox('Milk', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
b2 = st.selectbox('Yoghurt', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
b3 = st.selectbox('Cheese', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))

st.text("___"*100)

st.write("""
##### Fats
""")

c1 = st.selectbox('Butter', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
c2 = st.selectbox('Vegetable Oil', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
c3 = st.selectbox('Palm Oil', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
c4 = st.selectbox('Margarine ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))

st.text("___"*100)

st.write("""
##### Meat / fish/poultry 
""")

d1 = st.selectbox('Beef', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
d2 = st.selectbox('Pork', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
d3 = st.selectbox('Chicken', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
d4 = st.selectbox('Turkey ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
d5 = st.selectbox('Ice fish', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
d6 = st.selectbox('Catfish', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
d7 = st.selectbox('Sea fish', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
d8 = st.selectbox('Crayfish ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
d9 = st.selectbox('Prawn', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
d10 = st.selectbox('Stock fish', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))

st.text("___"*100)

st.write("""
##### Processed food/ grains						
""")

e1 = st.selectbox('Biscuits', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
e2 = st.selectbox('Bread', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
e3 = st.selectbox('Noodles', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
e4 = st.selectbox('Spaghetti ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
e5 = st.selectbox('Rice', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
e6 = st.selectbox('Oat', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
e7 = st.selectbox('Maize', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
e8 = st.selectbox('Maize pudding/ pap ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))


st.text("___"*100)

st.write("""
##### Roots and Tuber						
""")

f1 = st.selectbox('Fufu', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
f2 = st.selectbox('Garri', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
f3 = st.selectbox('Yam', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
f4 = st.selectbox('African salad ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
f5 = st.selectbox('Cocoyam', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
f6 = st.selectbox('Sweet potatoe', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
f7 = st.selectbox('Irish potatoe', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
f8 = st.selectbox('Plantain', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))

st.text("___"*100)

st.write("""
##### Alcohol/ Sweetened drinks 						
""")

g1 = st.selectbox('Soft drinks/malt', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
g2 = st.selectbox('Can juice', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
g3 = st.selectbox('Sachet alcoholic bitters  ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
g4 = st.selectbox('Squadron ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
g5 = st.selectbox('Red wine', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))


st.text("___"*100)

st.write("""
##### Legumes 						
""")

h1 = st.selectbox('Peas', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
h2 = st.selectbox('Beans/pudding/ akara', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
h3 = st.selectbox('Green beans', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
h4 = st.selectbox('Soybean ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
h5 = st.selectbox('Groundnut', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))


st.text("___"*100)

st.write("""
##### Vitamin A rich fruits and vegetables 						
""")

i1 = st.selectbox('Water melon', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
i2 = st.selectbox('Pawpaw', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
i3 = st.selectbox('Carrot', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
i4 = st.selectbox('Fresh tomatoes ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
i5 = st.selectbox('Yellow Pepper', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))


st.text("___"*100)

st.write("""
##### Other vegetables/fruits					
""")

j1 = st.selectbox('Green leafy vegetables', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
j2 = st.selectbox('Pineapple', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
j3 = st.selectbox('Cucumber', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
j4 = st.selectbox('Banana ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
j5 = st.selectbox('Tangerine', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
j6 = st.selectbox('Water leaf', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
j7 = st.selectbox('Bitter leaf', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
j8 = st.selectbox('Veg. for black soup ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
j9 = st.selectbox('Avocado', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
j10 = st.selectbox('Orange', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
j11 = st.selectbox('Green/red pepper', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
j12 = st.selectbox('Onions ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
j13 = st.selectbox('Radish', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
j14 = st.selectbox('Beetroot', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
j15 = st.selectbox('Okra ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))

st.text("___"*100)

st.write("""
##### Spices/nuts/sees 						
""")

k1 = st.selectbox('Ginger', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
k2 = st.selectbox('Garlic', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
k3 = st.selectbox('Scent leaf', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
k4 = st.selectbox('Utazi  (bitter local spice) ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
k5 = st.selectbox('Coconut', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
k6 = st.selectbox('Tiger nut', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
k7 = st.selectbox('Pumpkin', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))

if st.button("Submit Questionnare"):
    if firebase_admin._DEFAULT_APP_NAME not in firebase_admin._apps:
        cred_obj = firebase_admin.credentials.Certificate('qdataapp-firebase.json')
        firebase_admin.initialize_app(cred_obj, {
        'databaseURL':"https://qdataapp-default-rtdb.firebaseio.com/"
        })

    
    ref2 = db.reference("/Users/kycSunj6OASdyDgWnL6FTdEQbh23/Questionnaires/UD mmzBZ8/Count")
    a = ref2.get()
    n_a = int(a) + 1

    myData = {
        generateRandom() : {
            "Age": a1[0],
            "Sex": a2[0],
            "Level ": a3[0],
            "Household" : a4[0],
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
            "Groundnut" : h5[0],
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
        }
    }

    with open("jsondata.json", "w") as sd:
        json.dump(myData, sd)

    with open("jsondata.json", "w") as sd:
                json.dump(myData, sd)

    ref2.set(str(n_a))


    ref = db.reference("/Users/kycSunj6OASdyDgWnL6FTdEQbh23/Questionnaires/UD mmzBZ8/CollectedData/" + generateRandom())
    with open("jsondata.json", "r") as f:
        file_contents = json.load(f)

    for key, value in file_contents.items():
        ref.set(value)

        

    st.success('Data added Successfully')  

