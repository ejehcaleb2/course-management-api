from pydantic import BaseModel
from typing import Optional

class EnrollmentBase(BaseModel):
    user_id: str  
    course_id: str  
    enrolled_date: str  
    completed: Optional[bool] = False

class EnrollmentCreate(EnrollmentBase):
    pass

class Enrollment(EnrollmentBase):
    id: str  
