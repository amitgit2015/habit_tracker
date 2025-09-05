# Pydantic models for users

from pydantic import BaseModel, EmailStr
from typing import List, Optional

class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    password_hash: str
    role: str  # New role field

    class Config:
        from_attributes = True