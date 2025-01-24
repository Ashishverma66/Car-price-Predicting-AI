import streamlit as st
import json
#import requests
from streamlit_lottie import st_lottie
from model_operation import get_car_price_prediction


def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
     return json.load(f)

lottie_coding=load_lottiefile("E:\Py_Ash\Linear Regration Project\Main Scene.json")


st.title("Hi, This is your car price predicting :red[A.I] :sunglasses:")
st_lottie(
    lottie_coding
)

car_age_in_months=st.text_input("Enter your car age in months")
if st.button("Predict",type="primary"):
    car_price=get_car_price_prediction(car_age_in_months)
    st.write(f"Final evaluation of your car is {car_price:.2f}")