from enum import Enum

class UserRole(str, Enum):
    ADMIN = "ADMIN"
    STUDENT = "STUDENT"
    RECRUITER = "RECRUITER"

class JobStatus(str, Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"

class ApplicationStatus(str, Enum):
    APPLIED = "APPLIED"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
