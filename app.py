import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Set up page styling
st.set_page_config(page_title="Fraud Detection App", page_icon="💳", layout="centered")

st.title("💳 Credit Card Fraud Detection Portal")
st.write("This application uses a trained Random Forest model to analyze transaction parameters and predict the likelihood of fraud.")

# Load the saved model and scaler
@st.cache_resource
def load_assets():
    model = joblib.load('fraud_model.pkl')
    scaler = joblib.load('scaler.pkl')
    return model, scaler

try:
    model, scaler = load_assets()
    
    st.sidebar.header("Transaction Inputs")
    
    # 1. Input for Amount
    amount = st.sidebar.number_input("Transaction Amount ($)", min_value=0.0, max_value=100000.0, value=150.0, step=10.0)
    
    st.sidebar.write("### Principal Component Features")
    st.sidebar.write("Provide sample anonymized V-features for evaluation:")
    # 2. Input for a few prominent PCA features (defaulting others to 0 for demo purposes)
    v1 = st.sidebar.slider("Feature V1", -5.0, 5.0, 0.0)
    v2 = st.sidebar.slider("Feature V2", -5.0, 5.0, 0.0)
    v3 = st.sidebar.slider("Feature V3", -5.0, 5.0, 0.0)
    v4 = st.sidebar.slider("Feature V4", -5.0, 5.0, 0.0)
    
    # Process inputs when button is clicked
    if st.button("Analyze Transaction", type="primary"):
        # Scale the amount using the saved scaler
        scaled_amount = scaler.transform([[amount]])[0][0]
        
        # Create an array of 29 features (V1 to V28 + scaled_amount)
        # We populate V1-V4 from sliders, leave V5-V28 as 0, and append scaled_amount
        features = np.zeros(29)
        features[0] = v1
        features[1] = v2
        features[2] = v3
        features[3] = v4
        features[-1] = scaled_amount  # Last feature is the scaled amount
        
        # Reshape for prediction
        features_encoded = features.reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(features_encoded)[0]
        prediction_proba = model.predict_proba(features_encoded)[0]
        
        # Display results
        st.subheader("Analysis Results")
        if prediction == 1:
            st.error(f"🚨 HIGH RISK: This transaction is flagged as POTENTIAL FRAUD.")
            st.metric(label="Fraud Confidence", value=f"{prediction_proba[1]*100:.2f}%")
        else:
            st.success(f"✅ CLEAN: This transaction appears to be LEGITIMATE.")
            st.metric(label="Legitimate Confidence", value=f"{prediction_proba[0]*100:.2f}%")
            
except FileNotFoundError:
    st.error("Error: Trained model assets ('fraud_model.pkl' or 'scaler.pkl') not found. Please run 'python model.py' first to generate them.")