# FastAPI routes
# User-related endpoints


from ..schemas.user_schema import User 
from typing import List, Optional
from app.api.dependencies.db_session import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.user_model import User as UserModel

router = APIRouter()


# Create a new user
@router.post("/users/", response_model=User) # Create a new user and response with the created user
def create_user(user: User, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter((UserModel.username == user.username) | (UserModel.email == user.email)).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username or email already registered")
    new_user = UserModel(username=user.username, email=user.email, password_hash=user.password_hash, role=user.role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# Get all users
@router.get("/users/", response_model=List[User])
def get_users(db: Session = Depends(get_db)):
    return db.query(UserModel).all()

# Get user by ID    
@router.get("/users/{user_id}", response_model=User) 
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

# Update user by ID
@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User, db: Session = Depends(get_db)):
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
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return {"detail": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")

