from sqlalchemy import Column, Integer, String
from core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(225), index=True)
    adresse = Column(String(225), index=True)
    email = Column(String(225))
    role= Column(String(225))


