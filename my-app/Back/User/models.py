from sqlalchemy import Column, ForeignKey, Integer, String
from core.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from core.database import Base
from .schemas import UserBase # Assure-toi que ces schemas existent
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(225), index=True)
    adresse_id = Column(Integer, ForeignKey("adresse.id"))
    adresse = Column(String(225), index=True)
    email = Column(String(225))
    role= Column(String(225))

    adresse = relationship("Adresse", back_populates="user")

