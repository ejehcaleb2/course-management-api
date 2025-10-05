from fastapi import APIRouter, HTTPException
from typing import List
from schemas.course_schema import Course, CourseCreate, CourseUpdate
from services import course_service

router = APIRouter(prefix="/courses", tags=["Courses"])

@router.post("/", response_model=Course)
def create_course(course: CourseCreate):
    return course_service.create_course(course)

@router.get("/", response_model=List[Course])
def get_courses():
    return course_service.get_courses()

@router.get("/{course_id}", response_model=Course)
def get_course(course_id: str):
    course = course_service.get_course(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.put("/{course_id}", response_model=Course)
def update_course(course_id: str, course: CourseUpdate):
    updated = course_service.update_course(course_id, course)
    if not updated:
        raise HTTPException(status_code=404, detail="Course not found")
    return updated

@router.delete("/{course_id}")
def delete_course(course_id: str):
    success = course_service.delete_course(course_id)
    if not success:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"message": "Course deleted successfully"}

@router.patch("/{course_id}/close", response_model=Course)
def close_enrollment(course_id: str):
    course = course_service.close_enrollment(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course
