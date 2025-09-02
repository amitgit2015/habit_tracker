from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Database connection parameters
db_user = "postgres"
db_password = "my_password"
db_host = "localhost"
db_port = "5432"
db_name = "user_management"

# Create the connection string
connection_string = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Create the SQLAlchemy engine
engine = create_engine(connection_string, echo=True)  # echo=True logs SQL queries for debugging

# Optional: Create a session for ORM usage
Session = sessionmaker(bind=engine)
session = Session()

# Test the connection
try:
    # Execute a simple query
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        version = result.fetchone()
        print(f"Connected to PostgreSQL: {version[0]}")
except Exception as e:
    print(f"Error connecting to PostgreSQL: {e}")

# Execute select query example
with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM users;"))
    users = result.fetchall()
    for user in users:
        print(user)
# Close the session (if using ORM)
session.close()