import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# 1. Page Config
st.set_page_config(page_title="AI Fraud Detector", page_icon="🤖", layout="wide")
st.title("🤖 AI-Powered Credit Card Fraud Detection")
st.markdown("This app uses a live-trained Random Forest Machine Learning model to evaluate transaction risk.")

# 2. Background ML Training (Cached so it only runs once)
@st.cache_resource
def train_fraud_model():
    # Generating a synthetic dataset representing 10,000 transactions
    np.random.seed(42)
    n_samples = 10000
    
    # Features: [Amount, Distance, Is_Online, Is_High_Risk_Merchant]
    X_legit = np.random.multivariate_normal([50, 5, 0.2, 0.1], [[400, 0, 0, 0], [0, 25, 0, 0], [0, 0, 0.1, 0], [0, 0, 0, 0.05]], int(n_samples*0.95))
    X_fraud = np.random.multivariate_normal([800, 300, 0.8, 0.7], [[50000, 0, 0, 0], [0, 10000, 0, 0], [0, 0, 0.05, 0], [0, 0, 0, 0.1]], int(n_samples*0.05))
    
    X = np.vstack((X_legit, X_fraud))
    # Clip values to ensure realistic bounds (e.g., distances and amounts can't be negative)
    X = np.clip(X, 0, None)
    # Ensure binary columns are strictly 0 or 1
    X[:, 2] = np.where(X[:, 2] > 0.5, 1, 0)
    X[:, 3] = np.where(X[:, 3] > 0.5, 1, 0)
    
    # Labels: 0 = Legit, 1 = Fraud
    y = np.array([0] * len(X_legit) + [1] * len(X_fraud))
    
    # Train Model
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X, y)
    return model

# Initialize the model
model = train_fraud_model()

st.success("🤖 Machine Learning Model trained successfully and active!")

st.markdown("---")

# 3. User Inputs for Testing
st.subheader("🕵️‍♂️ Live Transaction Input")
col1, col2 = st.columns(2)

with col1:
    amount = st.slider("Transaction Amount ($)", 1.0, 5000.0, 120.0)
    distance = st.slider("Distance from Home (miles)", 0.0, 1000.0, 12.0)

with col2:
    online = st.selectbox("Is this an Online transaction?", ["No", "Yes"])
    high_risk = st.selectbox("Is the Merchant flagged as High-Risk?", ["No", "Yes"])

# Convert text options to numbers for the model (0 or 1)
online_val = 1 if online == "Yes" else 0
high_risk_val = 1 if high_risk == "Yes" else 0

# 4. Predict Button
if st.button("Run AI Detection", type="primary"):
    # Structure the inputs exactly like the model's training data
    features = np.array([[amount, distance, online_val, high_risk_val]])
    
    # Get predictions
    prediction = model.predict(features)[0]
    probabilities = model.predict_proba(features)[0] # [Prob of legit, Prob of fraud]
    fraud_probability = int(probabilities[1] * 100)
    
    st.markdown("### AI Assessment Analysis")
    
    if prediction == 0:
        st.success(f"✅ **Approved.** The AI is confident this transaction is legitimate. (Fraud Risk: {fraud_probability}%)")
        st.balloons()
    else:
        st.error(f"🚨 **Blocked!** The AI has flagged this transaction as highly suspicious. (Fraud Risk: {fraud_probability}%)")
