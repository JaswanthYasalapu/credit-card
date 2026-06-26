import streamlit as st

# --- 1. SET UP PAGE CONFIG ---
st.set_page_config(page_title="Credit Card Dashboard", page_icon="💳", layout="wide")

# --- 2. INITIALIZE SESSION STATE FOR LOGIN ---
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# --- 3. RENDER LOGIN FORM IF NOT LOGGED IN ---
if not st.session_state["logged_in"]:
    st.title("🔒 Security Gateway")
    
    with st.form("login_form"):
        username_input = st.text_input("Username")
        password_input = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Login")
        
        if submit_button:
            if username_input == "jaswanth" and password_input == "Lucky@6125":
                st.session_state["logged_in"] = True
                st.rerun()  # Forces Streamlit to instantly clear the login screen
            else:
                st.error("Username or password incorrect. Please try again.")

# --- 4. CHECK AUTHENTICATION STATUS ---
if st.session_state["logged_in"]:
    # -------------------------------------------------------------------------
    # ACCESS GRANTED: Everything inside this block runs ONLY when logged in
    # -------------------------------------------------------------------------
    
    # Simple native logout button in the sidebar
    if st.sidebar.button("Logout"):
        st.session_state["logged_in"] = False
        st.rerun()
        
    st.sidebar.success("Logged in as: Jaswanth Yasalap")
    
    # =========================================================================
    # ⬇️ YOUR ORIGINAL DASHBOARD CODE DIRECTLY BELOW THIS LINE ⬇️
    # ⚠️ CRITICAL: Ensure every line you paste below is INDENTED by 4 spaces!
    # =========================================================================
    
    st.title("💳 Credit Card Analytics Dashboard")
    st.write("Welcome to your secured live metrics engine.")
    
    # ---- PASTE ALL YOUR REMAINING CHARTS/GRAPH CODE HERE ----
    # Example:
    # df = pd.read_csv("data.csv")
    # st.line_chart(df)
    
    # =========================================================================

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


