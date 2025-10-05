import random
from schemas.course_schema import Course, CourseCreate

# In-memory storage for courses
courses_db = []

def create_course(course_data: CourseCreate) -> Course:
    """
    Create a course with a unique 6-digit string ID
    """
    # Generate a random 6-digit ID and ensure it’s unique
    new_id = str(random.randint(100000, 999999))
    while any(course.id == new_id for course in courses_db):
        new_id = str(random.randint(100000, 999999))
    
    course = Course(id=new_id, **course_data.dict())
    courses_db.append(course)
    return course

def get_courses():
    return courses_db

def get_course(course_id: str):
    """
    Retrieve a course by string ID
    """
    for course in courses_db:
        if course.id == course_id:
            return course
    return None

def update_course(course_id: str, course_data: CourseCreate):
    """
    Update a course by string ID
    """
    for index, course in enumerate(courses_db):
        if course.id == course_id:
            updated_course = Course(id=course_id, **course_data.dict())
            courses_db[index] = updated_course
            return updated_course
    return None

def delete_course(course_id: str) -> bool:
    """
    Delete a course by string ID
    """
    for index, course in enumerate(courses_db):
        if course.id == course_id:
            courses_db.pop(index)
            return True
    return False

def close_enrollment(course_id: str):
    """
    Close enrollment for a course by string ID
    """
    course = get_course(course_id)
    if course:
        course.is_open = False
        return course
    return None
