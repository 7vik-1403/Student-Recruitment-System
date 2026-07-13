from sqlalchemy import Column, String, Boolean, Enum, Index
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

   
