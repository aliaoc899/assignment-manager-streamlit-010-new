import streamlit as st
from services.assignment_manager import AssignmentManager
from data.assignment_store import AssignmentStore
from ui.assignment_dashboard import AssignmentDashboard


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
        store = AssignmentStore(Path("assignment_manager_oo/assignments.json")) # create an object from the data class and set the object inital state
        manager = AssignmentManager(store.load()) # create an object from the assignment manager class and set the object's inital state 
        dashboard = AssignmentDashboard(manager,store) # create an object from the dashboard class and set the object's inital state
        dashboard.main() # call the orch

    elif st.session_state["role"] == "student":
        pass
else:
    pass
    #set up/show the log in /registeration