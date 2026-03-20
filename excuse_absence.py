import streamlit as st
import json
from pathlib import Path
from datetime import datetime
import uuid
import time

st.set_page_config("Excuse Absence App",layout="wide",initial_sidebar_state="expanded")



if "page" not in st.session_state:
    st.session_state["page"] = "dashboard"


requests = [
    {
        "request_id": "011101",
        "status": "Pending",
        "course_id": "011101",
        "student_email": "jsmith@university.edu",
        "absence_date": "2026-03-25",
        "submitted_timestamp": "2026-03-19 08:30:00",
        "excuse_type": "Medical",
        "explanation": "I have a scheduled doctor's appointment that I cannot reschedule.",
        "instructor_note": ""
    }
]

json_path_requests = Path("requests.json")

if json_path_requests.exists():
    with open(json_path_requests, "r") as f:
        requests = json.load(f)




with st.sidebar:
    if st.button("Excuse Absence Dashboard", key="dashboard_btn",type="primary",use_container_width=True):
        st.session_state["page"] = "dashboard"
        st.rerun()

    if st.button("Excuse Absence Request", key="request_btn",type="primary",use_container_width=True):
        st.session_state["page"] = "request"
        st.rerun()



if st.session_state["page"] == "dashboard":

    col1,col2,col3 = st.columns([2,3,2])
    with col2:
        st.header("Excuse Absences")
    
    st.divider()

    col1,col2,col3 = st.columns([3,1,1])
   
    with col1:
        st.markdown("### Excused Absences")
    
    with col2:
        with st.container(border=True):
            col1_a, col1_b = st.columns(2)
            with col1_a:
                st.markdown("Count")
            with col1_b:
                #st.metric("", len(requests))
                st.markdown(f"## {len(requests)}")
    with col3:
        with st.container(border=True):
            col1_a, col1_b = st.columns(2)
            with col1_a:
                st.markdown("Pending")
            with col1_b:
                #st.metric("", len(requests))
                pending = 0
                for request in requests:
                    if request["status"].strip().lower() == "pending":
                        pending +=1

                st.markdown(f"## {pending}")


    with st.container(border= True):
        col1 , col2 = st.columns([4,2])
        with col1:
            search_item = st.text_input("Search by student Email", key= "search_txt_by_email")
        with col2:
            
            if "selected_status_filter" not in st.session_state:
                st.session_state["selected_status_filter"] = None
            

            selected_item = st.selectbox("Status", options= requests, format_func= lambda x: f"{x["status"]}")
            st.session_state["selected_status_filter"] = selected_item["status"]
           

    
    col1, col2 = st.columns([4,2])
    selected_request = None
    with col1:
        
        requests_list = requests
        
        if "selected_status_filter" in st.session_state:
            requests_list = []
            for request in requests:
                if request["status"] == st.session_state["selected_status_filter"]:
                    requests_list.append(request)



        event = st.dataframe(
            requests_list,
                on_select="rerun",
                selection_mode="single-row"
            )

        # Check if the user actually clicked on a row
        if event.selection.rows:
            selected_index = event.selection.rows[0]
            
            # Use the index to grab the original dictionary from your list
            selected_request = requests_list[selected_index]
    with col2:
        with st.container(border= True):
            st.markdown("### Request Details")
            if selected_request:
                with st.container(border= True):
                    st.markdown(f"**Status:** {selected_request['status']}")
                    st.markdown(f"**Student Email:** {selected_request['student_email']}")
                    st.markdown(f"**Absence Date:** {selected_request['absence_date']}")
                    st.markdown(f"**Submit Date:** {selected_request['submitted_timestamp']}")
                    st.markdown(f"**Excuse Type:** {selected_request['excuse_type']}")
                    st.markdown(f"**Explanation:** {selected_request['explanation']}")

                if selected_request['status'].strip().lower() =="pending":

                    explanation = st.text_area("Explanation (optional)",key="explnation_textbox",height=100)
                    decision = st.radio("Decision", ["Approve", "Reject","Cancel"], key="decision_radio")
                    

                    if st.button("Record Decision", key = "record_decision_excuse_btn", type="primary",use_container_width=True):
                        with st.spinner("Recording the decision..."):

                            for request in requests:
                                if request["request_id"] == selected_request["request_id"]:
                                    request["status"] = decision
                                    request["explanation"] = explanation
                                    break
                            
                            with open(json_path_requests,"w") as f :
                                json.dump(requests,f)
                        
                        st.success("Information recorded.")
                        time.sleep(4)
                        st.rerun()



elif st.session_state["page"] == "request":
    st.header("Excuse Request - Coming Soon...")
    st.divider()
    col1,col2,col3 = st.columns([1,3,1])
    with col2:
        with st.container(border=True):

            st.markdown("### Excuse Request")
            st.divider()
            absence_date = st.date_input("Absence Date", key="absence_date_input")
            student_explanation = st.text_area("Explanation" , key="student_explanation_text",height=100)
            excuse_type = st.radio("Excuse Type", ["Medical", "Competition", "Other"])

            if st.button("Submit Request", key="submit_request_btn", use_container_width=True, type="primary"):
                if not student_explanation and excuse_type and absence_date:
                    st.warning("Please provide the requested information")
                else:
                    with st.spinner("Recording..."):
                        requests.append({
                            "request_id": str(uuid.uuid4()),
                            "status": "Pending",
                            "course_id": "011101",
                            "student_email": "jsmith@university.edu",
                            "absence_date": str(absence_date),
                            "submitted_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "excuse_type": excuse_type,
                            "explanation": student_explanation,
                            "instructor_note": ""
                        })
                        
                        with open(json_path_requests,"w") as f:
                            json.dump(requests,f)

                    st.success("Request recorded.")
                    time.sleep(4)
                    st.rerun()
                


