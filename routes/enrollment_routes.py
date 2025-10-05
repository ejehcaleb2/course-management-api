from fastapi import APIRouter, HTTPException
from typing import List
from schemas.enrollment_schema import Enrollment, EnrollmentCreate
from services import enrollment_service

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])

@router.post("/", response_model=Enrollment)
def create_enrollment(enrollment: EnrollmentCreate):
    try:
        return enrollment_service.enroll_user(enrollment)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[Enrollment])
def get_all_enrollments():
    return enrollment_service.get_all_enrollments()

@router.get("/{enrollment_id}", response_model=Enrollment)
def get_enrollment(enrollment_id: str):
    enrollment = enrollment_service.get_enrollment(enrollment_id)
    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return enrollment

@router.get("/user/{user_id}", response_model=List[Enrollment])
def get_enrollments_for_user(user_id: str):
    return enrollment_service.get_enrollments_for_user(user_id)

@router.get("/course/{course_id}", response_model=List[Enrollment])
def get_enrollments_by_course(course_id: str):
    return enrollment_service.get_enrollments_by_course(course_id)

@router.patch("/{enrollment_id}/complete", response_model=Enrollment)
def mark_completion(enrollment_id: str):
    enrollment = enrollment_service.mark_completion(enrollment_id)
    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return enrollment
