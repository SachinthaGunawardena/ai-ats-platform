from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Text
)

from sqlalchemy.sql import func

from app.database.session import Base


class Resume(Base):

    __tablename__ = "resumes"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    filename = Column(
        String,
        nullable=False
    )

    object_name = Column(
        String,
        nullable=False
    )

    file_path = Column(
        String,
        nullable=True
    )

    extracted_text = Column(
        Text,
        nullable=True
    )

    status = Column(
        String,
        default="uploaded"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )