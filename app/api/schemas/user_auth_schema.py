# Pydantic models for users login

from pydantic import BaseModel, EmailStr
from typing import List, Optional

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str

    class Config:
        from_attributes = True