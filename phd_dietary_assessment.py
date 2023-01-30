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


st.title("""Dietary Assessment Questionnaire (24 hour recall and weighed food intake)
""")

st.text("___"*100)

st.subheader(""" Dear Respondents,
""")

st.write(""" This is a Community/Public Health Nutrition Research intended to gather information on the 
“Nutritional Status and Prevalence of Malnutrition among IDPs (6-60years) in Nigeria and Effect of Nutrition Education on Eating Behaviour of target Population”
In line with the research objectives, data on dietary habit of households is required. 
Information obtained from this questionnaire is strictly for research purpose and will be kept confidential. 
Please, answer all questions in each section below.
""")

st.write("""
    Thank you for your attention. 
""")

st.text("___"*100)
state = st.selectbox('State', ('Abuja', 'Bayelsa', 'Brono'))

st.text("___"*100)

st.subheader("Section A: 24 hour dietary recall at household level")
st.write("""
	In the past 24 hours, did your household consume any of the following foods?
""")

st.text("___"*100)

st.write("""
##### Diary Product
""")

b1 = st.selectbox('Milk', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
b2 = st.selectbox('Yoghurt', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
b3 = st.selectbox('Cheese', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))

st.text("___"*100)

st.write("""
##### Fats
""")

c1 = st.selectbox('Butter', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
c2 = st.selectbox('Vegetable Oil', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
c3 = st.selectbox('Palm Oil', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
c4 = st.selectbox('Margarine ', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))

st.text("___"*100)

st.write("""
##### Meat / fish/poultry 
""")

d1 = st.selectbox('Beef', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
d2 = st.selectbox('Pork', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
d3 = st.selectbox('Chicken', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
d4 = st.selectbox('Turkey ', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
d5 = st.selectbox('Ice fish', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
d6 = st.selectbox('Catfish', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
d7 = st.selectbox('Sea fish', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
d8 = st.selectbox('Crayfish ', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
d9 = st.selectbox('Prawn', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
d10 = st.selectbox('Stock fish', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))

st.text("___"*100)

st.write("""
##### Processed food/ grains						
""")

e1 = st.selectbox('Biscuits', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
e2 = st.selectbox('Bread', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
e3 = st.selectbox('Noodles', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
e4 = st.selectbox('Spaghetti ', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
e5 = st.selectbox('Rice', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
e6 = st.selectbox('Oat', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
e7 = st.selectbox('Maize', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
e8 = st.selectbox('Maize pudding / pap ', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))


st.text("___"*100)

st.write("""
##### Roots and Tuber						
""")

f1 = st.selectbox('Fufu', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
f2 = st.selectbox('Garri', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
f3 = st.selectbox('Yam', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
f4 = st.selectbox('African salad ', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
f5 = st.selectbox('Cocoyam', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
f6 = st.selectbox('Sweet potatoe', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
f7 = st.selectbox('Irish potatoe', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
f8 = st.selectbox('Plantain', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))

st.text("___"*100)

st.write("""
##### Alcohol/ Sweetened drinks 						
""")

g1 = st.selectbox('Soft drinks/malt', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
g2 = st.selectbox('Can juice', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
g3 = st.selectbox('Sachet alcoholic bitters', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
g4 = st.selectbox('Squadron ', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
g5 = st.selectbox('Red wine', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))


st.text("___"*100)

st.write("""
##### Legumes 						
""")

h1 = st.selectbox('Peas', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
h2 = st.selectbox('Beans/pudding/akara', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
h3 = st.selectbox('Green beans', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
h4 = st.selectbox('Soybean ', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
h5 = st.selectbox('Groundnut', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))


st.text("___"*100)

st.write("""
##### Vitamin A rich fruits and vegetables 						
""")

i1 = st.selectbox('Water melon', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
i2 = st.selectbox('Pawpaw', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
i3 = st.selectbox('Carrot', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
i4 = st.selectbox('Fresh tomatoes ', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
i5 = st.selectbox('Yellow Pepper', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))


st.text("___"*100)

st.write("""
##### Other vegetables/fruits					
""")

j1 = st.selectbox('Green leafy vegetables', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
j2 = st.selectbox('Pineapple', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
j3 = st.selectbox('Cucumber', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
j4 = st.selectbox('Banana ', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
j5 = st.selectbox('Tangerine', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
j6 = st.selectbox('Water leaf', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
j7 = st.selectbox('Bitter leaf', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
j8 = st.selectbox('Veg. for black soup', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
j9 = st.selectbox('Avocado', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
j10 = st.selectbox('Orange', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
j11 = st.selectbox('Green/red pepper', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
j12 = st.selectbox('Onions ', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
j13 = st.selectbox('Radish', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
j14 = st.selectbox('Beetroot', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
j15 = st.selectbox('Okra ', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))

st.text("___"*100)

st.write("""
##### Spices/nuts/sees 						
""")

k1 = st.selectbox('Ginger', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
k2 = st.selectbox('Garlic', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
k3 = st.selectbox('Scent leaf', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
k4 = st.selectbox('Utazi  (bitter local spice)', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
k5 = st.selectbox('Coconut', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
k6 = st.selectbox('Tigernut', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))
k7 = st.selectbox('Pumpkin', ('A (Breakfast)', 'B (Launch)', 'C (Dinner)'))


st.text("___"*100)

st.subheader("Section B: Weighed food intake  ")
st.write("""
    Weight of food consumed by respondents at the household
""")

st.text("___"*100)

st.write("""
##### Diary Product
""")

bb1 = st.selectbox('Milk', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
bb2 = st.selectbox('Yoghurt', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
bb3 = st.selectbox('Cheese', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))

st.text("___"*100)

st.write("""
##### Fats
""")

cc1 = st.selectbox('Butter', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
cc2 = st.selectbox('Vegetable Oil', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
cc3 = st.selectbox('Palm Oil', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
cc4 = st.selectbox('Margarine ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))

st.text("___"*100)

st.write("""
##### Meat / fish/poultry 
""")

dd1 = st.selectbox('Beef', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
dd2 = st.selectbox('Pork', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
dd3 = st.selectbox('Chicken', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
dd4 = st.selectbox('Turkey ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
dd5 = st.selectbox('Ice fish', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
dd6 = st.selectbox('Catfish', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
dd7 = st.selectbox('Sea fish', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
dd8 = st.selectbox('Crayfish ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
dd9 = st.selectbox('Prawn', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
dd10 = st.selectbox('Stock fish', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))

st.text("___"*100)

st.write("""
##### Processed food/ grains						
""")

ee1 = st.selectbox('Biscuits', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
ee2 = st.selectbox('Bread', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
ee3 = st.selectbox('Noodles', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
ee4 = st.selectbox('Spaghetti ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
ee5 = st.selectbox('Rice', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
ee6 = st.selectbox('Oat', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
ee7 = st.selectbox('Maize', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
ee8 = st.selectbox('Maize pudding/ pap ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))


st.text("___"*100)

st.write("""
##### Roots and Tuber						
""")

ff1 = st.selectbox('Fufu', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
ff2 = st.selectbox('Garri', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
ff3 = st.selectbox('Yam', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
ff4 = st.selectbox('African salad ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
ff5 = st.selectbox('Cocoyam', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
ff6 = st.selectbox('Sweet potatoe', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
ff7 = st.selectbox('Irish potatoe', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
ff8 = st.selectbox('Plantain', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))

st.text("___"*100)

st.write("""
##### Alcohol/ Sweetened drinks 						
""")

gg1 = st.selectbox('Soft drinks/malt', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
gg2 = st.selectbox('Can juice', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
gg3 = st.selectbox('Sachet alcoholic bitters  ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
gg4 = st.selectbox('Squadron ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
gg5 = st.selectbox('Red wine', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))


st.text("___"*100)

st.write("""
##### Legumes 						
""")

hh1 = st.selectbox('Peas', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
hh2 = st.selectbox('Beans/pudding/ akara', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
hh3 = st.selectbox('Green beans', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
hh4 = st.selectbox('Soybean ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
hh5 = st.selectbox('Groundnut', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))


st.text("___"*100)

st.write("""
##### Vitamin A rich fruits and vegetables 						
""")

ii1 = st.selectbox('Water melon', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
ii2 = st.selectbox('Pawpaw', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
ii3 = st.selectbox('Carrot', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
ii4 = st.selectbox('Fresh tomatoes ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
ii5 = st.selectbox('Yellow Pepper', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))


st.text("___"*100)

st.write("""
##### Other vegetables/fruits					
""")

jj1 = st.selectbox('Green leafy vegetables', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
jj2 = st.selectbox('Pineapple', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
jj3 = st.selectbox('Cucumber', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
jj4 = st.selectbox('Banana ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
jj5 = st.selectbox('Tangerine', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
jj6 = st.selectbox('Water leaf', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
jj7 = st.selectbox('Bitter leaf', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
jj8 = st.selectbox('Veg. for black soup ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
jj9 = st.selectbox('Avocado', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
jj10 = st.selectbox('Orange', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
jj11 = st.selectbox('Green/red pepper', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
jj12 = st.selectbox('Onions ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
jj13 = st.selectbox('Radish', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
jj14 = st.selectbox('Beetroot', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
jj15 = st.selectbox('Okra ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))

st.text("___"*100)

st.write("""
##### Spices/nuts/sees 						
""")

kk1 = st.selectbox('Ginger', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
kk2 = st.selectbox('Garlic', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
kk3 = st.selectbox('Scent leaf', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
kk4 = st.selectbox('Utazi  (bitter local spice) ', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
kk5 = st.selectbox('Coconut', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
kk6 = st.selectbox('Tiger nut', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))
kk7 = st.selectbox('Pumpkin', ('A (5-20g/ml)', 'B (25-40 g/ml)', 'C (45-60 g/ml)', 'D (65-90g/ml)', 'E (100-300g/ml)', 'F ( > 300g/ml)'))




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
            'State' : state,
            "Milk A" : b1[0],
            "Yoghurt A" : b2[0],
            "Cheese A" : b3[0],
            "Butter A" : c1[0],
            "Vegetable Oil A" : c2[0],
            "Palm Oil A" : c3[0],
            "Margarine A" : c4[0],
            "Beef A" : d1[0],
            "Pork A" : d2[0],
            "Chicken A" : d3[0],
            "Turkey A" : d4[0],
            "Ice Fish A" : d5[0],
            "Cat Fish A" : d6[0],
            "Sea Fish A" : d7[0],
            "Crayfish A" : d8[0],
            "Prawn A" : d9[0],
            "Stock Fish A" : d10[0],
            "Biscuits A" : e1[0],
            "Bread A" : e2[0],
            "Noodles A" : e3[0],
            "Spaghetti A" : e4[0],
            "Rice A" : e5[0],
            "Oat A" : e6[0],
            "Maize A" : e7[0],
            "Maize pudding or Pap A" : e8[0],
            "Fufu A" : f1[0],
            "Garri A" : f2[0],
            "Yam A" : f3[0],
            "African Salad A" : f4[0],
            "Cocoyam A" : f5[0],
            "Sweet Potatoe A" : f6[0],
            "Irish Potatoe A" : f7[0],
            "Plantain A" : f8[0],
            "Soft drinks or malt A" : g1[0],
            "Can juice A" : g2[0],
            "Sachet alcoholic bitters A" : g3[0],
            "Squadron A" : g4[0],
            "Red Wine A" : g5[0],
            "Peas A" : h1[0],
            "Beans or pudding or akara A" : h2[0],
            "Green Beans A" : h3[0],
            "Soybean A" : h4[0],
            "Soybean A" : h5[0],
            "Water Melon A" : i1[0],
            "Pawpaw A" : i2[0],
            "Carrot A" : i3[0],
            "Fresh Tomatoe A" : i4[0],
            "Yellow Pepper A" : i5[0],
            "Green leafy vegetables A" : j1[0],
            "Pineapple A" : j2[0],
            "Cucumber A" : j3[0],
            "Banana A" : j4[0],
            "Tangerine A" : j5[0],
            "Water Leaf A" : j6[0],
            "Bitter Leaf A" : j7[0],
            "Vegetable for black soup A" : j8[0],
            "Avocado A" : j9[0],
            "Orange A" : j10[0],
            "Green or red pepper A" : j11[0],
            "Onions A" : j12[0],
            "Raddish A" : j13[0],
            "Beetroot A" : j14[0],
            "Okra A" : j15[0],
            "Ginger A" : k1[0],
            "Garlic A" : k2[0],
            "Scent Leaf A" : k3[0],
            "Utazi  bitter local spice A" : k4[0],
            "Coconut A" : k5[0],
            "Tigernut A" : k6[0],
            "Pumpkin A" : k7[0],
            "Milk B" : bb1[0],
            "Yoghurt B" : bb2[0],
            "Cheese B" : bb3[0],
            "Butter B" : cc1[0],
            "Vegetable Oil B" : cc2[0],
            "Palm Oil B" : cc3[0],
            "Margarine B" : cc4[0],
            "Beef B" : dd1[0],
            "Pork B" : dd2[0],
            "Chicken B" : dd3[0],
            "Turkey B" : dd4[0],
            "Ice Fish B" : dd5[0],
            "Cat Fish B" : dd6[0],
            "Sea Fish B" : dd7[0],
            "Crayfish B" : dd8[0],
            "Prawn B" : dd9[0],
            "Stock Fish B" : dd10[0],
            "Biscuits B" : ee1[0],
            "Bread B" : ee2[0],
            "Noodles B" : ee3[0],
            "Spaghetti B" : ee4[0],
            "Rice B" : ee5[0],
            "Oat B" : ee6[0],
            "Maize B" : ee7[0],
            "Maize pudding or Pap B" : ee8[0],
            "Fufu B" : ff1[0],
            "Garri B" : ff2[0],
            "Yam B" : ff3[0],
            "African Salad B" : ff4[0],
            "Cocoyam B" : ff5[0],
            "Sweet Potatoe B" : ff6[0],
            "Irish Potatoe B" : ff7[0],
            "Plantain B" : ff8[0],
            "Soft drinks or malt B" : gg1[0],
            "Can juice B" : gg2[0],
            "Sachet alcoholic bitters B" : gg3[0],
            "Squadron B" : gg4[0],
            "Red Wine B" : gg5[0],
            "Peas B" : hh1[0],
            "Beans or pudding or akara B" : hh2[0],
            "Green Beans B" : hh3[0],
            "Soybean B" : hh4[0],
            "Soybean B" : hh5[0],
            "Water Melon B" : ii1[0],
            "Pawpaw B" : ii2[0],
            "Carrot B" : ii3[0],
            "Fresh Tomatoe B" : ii4[0],
            "Yellow Pepper B" : ii5[0],
            "Green leafy vegetables B" : jj1[0],
            "Pineapple B" : jj2[0],
            "Cucumber B" : jj3[0],
            "Banana B" : jj4[0],
            "Tangerine B" : jj5[0],
            "Water Leaf B" : jj6[0],
            "Bitter Leaf B" : jj7[0],
            "Vegetable for black soup B" : jj8[0],
            "Avocado B" : jj9[0],
            "Orange B" : jj10[0],
            "Green or red pepper B" : jj11[0],
            "Onions B" : jj12[0],
            "Raddish B" : jj13[0],
            "Beetroot B" : jj14[0],
            "Okra B" : jj15[0],
            "Ginger B" : kk1[0],
            "Garlic B" : kk2[0],
            "Scent Leaf B" : kk3[0],
            "Utazi  bitter local spice B" : kk4[0],
            "Coconut B" : kk5[0],
            "Tigernut B" : kk6[0],
            "Pumpkin 5" : kk7[0]
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

