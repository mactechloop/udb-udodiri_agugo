import streamlit as st
import json
import csv
import pandas as pd
import firebase_admin
from firebase_admin import db
import string
import random

def listToString(s):
 
    # initialize an empty string
    str1 = ""
 
    # traverse in the string
    for ele in s:
        str1 += ele
 
    # return string
    return str1

def make_json(csvFilePath, jsonFilePath):
    data = {}

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
       
        for rows in csvReader:
            key = rows['Sample']
            data[key] = rows
 

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
 

def generateRandom():
    N = 7
    res = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k=N))

    return res

st.title("Sensory evaluation form")

st.text("___"*100)

st.write("""
    Kindly evaluate the following samples using the scale provided below. 
    Information generated from this exercise is strictly for research purpose. 
    Individual perceptions on the texture (hand feel), appearance (color), 
    aroma and general acceptability as well as contributions (comment) on what else you 
    feel about the samples will be most welcomed.

    Wash your hands in the basin of water provided after evaluating each sample to avoid bias.
""")

st.text("___"*100)

st.subheader("""Instruction: Rate samples using  the scale provided below""")

st.text("___"*100)
st.text("""""""9 –point Hedonic ranking scale""""""")
st.text("""

9- liked extremely
8-liked very much
7- liked moderately
6- liked slightly
5- Neither liked nor disliked
4-disliked slightly
3-disliked moderately
2-disliked very much
1-disliked extremely 

""")

st.text("___"*100)

point_her = ["null", "disliked extremely", "disliked very much", "disliked moderately",
                "disliked slightly", "Neither liked nor disliked", "liked slightly", "liked moderately",
                        "liked very much", "liked extremely"]

st.subheader("Sample A")
a1 = st.slider('Taste for Sample(A)', 1, 9)
a2 = st.slider('Texture for Sample(A)', 1, 9)
a3 = st.slider('Appearance for Sample(A)', 1, 9)
a4 = st.slider('Aroma for Sample(A)', 1, 9)
a5 = st.slider('General Acceptability for Sample(A)', 1, 9)

st.text("___"*100)

st.subheader("Sample B")
b1 = st.slider('Taste for Sample(B)', 1, 9)
b2 = st.slider('Texture for Sample(B)', 1, 9)
b3 = st.slider('Appearance for Sample(B)', 1, 9)
b4 = st.slider('Aroma for Sample(B)', 1, 9)
b5 = st.slider('General Acceptability for Sample(B)', 1, 9)

st.text("___"*100)

st.subheader("Sample C")
c1 = st.slider('Taste for Sample(C)', 1, 9)
c2 = st.slider('Texture for Sample(C)', 1, 9)
c3 = st.slider('Appearance for Sample(C)', 1, 9)
c4 = st.slider('Aroma for Sample(C)', 1, 9)
c5 = st.slider('General Acceptability for Sample(C)', 1, 9)

st.text("___"*100)

st.subheader("Sample D")
d1 = st.slider('Taste for Sample(D)', 1, 9)
d2 = st.slider('Texture for Sample(D)', 1, 9)
d3 = st.slider('Appearance for Sample(D)', 1, 9)
d4 = st.slider('Aroma for Sample(D)', 1, 9)
d5 = st.slider('General Acceptability for Sample(D)', 1, 9)

st.text("___"*100)

st.subheader("Sample E")
e1 = st.slider('Taste for Sample(E)', 1, 9)
e2 = st.slider('Texture for Sample(E)', 1, 9)
e3 = st.slider('Appearance for Sample(E)', 1, 9)
e4 = st.slider('Aroma for Sample(E)', 1, 9)
e5 = st.slider('General Acceptability for Sample(E)', 1, 9)


if st.button("Submit Questionnare"):
    if firebase_admin._DEFAULT_APP_NAME not in firebase_admin._apps:
        cred_obj = firebase_admin.credentials.Certificate('qdataapp-firebase.json')
        firebase_admin.initialize_app(cred_obj, {
        'databaseURL':"https://qdataapp-default-rtdb.firebaseio.com/"
        })

    try:
        ref2 = db.reference("/Users/kycSunj6OASdyDgWnL6FTdEQbh23/Questionnaires/UDBcapnI/Count")
        a = ref2.get()
        print(type(a))
        n_a = int(a) + 1

        myData = {
            generateRandom() : {
                "Sample": "1, 2, 3, 4, 5",
                "Taste": str([(a1), (b1), (c1), (d1), (e1)]),
                "Texture": str([(a2), (b2), (c2), (d2), (e2)]),
                "Appearance": str([(a3), (b3), (c3), (d3), (e3)]),
                "Aroma": str([(a4), (b4), (c4), (d4), (e4)]),
                "General Acceptability": str([(a5), (b5), (c5), (d5), (e5)]),
                "Pendant":  str([int(n_a), int(n_a), int(n_a), int(n_a), int(n_a)])
            }
        }



        with open("jsondata.json", "w") as sd:
                    json.dump(myData, sd)

        ref2.set(str(n_a))


        ref = db.reference("/Users/kycSunj6OASdyDgWnL6FTdEQbh23/Questionnaires/UDBcapnI/CollectedData/" + generateRandom())
        with open("jsondata.json", "r") as f:
            file_contents = json.load(f)

        for key, value in file_contents.items():
            ref.set(value)

        

        st.success('Data added Successfully')   
    except Exception:
        st.error('An Error Occurred')
    


