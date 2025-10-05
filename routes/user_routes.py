from fastapi import APIRouter, HTTPException
from typing import List
from schemas.user_schema import User, UserCreate
from services import user_service

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=User)
def create_user(user: UserCreate):
    return user_service.create_user(user)

@router.get("/", response_model=List[User])
def get_users():
    return user_service.get_users()

@router.get("/{user_id}", response_model=User)
def get_user(user_id: str):
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=User)
def update_user(user_id: str, user: UserCreate):
    updated = user_service.update_user(user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@router.delete("/{user_id}")
def delete_user(user_id: str):
    success = user_service.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

@router.patch("/{user_id}/deactivate", response_model=User)
def deactivate_user(user_id: str):
    user = user_service.deactivate_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
