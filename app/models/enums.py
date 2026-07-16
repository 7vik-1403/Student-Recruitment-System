from enum import Enum

class UserRole(str, Enum):
    ADMIN = "ADMIN"
    STUDENT = "STUDENT"
    RECRUITER = "RECRUITER"

class JobStatus(str, Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"
    PAUSED = "PAUSED"

class ApplicationStatus(str, Enum):
    APPLIED = "APPLIED"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"

class EmploymentType(str,Enum):
    INTERNSHIP = "INTERNSHIP"
    JOB = "JOB"
    PERFORMANCE_BASED = "PERFORMANCE_BASED"

class WorkMode(str,Enum):
    REMOTE = "REMOTE"
    ON_SITE = "ON_SITE"
    HYBRID = "HYBRID"
