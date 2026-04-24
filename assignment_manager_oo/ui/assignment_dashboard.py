import streamlit as st

from assignment_manager_oo.services.assignment_manager import AssignmentManager
from assignment_manager_oo.data.assignment_store import AssignmentStore

class AssignmentDashboard:
    def __init__(self, manager: 'AssignmentManager', store: 'AssignmentStore') -> None:
        self.manager = manager
        self.store = store

    def main(self):
        if st.session_state["page"] == "dashboard":
            self.show_manage_assignments()
        else:
            self.show_add_new_assignment()

    def show_manage_assignments(self):
        assignments = self.manager.all()
        for assignment in assignments:
            st.write(f"Title: {assignment['title']}")

        if st.button("Add New Assignment"):
            st.session_state["page"] = "add_assignment"
            st.rerun()


    def show_add_new_assignment(self):
        pass