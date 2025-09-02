# Entry point for User Management FastAPI application   

from fastapi import FastAPI
from .api.routes import users_routes


app = FastAPI()
app.include_router(users_routes.router)
