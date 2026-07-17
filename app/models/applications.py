from sqlalchemy import String, Column,Integer,ForeignKey,UniqueConstraint,UUID,Enum
from sqlalchemy.orm import relationship
from .base_model import BaseModel
from .enums import ApplicationStatus

class Application(BaseModel):
    __tablename__ = "applications"

    student_id = Column(UUID(as_uuid=True),
                        ForeignKey('students_profile.id'),nullable=False)
    job_id = Column(UUID(as_uuid=True),
                    ForeignKey('jobs.id'),nullable=False)
    status = Column(Enum(ApplicationStatus),nullable=False)
    resume_snapshot_url = Column(String,nullable=False)

    __table_args__ = (UniqueConstraint('student_id','job_id',name="uq_job_applications"))
    
    jobs = relationship('Job',back_populates='applications')
    student_profile = relationship('StudentProfile',back_populates='applications')


#     id
# student_id
# job_id
# status
# cover_letter
# resume_snapshot_url
# applied_at
# updated_at