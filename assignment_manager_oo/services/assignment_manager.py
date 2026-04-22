
from typing import List, Dict, Optional

class AssignmentManager:
    def __init__(self,intial_assignments) -> None:
        self.assignments = intial_assignments

    def all(self) -> List[Dict]:
        return list(self.assignments)

    def add(self, title: str , description: str,
            points: int , assignment_type: str):
        pass

    def delete(self, assignment_id: str):
        pass