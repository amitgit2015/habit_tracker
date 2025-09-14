# FastAPI routes
# User-related endpoints


from ..schemas.user_schema import UserCreate, UserOut, UserUpdate  # Import UserCreate and UserOut schemas
from typing import List, Optional # Import List and Optional for type hinting
from app.api.dependencies.db_session import get_db # Import the database session dependency
from fastapi import APIRouter, Depends, HTTPException # Import FastAPI components
from sqlalchemy.orm import Session # Import SQLAlchemy Session
from app.models.user_model import UserModel # Import the UserModel
from app.utils.auth_utils import hash_password, verify_password # Import password hashing and verification functions
from app.utils.auth_utils import get_current_user  # Import the function to get the current user from the token

router = APIRouter()

# Create a new user
@router.post("/users/", response_model=UserOut) # Create a new user and response with the created user
def create_user(
    user: UserCreate, # User data from request body
    db: Session = Depends(get_db), # Database session
    current_user: str = Depends(get_current_user) # Current user from token dependency (added for authentication)
    ):
    db_user = db.query(UserModel).filter((UserModel.username == user.username) | (UserModel.email == user.email)).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username or email already registered")
    new_user = UserModel(
    username=user.username,
    email=user.email,
    password_hash=hash_password(user.password_hash),  # assuming user.password_hash is the plain password from the request
    role=user.role
)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# Get all users
@router.get("/users/", response_model=List[UserOut])
def get_users(
    db: Session = Depends(get_db),  # Database session
    current_user: str = Depends(get_current_user)  # Current user from token dependency (added for authentication) 
):
    return db.query(UserModel).all()

# Get user by ID
@router.get("/users/{user_id}", response_model=UserOut)
def get_user(
    user_id: int, # ID of the user to retrieve
    db: Session = Depends(get_db), # Database session
    current_user: str = Depends(get_current_user)  # Current user from token dependency (added for authentication)
    ):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

# Update user by ID
@router.put("/users/{user_id}", response_model=UserOut)
def update_user(
    user_id: int, # ID of the user to update
    updated_user: UserUpdate, db: Session = Depends(get_db), # Database session
    current_user: str = Depends(get_current_user)  # Current user from token dependency (added for authentication)
):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user:
        user.username = updated_user.username
        user.email = updated_user.email
        user.password_hash = updated_user.password_hash
        user.role = updated_user.role
        db.commit()
        db.refresh(user)
        return user
    raise HTTPException(status_code=404, detail="User not found")

# Delete user by ID
@router.delete("/users/{user_id}")
def delete_user(
    user_id: int, # ID of the user to delete
    db: Session = Depends(get_db), # Database session
    current_user: str = Depends(get_current_user)  # Current user from token dependency (added for authentication)
):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return {"detail": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")

