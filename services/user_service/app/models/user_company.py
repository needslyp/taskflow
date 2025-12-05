import uuid

from sqlalchemy import Column, String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base, SCHEMA_NAME


class UserCompany(Base):
    __tablename__ = "user_companies"
    __table_args__ = (
        PrimaryKeyConstraint("user_id", "company_id"),
        {"schema": SCHEMA_NAME},
    )

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey(f"{SCHEMA_NAME}.users.id"),
        nullable=False,
    )
    company_id = Column(
        UUID(as_uuid=True),
        ForeignKey(f"{SCHEMA_NAME}.companies.id"),
        nullable=False,
    )
    role = Column(String, nullable=False)

