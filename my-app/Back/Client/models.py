from sqlalchemy import Column, Integer, String, Text
from core.database import Base

class Role(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(225), index=True)
    number =  Column(int(225))
    adresse = Column(String(225), index=True)
    email = Column(String(225))
