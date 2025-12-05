import uuid
from datetime import date

from sqlalchemy import Column, String, Date
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base, SCHEMA_NAME


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": SCHEMA_NAME}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)
    avatar_url = Column(String, nullable=True)
    timezone = Column(String, nullable=True)
    created_at = Column(Date, nullable=False, default=date.today)

