import streamlit as st
# Own python files
from src.utilities import st_methods_login

# Initialize st.session_state (st.Class properties) at start or reload of app/page. 
def init_st_session_state() -> None:
    """Initialize all streamlit.session_states that are needed or required in the app."""
    if "username" not in st.session_state:
        st.session_state["logged_in"] = None
    if "path_credential_users" not in st.session_state:
        st.session_state["path_credential_users"] = "data/credential_users.yaml"
    return

# ------------------------------- Pages --------------------------------------

def pages_bevor_login():
    """Pages of streamlit app bevor login defined by functions"""
    login = st.Page(st_methods_login.login_box, title="Login", icon=":material/login:")
    register = st.Page(st_methods_login.register_box, title="Register", icon=":material/person_add:")

    return [login, register]

def pages_after_login():
    """Pages of streamlit app after login defined by functions and python files"""
    welcome = st.Page("src/ui_pages/page_1_welcome.py", title="Welcome", icon=":material/home:")
    reset_password = st.Page(st_methods_login.reset_password_box, title="Reset Password", icon=":material/lock_reset:")
    logout = st.Page(st_methods_login.logout_box, title="Logout", icon=":material/logout:")

    return [welcome, reset_password, logout]

def main():
    """
    Main function of the entire steamlit app. 
    This is where the navigator is defined that leads to all scripts and functions. 
    """
    # Init some session states
    init_st_session_state()

    # Show pages before a user is logged in
    if not st.session_state.logged_in:
        page_navigator = st.navigation(pages_bevor_login())
        page_navigator.run()
    
    # Show pages after a user is logged in
    elif st.session_state.logged_in:
        page_navigator = st.navigation(pages_after_login())
        page_navigator.run()
    
    
    return

if __name__ == "__main__":
    main()