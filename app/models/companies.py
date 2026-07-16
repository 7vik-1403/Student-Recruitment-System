from sqlalchemy import String , Column,ForeignKey,Boolean,Integer
from sqlalchemy.orm import relationship
from .base_model import BaseModel

class Company(BaseModel):
    __tablename__ = "companies"

    name = Column(String,nullable=False,unique=True)
    description = Column(String,nullable=False)
    website = Column(String,nullable=False,unique=True)
    industry = Column(String,nullable=False)
    company_size = Column(String,nullable=False)
    headquarters = Column(String,nullable=False)
    founded_year = Column(Integer,nullable=False)
    logo_url = Column(String,nullable=False)
    verified = Column(Boolean,nullable=False,default=False)

    recruiter_profile = relationship("RecruiterProfile",back_populates="company")
    jobs = relationship("Job",back_populates="company")
# id
# name
# description
# website
# industry
# company_size
# headquarters
# founded_year
# logo_url
# verified
# created_at
# updated_at
