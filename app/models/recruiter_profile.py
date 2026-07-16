from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import UUID
from sqlalchemy.orm import relationship
from .base_model import BaseModel
class RecruiterProfile(BaseModel):
    __tablename__ = "recruiter_profile"

    user_id = Column(UUID(as_uuid=True),
                     ForeignKey('users.id'),
                     unique=True,
                     nullable=False )
    company_id = Column(UUID(as_uuid=True),
                        ForeignKey('companies.id',use_alter=True),
                        nullable=False,
                        unique=True,
                        )
    first_name = Column(String,nullable=False)
    last_name = Column(String,nullable=False)
    phone = Column(String,nullable=False,unique=True)
    bio = Column(String,nullable=False)
    profile_photo_url = Column(String)
    designation = Column(String,nullable=False)

    user = relationship("User",back_populates="recruiter_profile",uselist=False)
    company = relationship("Company",back_populates="recruiter_profile")
    jobs = relationship(
    "Job",
    back_populates="recruiter_profile"
)
