# app/utils/auth_utils.py
# Utility functions for authentication, such as password hashing and verification
import bcrypt

# JWT handling
from jose import jwt, JWTError

# FastAPI imports
from fastapi import Depends, HTTPException, status

# For token creation and validation
from datetime import datetime, timedelta

# For OAuth2 password flow
from fastapi.security import OAuth2PasswordBearer

# Configuration
SECRET_KEY = "your-secret-key"  # Use a strong, random key in production!
ALGORITHM = "HS256" # Algorithm used for encoding the JWT
ACCESS_TOKEN_EXPIRE_MINUTES = 30 # Token expiry time in minutes

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Password hashing and verification
# Hash a plain password
def hash_password(plain_password: str) -> str:
    return bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Verify a plain password against a hashed password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

# Create a JWT access token
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Get current user from token  
# This function can be used as a dependency in routes to get the current user
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
            )
        return username
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )