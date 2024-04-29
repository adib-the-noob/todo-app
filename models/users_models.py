from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db import Base
from .base_models import BaseModel

class User(BaseModel):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    
    todo = relationship("Todo", back_populates="owner")

