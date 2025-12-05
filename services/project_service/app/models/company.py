import uuid

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base, SCHEMA_NAME


class Company(Base):
    __tablename__ = "companies"
    __table_args__ = {"schema": SCHEMA_NAME}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

