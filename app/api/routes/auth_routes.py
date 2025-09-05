from ..schemas.user_auth_schema import UserLogin
from typing import List, Optional
from app.api.dependencies.db_session import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils.auth_utils import verify_password
from app.models.user_model import UserModel  # Make sure this import path matches your project structure
# Example: define the function and ensure login_data is passed in and has username and password
# Assume login_data is provided as a parameter to a function or endpoint, e.g.:
router = APIRouter()

def authenticate_user(db: Session, login_data: UserLogin):
    user = db.query(UserModel).filter(UserModel.username == login_data.username).first()
    if not user or not verify_password(login_data.password, user.password_hash):
        return None
    return user # Return user object if authentication is successful

# User login endpoint
@router.post("/login")
def login(login_data: UserLogin, db: Session = Depends(get_db)):
    user = authenticate_user(db, login_data)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    # Generate and return a token or session info as needed
    return {"message": "Login successful"}    