from sqlalchemy import Column, Integer, String
from core.database import Base

class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    Age = Column(Integer)
    email = Column(String)
    Number=Column(Integer)


