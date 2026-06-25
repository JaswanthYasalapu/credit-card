import streamlit as st
import pandas as pd
import numpy as np

# 1. Page Configuration
st.set_page_config(page_title="Credit Card Fraud Detector", page_icon="💳", layout="wide")

st.title("💳 Credit Card Analytics & Fraud Detection")
st.markdown("Analyze transaction patterns and test individual transactions for potential fraud risk factors.")

# 2. Main Dashboard Metrics (Using simulated data)
st.subheader("System Overview")
c1, c2, c3 = st.columns(3)
c1.metric("Total Transactions Monitored", "1,248,902")
c2.metric("Fraud Cases Blocked Today", "42", delta="+12% vs yesterday", delta_color="inverse")
c3.metric("System Accuracy Rate", "99.4%")

st.markdown("---")

# 3. Interactive Fraud Detection Section
st.subheader("🕵️‍♂️ Real-Time Transaction Risk Assessor")
st.markdown("Adjust the variables below to simulate an incoming credit card transaction and calculate its fraud risk score.")

# Create input layout using columns
col1, col2 = st.columns(2)

with col1:
    transaction_amount = st.slider("Transaction Amount ($)", min_value=1.0, max_value=5000.0, value=120.0, step=0.5)
    distance_from_home = st.slider("Distance from Home Address (miles)", min_value=0.0, max_value=1000.0, value=4.5, step=0.1)
    online_order = st.selectbox("Is this an online / e-commerce transaction?", options=["No (In-store chip/tap)", "Yes (Online)"])

with col2:
    time_of_day = st.slider("Hour of Transaction (0-23)", min_value=0, max_value=23, value=14)
    device_recognized = st.selectbox("Is the transaction device/terminal recognized?", options=["Yes", "No (New device/location)"])
    high_risk_merchant = st.selectbox("Is the merchant flagged as high-risk? (e.g., electronics, jewelry, crypto)", options=["No", "Yes"])

# 4. Fraud Scoring Logic (A rule-based probability model simulating ML behavior)
# This mimics how a real tree-based model (like Random Forest) weights features.
risk_score = 0

if transaction_amount > 1000: risk_score += 25
if transaction_amount > 3000: risk_score += 20
if distance_from_home > 100: risk_score += 15
if distance_from_home > 500: risk_score += 15
if online_order == "Yes (Online)": risk_score += 10
if time_of_day >= 1 and time_of_day <= 4: risk_score += 15  # Late-night transactions carry minor weight
if device_recognized == "No (New device/location)": risk_score += 15
if high_risk_merchant == "Yes": risk_score += 25

# Cap risk at 100%
risk_score = min(risk_score, 100)

# 5. Prediction Results Trigger
st.markdown("### Assessment Result")
if st.button("Analyze Transaction", type="primary"):
    
    # Progress bar simulation for UX
    with st.spinner("Running fraud detection algorithms..."):
        import time
        time.sleep(0.6) # Short delay to make it feel like a processing model
    
    # Show risk alert level based on score
    if risk_score < 35:
        st.success(f"**APPROVED** — This transaction is safe. Fraud Risk Score: **{risk_score}%**")
        st.balloons()
    elif risk_score >= 35 and risk_score < 65:
        st.warning(f"**FLAGGED FOR REVIEW** — Moderate suspicious indicators detected. Fraud Risk Score: **{risk_score}%**")
        st.info("💡 *Reasoning:* Unusual activity profile, possibly requiring secondary SMS/MFA verification.")
    else:
        st.error(f"**DENIED / BLOCKED** — High probability of a fake/fraudulent transaction! Fraud Risk Score: **{risk_score}%**")
        st.markdown("""
        🚨 **Risk Triggers Tripped:**
        * High-risk spending profile relative to historical user trends.
        * Security thresholds crossed for terminal verification or location matching.
        """)
