import streamlit as st
import streamlit_authenticator as stauth

# --- 1. SET UP PAGE CONFIG ---
st.set_page_config(page_title="Credit Card Dashboard", page_icon="💳", layout="wide")

# --- 2. MANUALLY BUILD THE SECURE CREDENTIALS DICTIONARY ---
credentials = {
    "usernames": {
        "jaswanth": {
            "email": st.secrets.get("email", "jaswanth@example.com"),
            "name": st.secrets.get("name", "Jaswanth Yasalap"),
            "password": st.secrets.get("password", "$2b$12$.h5mZ85f/BWhU.O0G.aT6Oy7V6wB78kU7w19H2B78gX/8kM1YvU8W")
        }
    }
}

# --- 3. INITIALIZE AUTHENTICATOR ---
# We pass credentials, cookie name, cookie key, and cookie expiry directly
authenticator = stauth.Authenticate(
    credentials=credentials,
    cookie_name="credit_card_dashboard_session",
    key="secure_cookie_signing_key_2026",
    cookie_expiry_days=30
)

# --- 4. RENDER LOGIN FORM ---
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
