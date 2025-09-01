# habit_tracker

This is user management service where user can login, user roles will be created , Admin can create , update and delete the user

Project structure :

habit_tracker/
│
├── app
│   ├── __init__.py
│   ├── main.py                # Entry point for FastAPI app
│   ├── api/                   # API-related code
│   │   ├── __init__.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── users.py       # User-related endpoints
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── user.py        # Pydantic models for users
│   │   ├── dependencies/
│   │   │   ├── __init__.py
│   │   │   ├── database.py    # Database connection logic
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py          # Configuration (e.g., environment variables)
│   │   ├── database.py        # Database setup (e.g., SQLAlchemy)
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py            # Database models (e.g., SQLAlchemy models)
│   ├── services/
│   │   ├── __init__.py
│   │   ├── user_service.py    # Business logic for user operations
│
├── tests/
│   ├── __init__.py
│   ├── test_users.py          # Tests for user endpoints
│
├── requirements.txt           # Project dependencies
├── .env                       # Environment variables
├── README.md                  # Project documentation