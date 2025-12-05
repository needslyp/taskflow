import uuid

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base, SCHEMA_NAME


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": SCHEMA_NAME}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

