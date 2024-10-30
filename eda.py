import streamlit as st
import numpy as np
import joblib

model = joblib.load("Sales.pkl")

st.title("App of Sales")

TV = st.number_input("Please enter your TV Amount:")
Radio = st.number_input("Please enter your Radio Amount:")
Newspaper = st.number_input("Please enter your Newspaper Amount:")

if st.button('predict'):
    features = np.array([[TV, Radio, Newspaper]])
    pranith = model.predict(features)
    st.write(f"Predtion of the Sales{pranith[0]}")