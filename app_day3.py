import streamlit as st
import time
import json
from pathlib import Path

st.title("Course Management App")
st.divider()

next_assignment_id_number = 3

#load assignments
assignments = [
    {
        "id" : "HW1",
        "title" : "Introduction to Database",
        "description": "basics of database design",
        "points" : 100,
        "type" : "homework"
    },
    {
        "id": "HW2",
        "title": "Normalization",
        "description" : "Normalize the table designs",
        "points": 100,
        "type" : "lab"
    }
]

json_path = Path("assignments.json")

if json_path.exists:
    with json_path.open("r", encoding= "utf-8") as f:
        assignments = json.load(f)




tab1, tab2, tab3 = st.tabs(["View Assignments", "Add New Assignment", "Update An Assignment"])

with tab1:
    #st.info("This tab is under development!")
    option = st.radio("View/Search", ["View" , "Search"], horizontal= True)

    if option == "View":
        st.dataframe(assignments)

    else:
        search_title = st.selectbox("Assignmnet Titles", [])


        
with tab2:
    # Add New Assignment
    st.markdown("# Add New Assignment")

    #input

    title = st.text_input("Title",placeholder="ex. Homework 1", 
                        help="This is the name of the assignment")

    description = st.text_area("Description",placeholder="ex. database design...")
    due_date = st.date_input("Due Date")
    assignments_type = st.radio("Type",["Homework", "Lab"])

    points = st.number_input("Points")

    #assignments_type2 = st.selectbox("Type", ["Homework", "Lab","Other"])
    #if assignments_type2 == "Other":
    #   assignments_type2 = st.text_input("Assingment Type")

    #lab = st.checkbox("Lab")

    with st.expander("Assignment Preview",expanded= True):
        st.markdown("## Live Preview")
        st.markdown(f"Title: {title}")

    btn_save = st.button("Save",use_container_width=True, disabled=False)


   

    if btn_save:
        with st.spinner("Saving the Assignmnet..."):
            time.sleep(5)
            if not title:
                st.warning("Enter Assignmnet Title")
            else:
                #Add/Create new Assignmnet
                new_assignmnet_id = "HW" + str(next_assignment_id_number)
                next_assignment_id_number += 1

                assignments.append(
                    {
                    "id" : new_assignmnet_id,
                    "title": title,
                    "description" : description,
                        "points" : points,
                        "type" : assignments_type
                    }
                )

                with json_path.open("w",encoding="utf-8") as f:
                    json.dump(assignments,f)


                st.success("Assignment is recorded!")
                st.dataframe(assignments)