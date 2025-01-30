import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

st.header("Restuarant Price Prediction")

data = pd.read_csv("zomato.csv")
model = joblib.load("model1.joblib")

online_order = st.selectbox("Do you want to do online order: ", data['online_order'].unique().tolist())
book_table = st.selectbox("Do you want to book table: ", data['book_table'].unique().tolist())
ratings = st.slider("Select a rating for Restuarant", min_value=0.0, max_value=5.0, step=0.1)
votes = st.slider("Select how much people rate a Restuarant", min_value=0, max_value=2500, step=10)
rest_type = st.selectbox("Select restaurant types", data['rest_type'].unique().tolist())
type = st.selectbox("Select your Dining Options", data['type'].unique().tolist())
location = st.selectbox("Select a location for restuarant", data['location'].unique().tolist())

input_data = pd.DataFrame([[online_order, book_table,ratings,votes,rest_type,type,location]],
                          columns=['online_order','book_table','rate','votes','rest_type','type','location'])

st.dataframe(input_data)

# if st.button("Predict Price"):
#     prediction = model.predict(input_data)
#     st.success(f"Predicted price for the Restuarant is:{prediction}")

