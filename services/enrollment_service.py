import random
import string
from schemas.enrollment_schema import Enrollment, EnrollmentCreate
from services.user_service import get_user
from services.course_service import get_course

# In-memory storage for enrollments
enrollments_db = []

def generate_enrollment_id() -> str:
    """Generate a unique alphanumeric ID for enrollment (e.g., ENR4F9A2)."""
    new_id = "ENR" + "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    # Ensure uniqueness
    while any(e.id == new_id for e in enrollments_db):
        new_id = "ENR" + "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return new_id

def enroll_user(enrollment_data: EnrollmentCreate) -> Enrollment:
    # Check user exists and is active
    user = get_user(enrollment_data.user_id)
    if not user:
        raise ValueError("User not found")
    if not user.is_active:
        raise ValueError("User is no1t active")

    # Check course exists and is open
    course = get_course(enrollment_data.course_id)
    if not course:
        raise ValueError("Course not found")
    if not course.is_open:
        raise ValueError("Course enrollment is closed")

    # Prevent duplicate enrollment
    for e in enrollments_db:
        if e.user_id == enrollment_data.user_id and e.course_id == enrollment_data.course_id:
            raise ValueError("User already enrolled in this course")

    enrollment_id = generate_enrollment_id()
    enrollment = Enrollment(id=enrollment_id, **enrollment_data.dict())
    enrollments_db.append(enrollment)
    return enrollment

def mark_completion(enrollment_id: str):
    for enrollment in enrollments_db:
        if enrollment.id == enrollment_id:
            enrollment.completed = True
            return enrollment
    return None

def get_enrollments_for_user(user_id: str):
    return [e for e in enrollments_db if e.user_id == user_id]

def get_all_enrollments():
    return enrollments_db

def get_enrollments_by_course(course_id: str):
    return [e for e in enrollments_db if e.course_id == course_id]

def get_enrollment(enrollment_id: str):
    for enrollment in enrollments_db:
        if enrollment.id == enrollment_id:
            return enrollment
    return None
