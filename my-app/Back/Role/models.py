from sqlalchemy import Column, Integer, String, Text
from core.database import Base

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(225), index=True)
    Description = Column(Text)


