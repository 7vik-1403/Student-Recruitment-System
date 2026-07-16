from sqlalchemy import String,Column,DateTime,ForeignKey,UUID,Enum,Text
from sqlalchemy import Integer,Float
from sqlalchemy.orm import relationship
from .base_model import BaseModel
from .enums import EmploymentType , WorkMode , JobStatus

class Job(BaseModel):
    __tablename__ = 'jobs'

    company_id = Column(UUID(as_uuid=True),
                        ForeignKey("companies.id"),
                        nullable=False,
                        unique=True)
    recruiter_id = Column(UUID(as_uuid=True),
                          ForeignKey("recruiter_profile.id"),
                          nullable=False,
                          unique=True)
    title = Column(String,nullable=False)
    description = Column(Text,nullable=False)
    employment_type = Column(Enum(EmploymentType),nullable=False)
    work_mode = Column(Enum(WorkMode),nullable=False)
    location = Column(String,nullable=False)
    salary_min = Column(Float,nullable=False)
    salary_max = Column(Float,nullable=False)
    experience_required = Column(Integer,nullable=False)
    vacancies = Column(Integer,nullable=False)
    application_deadline = Column(DateTime,nullable=False)
    status = Column(Enum(JobStatus),nullable=False)
    
    company = relationship(
    "Company",
    back_populates="jobs"
)
    recruiter = relationship(
    "RecruiterProfile",
    back_populates="jobs"
)
     





# id
# company_id
# recruiter_id
# title
# description
# employment_type
# work_mode
# location
# salary_min
# salary_max
# experience_required
# vacancies
# application_deadline
# status
# created_at
# updated_at