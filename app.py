import streamlit as st
import streamlit_authenticator as stauth

# --- 1. SET UP PAGE CONFIG ---
st.set_page_config(page_title="Credit Card Dashboard", page_icon="💳", layout="wide")

# --- 2. LOAD SECURE CREDENTIALS AND INITIALIZE AUTHENTICATOR ---
try:
    # Safely convert the stream secrets into a pure python dictionary
    secrets_dict = st.secrets.to_dict()
    
    # Extract the nested credentials key
    if "credentials" in secrets_dict:
        credentials_data = secrets_dict["credentials"]
    else:
        st.error("Missing [credentials] section in your Streamlit Secrets panel.")
        st.stop()
        
    # Build the full configuration dictionary wrapper
    config = {
        "credentials": credentials_data,
        "cookie": {
            "expiry_days": 30,
            "key": "secure_cookie_signing_key_2026",
            "name": "credit_card_dashboard_session"
        }
    }
    
    # Initialize the Authenticate instance
    authenticator = stauth.Authenticate(config)

except Exception as e:
    st.error(f"Secrets configuration error: {e}")
    st.stop()

# --- 3. RENDER LOGIN FORM ---
authenticator.login(location='main')

except Exception as e:
    st.error(f"Secrets configuration error: {e}")
    st.stop()

# --- 3. RENDER LOGIN FORM ---
authenticator.login(location='main')
# --- 3. INITIALIZE AUTHENTICATOR ---
# We pass the newly constructed config dictionary directly using unpacking
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)

# --- 4. RENDER LOGIN FORM ---
authenticator.login(location='main')

# --- 4. RENDER LOGIN FORM ---
# --- 4. RENDER LOGIN FORM (FIXED) ---
# Just call the function by itself. Do not assign it to variables.
authenticator.login(location='main')

# --- 5. CHECK AUTHENTICATION STATUS FROM SESSION STATE ---
if st.session_state.get("authentication_status"):
    # -------------------------------------------------------------------------
    # ACCESS GRANTED: Everything inside this block runs ONLY when logged in
    # -------------------------------------------------------------------------
    
    # Render the logout button in the sidebar
    authenticator.logout('Logout', 'sidebar')
    
    st.sidebar.success(f"Logged in as: {st.session_state.get('name')}")
    
    # =========================================================================
    # ⬇️ PASTE YOUR ORIGINAL DASHBOARD CODE DIRECTLY BELOW THIS LINE ⬇️
    # ⚠️ CRITICAL: Ensure every line you paste below is INDENTED by 4 spaces!
    # =========================================================================
    
    st.title("💳 Credit Card Analytics Dashboard")
    st.write("Welcome to your secured live metrics engine.")
    
    # Your dashboard charts, sliders, and dataframes go here...
    
    # =========================================================================
    # ⬆️ END OF YOUR ORIGINAL DASHBOARD CODE ⬆️
    # =========================================================================

elif st.session_state.get("authentication_status") is False:
    # Access Denied: Incorrect password entered
    st.error('Username or password incorrect. Please try again.')

elif st.session_state.get("authentication_status") is None:
    # Default State: User has not attempted logging in yet
    st.warning('Please enter your username and password to proceed.')

elif st.session_state["authentication_status"] is False:
    # Access Denied: Incorrect password entered
    st.error('Username or password incorrect. Please try again.')

elif st.session_state["authentication_status"] is None:
    # Default State: User has not attempted logging in yet
    st.warning('Please enter your username and password to proceed.')

# --- 5. CHECK AUTHENTICATION STATUS ---
if st.session_state.get("authentication_status"):
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

elif st.session_state.get("authentication_status") is False:
    # Access Denied: Incorrect password entered
    st.error('Username or password incorrect. Please try again.')

elif st.session_state.get("authentication_status") is None:
    # Default State: User has not attempted logging in yet
    st.warning('Please enter your username and password to proceed.')
