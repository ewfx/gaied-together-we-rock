from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Email(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True, index=True)
    body = Column(Text, nullable=False)
    category = Column(String, nullable=False)

    attachments = relationship("Attachment", back_populates="email")

class Attachment(Base):
    __tablename__ = "attachments"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    file_type = Column(String, nullable=False)
    classification = Column(String, nullable=False)
    email_id = Column(Integer, ForeignKey("emails.id"))

    email = relationship("Email", back_populates="attachments")
