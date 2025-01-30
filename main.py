import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

st.title("Restaurant Price Prediction")
st.header('We used Regression model to predict a Restaurant price')

data = pd.read_csv("zomato.csv")
X_test = pd.read_csv('X_test.csv')
y_test = pd.read_csv('y_test.csv')

model = joblib.load("model1.joblib")

online_order = st.selectbox("Do you want to do online order: ", data['online_order'].unique().tolist())
book_table = st.selectbox("Do you want to book table: ", data['book_table'].unique().tolist())
ratings = st.slider("Select a rating for Restaurant", min_value=0.0, max_value=5.0, step=0.1)
votes = st.slider("Select how much people rate a Restaurant", min_value=0, max_value=2500, step=10)
rest_type = st.selectbox("Select restaurant types", data['rest_type'].unique().tolist())
type = st.selectbox("Select your Dining Options", data['type'].unique().tolist())
location = st.selectbox("Select a location for restaurant", data['location'].unique().tolist())

input_data = pd.DataFrame([[online_order, book_table,ratings,votes,rest_type,type,location]],
                          columns=['online_order','book_table','rate','votes','rest_type','type','location'])

st.dataframe(input_data)

if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted price for the Restuarant is: {prediction.round(2)} INR")

tab1, tab2, tab3 = st.tabs(["R2_score",'Mean Absolute Error','Root Mean Squared Error'])

with tab1:
    st.header('R2_score')
    st.write("The R² score of the model on the test dataset")
    score = round(r2_score(y_test, model.predict(X_test))*100,2)
    st.success(f"R2_score: {score}%")

with tab2:
    st.header('Mean Absolute Error')
    st.write("The mean absolute value of the model on the test dataset")
    mean_absolute_error_score = round(mean_absolute_error(y_test, model.predict(X_test)), 4)
    st.success(f"Mean Absolute Error: {mean_absolute_error_score}")

with tab3:
    st.header('Root Mean Squared Error')
    st.write("The root mean squared value of the model on the test dataset")
    RMSE = round(np.sqrt(mean_squared_error(y_test, model.predict(X_test))), 4)
    st.success(f"Root Mean Squared Error: {RMSE}")


