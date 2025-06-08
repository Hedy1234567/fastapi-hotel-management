from sqlalchemy import Column, Integer, String, Text
from core.database import Base

class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    


