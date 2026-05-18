import streamlit as st
import joblib
import numpy as np

model = joblib.load(r"C:\Users\shrut\OneDrive\Desktop\customer churn prediction\models\churn_model.pk1")
scaler = joblib.load(r"C:\Users\shrut\OneDrive\Desktop\customer churn prediction\models\scaler.pk1")

st.title("Customer Churn Prediction")
st.write("Enter customer details")

# Real options
gender = st.selectbox("Gender", ["Female", "Male"])
senior = st.selectbox("Senior Citizen", ["No", "Yes"])
partner = st.selectbox("Partner", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["No", "Yes"])

tenure = st.number_input("Tenure")

phone = st.selectbox("Phone Service", ["No", "Yes"])
multiple = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])

internet = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

security = st.selectbox(
    "Online Security",
    ["No", "Yes", "No internet service"]
)

backup = st.selectbox(
    "Online Backup",
    ["No", "Yes", "No internet service"]
)

device = st.selectbox(
    "Device Protection",
    ["No", "Yes", "No internet service"]
)

tech = st.selectbox(
    "Tech Support",
    ["No", "Yes", "No internet service"]
)

tv = st.selectbox(
    "Streaming TV",
    ["No", "Yes", "No internet service"]
)

movies = st.selectbox(
    "Streaming Movies",
    ["No", "Yes", "No internet service"]
)

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

paperless = st.selectbox("Paperless Billing", ["No", "Yes"])

payment = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer",
        "Credit card"
    ]
)

monthly = st.number_input("Monthly Charges")
total = st.number_input("Total Charges")


# Encoding maps
gender = {"Female":0, "Male":1}[gender]
senior = {"No":0, "Yes":1}[senior]
partner = {"No":0, "Yes":1}[partner]
dependents = {"No":0, "Yes":1}[dependents]
phone = {"No":0, "Yes":1}[phone]

multiple = {
    "No":0,
    "Yes":1,
    "No phone service":2
}[multiple]

internet = {
    "DSL":0,
    "Fiber optic":1,
    "No":2
}[internet]

security = {
    "No":0,
    "Yes":1,
    "No internet service":2
}[security]

backup = {
    "No":0,
    "Yes":1,
    "No internet service":2
}[backup]

device = {
    "No":0,
    "Yes":1,
    "No internet service":2
}[device]

tech = {
    "No":0,
    "Yes":1,
    "No internet service":2
}[tech]

tv = {
    "No":0,
    "Yes":1,
    "No internet service":2
}[tv]

movies = {
    "No":0,
    "Yes":1,
    "No internet service":2
}[movies]

contract = {
    "Month-to-month":0,
    "One year":1,
    "Two year":2
}[contract]

paperless = {"No":0, "Yes":1}[paperless]

payment = {
    "Electronic check":0,
    "Mailed check":1,
    "Bank transfer":2,
    "Credit card":3
}[payment]


if st.button("Predict"):

    input_data = np.array([[
        gender, senior, partner, dependents,
        tenure, phone, multiple, internet,
        security, backup, device, tech,
        tv, movies, contract,
        paperless, payment,
        monthly, total
    ]])

    input_data = scaler.transform(input_data)

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Customer is likely to churn")
    else:
        st.success("Customer is likely to stay")