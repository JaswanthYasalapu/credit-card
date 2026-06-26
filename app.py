import streamlit as st
import streamlit_authenticator as stauth

# --- 1. SET UP PAGE CONFIG (Must be the very first Streamlit command) ---
st.set_page_config(page_title="Credit Card Dashboard", page_icon="💳", layout="wide")

# --- 2. LOAD SECURE CREDENTIALS FROM STREAMLIT SECRETS ---
# This securely reads the user details you paste into the Streamlit Cloud dashboard
try:
    credentials = st.secrets["credentials"].to_dict()
except Exception:
    st.error("Secrets dictionary 'credentials' is missing. Please set it up in your Streamlit Cloud settings.")
    st.stop()

# --- 3. INITIALIZE AUTHENTICATOR ---
authenticator = stauth.Authenticate(
    credentials,
    cookie_name="credit_card_dashboard_session",
    key="secure_cookie_signing_key_2026", # You can change this to any random string
    cookie_expiry_days=30
)

# --- 4. RENDER LOGIN FORM ---
name, authentication_status, username = authenticator.login(
    location='main', 
    title='Login to Credit Card Dashboard'
)

# --- 5. CHECK AUTHENTICATION STATUS ---
if authentication_status:
    # -------------------------------------------------------------------------
    # ACCESS GRANTED: Everything inside this block runs ONLY when logged in
    # -------------------------------------------------------------------------
    
    # Render the logout button in the sidebar
    authenticator.logout('Logout', 'sidebar')
    
    st.sidebar.success(f"Logged in as: {name}")
    
    # =========================================================================
    # ⬇️ PASTE YOUR ORIGINAL DASHBOARD CODE DIRECTLY BELOW THIS LINE ⬇️
    # ⚠️ CRITICAL: Ensure every line you paste below is INDENTED by 4 spaces!
    # =========================================================================
    
    st.title("💳 Credit Card Analytics Dashboard")
    st.write("Welcome to your secured live metrics engine.")
    
    # Example placeholder of your dashboard logic:
    # st.metric(label="Total Spend", value="$4,500")
    # fig = your_plotting_function()
    # st.plotly_chart(fig)
    
    # =========================================================================
    # ⬆️ END OF YOUR ORIGINAL DASHBOARD CODE ⬆️
    # =========================================================================

elif authentication_status == False:
    # Access Denied: Incorrect password entered
    st.error('Username or password incorrect. Please try again.')

elif authentication_status == None:
    # Default State: User has not attempted logging in yet
    st.warning('Please enter your username and password to proceed.')
