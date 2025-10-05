from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: EmailStr
    is_active: Optional[bool] = True

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: str
