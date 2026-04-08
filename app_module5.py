import streamlit as st
import time
import json
from pathlib import Path
import uuid


#Data Layer
def load_data(json_path):
    if json_path.exists():
        with open(json_path, "r") as f:
            return json.load(f)
    else:
        return []

def save_data(assignments, json_path):
    with open(json_path, "w") as f:
                json.dump(assignments,f)

#Service Layer
def add_new_assignment(assignments,title, description,points, type):
    assignments.append(
        {
            "id": str( uuid.uuid4()),
            "title": title,
            "description": description,
            "points": points,
            "type": type
        }
    )
    return assignments

#Ui Layer
def render_add_new_assignment(assignments, json_path):
    col1, col2 = st.columns([3,1])
    with col1:
        st.subheader("Add New Assignment")
    with col2:
        if st.button("Back", key="back_btn", use_container_width=True):
            st.session_state["page"] = "Assignment Dashboard"
            st.rerun()
    st.session_state['draft']['title'] = st.text_input("Title", key="title_txt")
    st.session_state['draft']['description'] = st.text_area("Description", key="description_txt",
                                                             placeholder="normalization is covered here",
                            help="Here you are entering the assignment details")
    st.session_state["draft"]['points'] = st.number_input("Points",key="points_number_input")
    st.session_state['draft']['assignment_type'] = st.selectbox("Type",  ["Select an option", "Homework", "Lab", "other"], 
                                                                key="assignment_type_selector")

    
    if st.button("Save", key="save_btn", use_container_width=True, type="primary"):
        with st.spinner("In progress..."):

            #add new assignment to the assignments list
            add_new_assignment(assignments,st.session_state['draft']['title'],
                              st.session_state['draft']['description'],
                              st.session_state["draft"]['points'],
                              st.session_state['draft']['assignment_type'])
            

            save_data(assignments,json_path)

            st.success("assignment is recorded")
            time.sleep(4)
            st.session_state["page"] = "Assignment Dashboard"

            st.rerun()

def render_dashboard(assignments):
    col1, col2 = st.columns([3,1])
    with col1:
        st.subheader("Assignments")

    with col2:
        if st.button("Add New Assignment", key="add_new_assignment_btn", 
                     type="primary",use_container_width=True):
            st.session_state["page"] = "Add New Assignment"
            st.rerun()

    st.dataframe(assignments)


def main():
    st.set_page_config(page_title="Course Management",
                    layout="centered",
                    initial_sidebar_state="collapsed")

    st.title("Course Management App")
    st.divider()

    #Loading the Data

    assignments = [
        {
            "id": "HW1",
            "title": "Intro to Database",
            "description": "basics of database design",
            "points": 100,
            "type": "homework"
        },
        {
            "id": "HW2",
            "title": "Normalization",
            "description": "normalizing",
            "points": 100,
            "type": "homework"
        }
    ]

    json_path = Path("assignments.json")
    
    assignments = load_data(json_path)

    # Session State Initialization
    if "page" not in st.session_state:
        st.session_state["page"] = "Assignment Dashboard"

    if "draft" not in st.session_state:
        st.session_state["draft"] = {}


    if st.session_state["page"] == "Assignment Dashboard":
        render_dashboard(assignments=assignments)

        
    elif st.session_state["page"] == "Add New Assignment":
        render_add_new_assignment(assignments=assignments, json_path=json_path)
        
    elif st.session_state["page"] == "Edit Assignment":
        pass



if __name__ == "__main__":
    main()