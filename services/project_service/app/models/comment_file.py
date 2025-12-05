import uuid

from sqlalchemy import Column, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base, SCHEMA_NAME


class CommentFile(Base):
    __tablename__ = "comment_files"
    __table_args__ = (
        PrimaryKeyConstraint("comment_id", "file_id"),
        {"schema": SCHEMA_NAME},
    )

    comment_id = Column(
        UUID(as_uuid=True),
        ForeignKey(f"{SCHEMA_NAME}.comments.id"),
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

