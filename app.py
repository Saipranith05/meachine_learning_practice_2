import streamlit as st
import numpy as np
import joblib

Model = joblib.load("Exam_Score.pkl")

st.title("Exam Score Prediction")

Hours_Studied = st.number_input("Please enter no.of Hours Studied:")
Attendance = st.number_input("Please enter your Attendance:")
Sleep_Hours = st.number_input("Please enter your Sleep Hours:")
Previous_Scores = st.number_input("Please enter your Previous Scores:")
Family_Income = st.selectbox("Family_Income(0:Low, 1:Medium, 2:High)", [0,1,2])
School_Type = st.selectbox("School_Type(0:Public, 1:Private)", [0,1])
Gender = st.selectbox("Gender(0:Male, 1:Female)", [0,1])

if st.button('predict'):
    features = np.array([[Hours_Studied, Attendance, Sleep_Hours, Previous_Scores, Family_Income, School_Type, Gender]])
    output = Model.predict(features)
    st.write(f"Prediction of Exam Score of the Student:{output[0]}")