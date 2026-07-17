from sqlalchemy import Column, String,Integer,Float
from sqlalchemy import ForeignKey 
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.models.base_model import BaseModel

class StudentProfile(BaseModel):
    __tablename__ = "students_profiles"
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False,
        unique=True
        )
    first_name = Column(String,nullable=False)
    last_name = Column(String,nullable=False)
    phone = Column(String,nullable=False)
    university = Column(String, nullable=False)
    degree = Column(String, nullable=False)
    branch = Column(String, nullable=False)
    graduation_year = Column(Integer,nullable=False)
    cgpa = Column(Float,nullable=False)
    github_url = Column(String,nullable=False)
    linkedin_url = Column(String,nullable=False)
    resume_url = Column(String,nullable=False)
    profile_photo_url = Column(String,nullable=False)
    bio = Column(String,nullable=True)
    expected_stipend = Column(Float,nullable=False)

    user = relationship("User",back_populates="student_profile")
    applications = relationship("Application",back_populates="student_profile")
