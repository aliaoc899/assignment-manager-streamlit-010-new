import streamlit as st
from assignment_manager_oo.services.assignment_manager import AssignmentManager
from assignment_manager_oo.data.assignment_store import AssignmentStore

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
        #create an object from the data class and load the data
        from pathlib import Path
        store = AssignmentStore(Path("assignments.json"))
        manager = AssignmentManager(store.load())

        

    elif st.session_state["role"] == "student":
        pass
else:
    pass
    #set up/show the log in /registeration