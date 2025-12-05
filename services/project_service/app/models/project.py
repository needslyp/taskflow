import uuid
from datetime import datetime, timezone

from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base, SCHEMA_NAME


class Project(Base):
    __tablename__ = "projects"
    __table_args__ = {"schema": SCHEMA_NAME}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    status = Column(String, nullable=False)
    deadline = Column(DateTime, nullable=True)
    company_id = Column(
        UUID(as_uuid=True),
        ForeignKey(f"{SCHEMA_NAME}.companies.id"),
        nullable=False,
    )
    created_at = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    is_private = Column(Boolean, nullable=False, default=False)

