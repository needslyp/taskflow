import uuid

from sqlalchemy import Column, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base, SCHEMA_NAME


class TaskFile(Base):
    __tablename__ = "task_files"
    __table_args__ = (
        PrimaryKeyConstraint("task_id", "file_id"),
        {"schema": SCHEMA_NAME},
    )

    task_id = Column(
        UUID(as_uuid=True),
        ForeignKey(f"{SCHEMA_NAME}.tasks.id"),
        nullable=False,
    )
    file_id = Column(
        UUID(as_uuid=True),
        ForeignKey(f"{SCHEMA_NAME}.files.id"),
        nullable=False,
    )
    uploaded_by = Column(
        UUID(as_uuid=True),
        ForeignKey(f"{SCHEMA_NAME}.users.id"),
        nullable=False,
    )

