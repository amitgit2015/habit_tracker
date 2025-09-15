from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserCreate(BaseModel):
    """Schema for creating a new user (input only)."""
    username: str = Field(..., example="alice")
    email: EmailStr = Field(..., example="alice@example.com")
    password: str = Field(..., example="strongpassword123")
    role: str = Field(..., example="user")

    # Forbid extra fields not defined in the model
    class Config:
        extra = "forbid"

class UserOut(BaseModel):
    """Schema for returning user data (output only)."""
    id: int
    username: str
    email: EmailStr
    role: str

    # ORM mode to work with SQLAlchemy models
    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    """Schema for updating user data (input, all fields optional)."""
    username: Optional[str] = Field(None, example="newname")
    email: Optional[EmailStr] = Field(None, example="newemail@example.com")
    password: Optional[str] = Field(None, example="newpassword123")
    role: Optional[str] = Field(None, example="admin")

    # Forbid extra fields not defined in the model
    class Config:
        extra = "forbid" # Disallow extra fields
        from_attributes = True # Enable ORM mode