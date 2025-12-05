import uuid

from sqlalchemy import Column, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base, SCHEMA_NAME


class ProjectFile(Base):
    __tablename__ = "project_files"
    __table_args__ = (
        PrimaryKeyConstraint("project_id", "file_id"),
        {"schema": SCHEMA_NAME},
    )

    project_id = Column(
        UUID(as_uuid=True),
        ForeignKey(f"{SCHEMA_NAME}.projects.id"),
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

