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


st.title("Dietary Diversity Assessment (24 Hr Open Recall Method)")

st.text("___"*100)

st.write("""
## Dear Respondents,
""")

st.write("""
This is a Community/Public Health Nutrition Research intended to gather information on the 
“Nutritional Status and Prevalence of Malnutrition among IDPs (6-60years) in Nigeria and Effect of Nutrition Education on Eating Behaviour of target Population”
In line with the research objectives, data on dietary diversity of households is required. 
Information obtained from this questionnaire is strictly for research purpose and will be kept confidential. 
Please, answer all questions in each section below.
""")

st.write("""
    Thank you for your attention. 
""")

st.text("___"*100)

st.subheader("Section A: Personal data of household head/representative ")

a1 = st.selectbox('Age', ('A (15-24)', 'B (25-34)', 'C (35-44)', 'D (45-59)'))
a2 = st.selectbox('Education Qualification', ('A (Primary)', 'B (SSCE)', 'C (undergraduate)', 'D (graduate)'))
a3 = st.selectbox('Marital Status', ('A (married)', 'B (single)', 'C (divorced)', 'D (widow)'))
a4 = st.selectbox('Occupation', ('A (Civil servant)', 'B (Trader)', 'C (Farmer)', 'D (Other)'))

st.text("___"*100)  

st.subheader("Section B: Household Dietary Diversity Record ")
st.write("""
	In the past 24 hours, did you consume any of the following foods?
""")


st.text("___"*100)

st.write("""
##### Grains, roots, tuber
""")


a = st.selectbox("""
Rice, maize, yam, cocoyam, garri, fufu, 
pounded yam, maize pudding, pap, Irish potato, 
sweet potato, plantain, porridge, bread, cake,
""", ('A (Yes)', 'B (No)'))
aa = a[0]

st.text("___"*100)

st.write("""
##### Pulses
""")


b = st.selectbox("""
Beans, soybean, peas, traditional beans,
 kidney beans, jack beans, green beans
""", ('A (Yes)', 'B (No)'))

st.text("___"*100)


st.write("""
##### Nuts and seeds
""")


c = st.selectbox("""
Coconut, groundnut, tiger nut, cashew nuts, local nuts
""", ('A (Yes)', 'B (No)'))

st.text("___"*100)

st.write("""
##### Diary
""")

d = st.selectbox("""
Yoghurt, ice cream, cheese, full cream milk, skim milk, milk shake,   
""", ('A (Yes)', 'B (No)'))

st.text("___"*100)

st.write("""
##### Meat, fish, poultry
""")


e = st.selectbox("""
Beef, pork, turkey, chicken, fish, crayfish, crab, stock fish, prawn, shrimps,    
""", ('A (Yes)', 'B (No)'))

st.text("___"*100)

st.write("""
##### Eggs
""")

f = st.selectbox("""
Egg of any type
""", ('A (Yes)', 'B (No)'))

st.text("___"*100)

st.write("""
##### Dark leafy greens and vegetables
""")

g = st.selectbox("""
Amaranths, pumpkin leave, water leaf,  bitter leaf, veg. for black soup, other traditional vegetable 
""", ('A (Yes)', 'B (No)'))

st.text("___"*100)

st.write("""
##### Other vitamin-A rich foods and vegetables
""")

h = st.selectbox("""
Fresh tomatoes, yellow pepper, paw-paw, carrot, watermelon, orange flesh sweet potato,
""", ('A (Yes)', 'B (No)'))

st.text("___"*100)

st.write("""
##### Other vegetables
""")


i = st.selectbox("""
Cabbage, lettuce, cucumber, radish, beetroot, onions, okra, 
""", ('A (Yes)', 'B (No)'))

st.text("___"*100)

st.write("""
##### Other fruits 
""")


j = st.selectbox("""
Oranges, tangerine, cashew, avocado, grape fruits, 
English pear, apple, pineapple, grape, lime, lemon, any traditional fruit, banana, 
""", ('A (Yes)', 'B (No)'))

st.text("___"*100)

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
            "Age" : a1[0],
            "Education Qualification" : a2[0],
            "Marital Status" : a3[0],
            "Occupation" : a4[0],
            "Grains roots tuber": aa,
            "Pulses": b[0],
            "Nuts and seeds ": c[0],
            "Dairy " : d[0],
            "Milk" : e[0],
            "Meat, fish, poultry " : f[0],
            "Dark leafy greens and vegetables" : g[0],
            "Other vitamin-A rich foods and vegetables" : h[0],
            "Other vegetables" : i[0],
            "Other fruits " : j[0]
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

