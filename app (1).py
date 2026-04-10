import streamlit as st
import numpy as np
import pandas as pd
import pickle

st.title("Heart Disease Predictor")
with open('heart_model.pkl','rb') as file:
    model=pickle.load(file)

# ''' Age , sex, chest pain type, resting blood prussure, serum colostrol in mg per dl, fasting blood suger > 120 mg/dl, resting elctro cardiographic results, 
# (values 0,1,2), max heart rate, execrise induced , angina, old peek = st depression induced by excersie related to rest,
# the slop of peakk exercise st segment, no of mahor vessels (0 to 3 colored by folosopy), thal : 0 = normal , 1 = fixed defect  : 2 = reversibel defect'''


age = st.slider("Select your age : ",0,100,25)
st.write(f"Your age is : {age}")

sex_options = ["Male",'Female']
sex = st.selectbox("Choose your sex : ",sex_options)
if sex=='Male':
    sex=1
else:
    sex=0

chest_pain = st.checkbox("Chestpain")


Resting_Blood_Pressure = st.number_input("Resting Blood Pressure",help="Pressure of blood in arteries when the body is at rest; normal value ≈ 120/80 mmHg.")
serum_colostrol = st.number_input("Serum colostrol : ", help="Amount of cholesterol present in blood; normal level ≈ <200 mg/dL.")

fasting_blood_pressure = st.checkbox("Fasting Blood Pressure")

rec = [0,1,2]
resting_electro_cardio = st.selectbox("Reseting Electro Cardio Results",rec)

max_heartrate = st.number_input("Maximum Heartrate(bpm) :")

exercise_induced = st.checkbox("Exercise Induced")
angina = st.checkbox("Angina ", help="Chest pain caused by reduced blood flow to the heart.")

old_peak = st.number_input("Old peek : ")
slop = st.number_input("Slope : ")
mahor_vessel = st.number_input("Mahor Vessel",0,3)
thal = st.number_input("Thal Value",0,2)

input_data = [[
    age,
    sex,
    chest_pain,
    Resting_Blood_Pressure,
    serum_colostrol,
    fasting_blood_pressure,
    resting_electro_cardio,
    max_heartrate,
    exercise_induced,
    old_peak,
    slop,
    mahor_vessel,
    thal
]]

result = model.predict(input_data)


button=st.button("Submit here ")


if button:
    if result == 0:
        new_result = "You may not have a heart disease."
        st.success(f'The result is: {new_result}')
    else:
        st.warning(new_result)
    
