# Entry point for User Management FastAPI application   

from fastapi import FastAPI
from .api.routes import users_routes, auth_routes


app = FastAPI()
app.include_router(users_routes.router)
app.include_router(auth_routes.router)  # Include auth routes as well
