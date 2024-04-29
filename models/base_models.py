from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.types import DateTime
import datetime

from db import Base

class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    
    created_at = Column(DateTime, default=datetime.datetime.now) 
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)