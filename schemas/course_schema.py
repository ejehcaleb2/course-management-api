from pydantic import BaseModel
from typing import Optional

class CourseBase(BaseModel):
    title: str
    description: str
    is_open: Optional[bool] = True

class CourseCreate(CourseBase):
    pass

class CourseUpdate(CourseBase):
    pass

class Course(CourseBase):
    id: str
