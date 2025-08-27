from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List, Optional

app = FastAPI()

# Pydantic model for User
class User(BaseModel):
    id: int
    name: str
    email: EmailStr # Ensures valid email format
    age: Optional[str] = None # Optional field

# In-memory "database"
users_db = []

#
@app.post("/users/", response_model=User) # Create a new user and response with the created user
def create_user(user: User):
    if any(u.id == user.id for u in users_db):# Check for duplicate IDs
        raise HTTPException(status_code=400, detail="User ID already exists")
    users_db.append(user) # Add user to the "database"
    return user

@app.get("/users/", response_model=List[User]) #
def get_users():
    return users_db

@app.get("/users/{user_id}", response_model=User) # Get user by ID
def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    for idx, user in enumerate(users_db):
        if user.id == user_id:
            users_db[idx] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for idx, user in enumerate(users_db):
        if user.id == user_id:
            del users_db[idx]
            return {"detail": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")