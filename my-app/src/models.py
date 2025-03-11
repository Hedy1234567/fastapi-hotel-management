from sqlalchemy import Column, Integer, String
from .database import Base

class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    city = Column(String)
    rating = Column(Integer)
