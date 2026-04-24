
from typing import List, Dict, Optional
import uuid

class AssignmentManager:
    def __init__(self,intial_assignments) -> None:
        self.assignments = intial_assignments

    def all(self) -> List[Dict]:
        return list(self.assignments)

    def add(self, title: str , description: str,
            points: int , assignment_type: str) -> Dict:
        if not title.strip():
            raise ValueError("Title is required")
        
        allowed_types = ["Homework", "Lab"]

        if assignment_type.lower() not in allowed_types:
            raise ValueError("assignment type is invalid")
        
        new_assignment = {
                "id": str(uuid.uuid4()),
                "title" : title,
                "description": description,
                "points" : points,
                "type" : assignment_type.lower()
        }
        self.assignments.append(new_assignment)
        return new_assignment

    def delete(self, assignment_id: str):
        pass