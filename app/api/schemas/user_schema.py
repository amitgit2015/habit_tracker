# Pydantic models for users

from pydantic import BaseModel, EmailStr
from typing import List, Optional

class UserCreate(BaseModel):
    id: int
    username: str
    email: EmailStr
    password_hash: str
    role: str  # New role field

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str  # New role field

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password_hash: Optional[str] = None
    role: Optional[str] = None  # Role can be updated

    class Config:
        from_attributes = True