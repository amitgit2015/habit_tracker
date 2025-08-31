# Pydantic models for users

from pydantic import BaseModel, EmailStr
from typing import List, Optional

class User(BaseModel):
    id: int
    name: str
    email: EmailStr # Ensures valid email format
    age: Optional[str] = None # Optional field