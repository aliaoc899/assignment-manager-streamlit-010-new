import streamlit as st

st.set_page_config("Assignment Manager")

st.title("Assignment Manager")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = True


if "role" not in st.session_state:
    st.session_state["role"] = "Instructor"

if "page" not in st.session_state:
    st.session_state["page"]= "dashboard"

if st.session_state["logged_in"]:
    if st.session_state["role"] == "Instructor":
        pass
    elif st.session_state["role"] == "student":
        pass
else:
    pass
    #set up/show the log in /registeration