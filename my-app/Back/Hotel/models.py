from sqlalchemy import Column, Integer, String
from core.database import Base

class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(225)) 
    city = Column(String(225))
    rating = Column(Integer)

class Adresse(Base):
    __tablename__ = "Adresse"

    id = Column(Integer, primary_key=True, index=True)
    streetname = Column(String(225), index=True)
    streetnumber = Column(Integer)
    postalcode = Column(Integer)
    country=Column(String(225))
