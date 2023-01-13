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


st.title("Questionnaire for Dietary Diversity of Women 15-49 years (24 hr open recall method)")

st.text("___"*100)

st.subheader("Section A: Personal Data")

st.selectbox('Age', ('A (18-25)', 'B (26-35)', 'C (36-50)', 'D ( > 50)'))
st.selectbox('Education Qualification', ('A (FSLC)', 'B (SSCE)', 'C (graduate)', 'D (none)'))
st.selectbox('Marital Status', ('A (single)', 'B (married)', 'C (divorced)', 'D (widow)'))
st.selectbox('Occupation', ('A (Civil servant)', 'B (Trader)', 'C (Farmer)', 'D (Other)'))
st.selectbox('Income Level', ('A ( ≤ N50,000)', 'B (N60,000-N80,000)', 'C (N90,000 -N110,000)', 'D ( ≥ N120,000)'))
st.selectbox('Religion', ('A (Traditional religion)', 'B (Christianity)', 'C (Islam)', 'D (other)'))
st.selectbox('Family Size', ('A (2-3)', 'B (4-5)', 'C (6-9)', 'D ( > 9)'))

st.text("___"*100)  

st.subheader("SECTION B: Minimum Dietary Diversity- women ")
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

    
    ref2 = db.reference("/Users/g4WDG6gkkhPpTOeoP3szUJf9L603/Questionnaires/SENEVArpp025/Count")
    a = ref2.get()
    n_a = int(a) + 1

    myData = {
        generateRandom() : {
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


    ref = db.reference("/Users/g4WDG6gkkhPpTOeoP3szUJf9L603/Questionnaires/SENEVArpp025/CollectedData/" + generateRandom())
    with open("jsondata.json", "r") as f:
        file_contents = json.load(f)

    for key, value in file_contents.items():
        ref.set(value)

        

    st.success('Data added Successfully')  

