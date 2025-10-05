from schemas.user_schema import User, UserCreate
import random
import string

# In-memory storage for users
users_db = []

def generate_user_id() -> str:
    """Generate a unique alphanumeric ID for users (e.g., USR4F9A2)."""
    new_id = "USR" + "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    while any(user.id == new_id for user in users_db):
        new_id = "USR" + "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return new_id

def create_user(user_data: UserCreate) -> User:
    user_id = generate_user_id()
    user = User(id=user_id, **user_data.dict())
    users_db.append(user)
    return user

def get_users():
    return users_db

def get_user(user_id: str):
    for user in users_db:
        if user.id == user_id:
            return user
    return None

def update_user(user_id: str, user_data: UserCreate):
    for user in users_db:
        if user.id == user_id:
            user.name = user_data.name
            user.email = user_data.email
            # Keep is_active as is
            return user
    return None

def delete_user(user_id: str) -> bool:
    for index, user in enumerate(users_db):
        if user.id == user_id:
            users_db.pop(index)
            return True
    return False

def deactivate_user(user_id: str):
    for user in users_db:
        if user.id == user_id:
            user.is_active = False
            return user
    return None
