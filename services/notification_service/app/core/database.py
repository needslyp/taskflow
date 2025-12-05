import os

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

# PostgreSQL schema for notification_service
SCHEMA_NAME = "notification_service"

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://taskflow:taskflow@localhost:5432/taskflow_db",
)

engine = create_engine(DATABASE_URL, future=True)

# Create schema if it doesn't exist
with engine.begin() as conn:
    conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {SCHEMA_NAME}"))

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models with schema
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


