from sqlalchemy import Column, String, Boolean, Enum
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel
from .enums import UserRole

class User(BaseModel):
    __tablename__ = "users"

    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    student_profile = relationship("StudentProfile",back_populates="user")
    recruiter_profile = relationship("RecruiterProfile",back_populates="user")
