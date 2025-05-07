# Import necessary libraries
import streamlit as st       # For building the web app
import pandas as pd          # For creating input data as a DataFrame
import joblib                # For loading the pre-trained model

# Load the trained machine learning pipeline model
model = joblib.load("fraud_detection_pipeline.pkl")

# Set the title of the web app
st.title("Fraud Detection Prediction Web App")

# Add instructions for the user
st.markdown("Please enter the transaction details and use the predict button.")

# Draw a horizontal divider
st.divider()

# Input widgets for the user to enter transaction details
transaction_type = st.selectbox(
    "Transaction Type", 
    ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"]
)
amount = st.number_input(
    "Amount", 
    min_value=0.0,
    value=1000.0
)
oldbalanceOrg = st.number_input(
    "Old Balance (Sender)", 
    min_value=0.0,  
    value=10000.0
)
newbalanceOrig = st.number_input(
    "New Balance (Sender)", 
    min_value=0.0,
    value=9000.0
)
oldbalanceDest = st.number_input(
    "Old Balance (Receiver)", 
    min_value=0.0,
    value=0.0
)
newbalanceDest = st.number_input(
    "New Balance (Receiver)", 
    min_value=0.0,
    value=0.0
)

# When the "Predict" button is clicked
if st.button("Predict"):
    # Collect all the input values into a DataFrame
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    # Use the loaded model to make a prediction
    prediction = model.predict(input_data)[0]

    # Show the prediction result (0 or 1)
    st.subheader(f"Prediction : {int(prediction)}")

    # Display a message based on prediction
    if prediction == 1:
        st.error("⚠️ This transaction could potentially be a fraud.")
    else:
        st.success("✅ This transaction appears to be valid.")
