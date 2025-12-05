import uuid

from sqlalchemy import Column, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base, SCHEMA_NAME


class TaskUser(Base):
    __tablename__ = "task_users"
    __table_args__ = (
        PrimaryKeyConstraint("task_id", "user_id"),
        {"schema": SCHEMA_NAME},
    )

    task_id = Column(
        UUID(as_uuid=True),
        ForeignKey(f"{SCHEMA_NAME}.tasks.id"),
        nullable=False,
    )
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey(f"{SCHEMA_NAME}.users.id"),
        nullable=False,
    )

