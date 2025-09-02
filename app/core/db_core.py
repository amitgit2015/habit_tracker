from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from app.core import config

Base = declarative_base()
connection_string = f"postgresql+psycopg2://{config.db_user}:{config.db_password}@{config.db_host}:{config.db_port}/{config.db_name}"
engine = create_engine(connection_string, echo=True)