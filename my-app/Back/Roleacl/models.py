from sqlalchemy import Boolean, Column, Integer, String, Text
from core.database import Base

class RoleAcl(Base):
    __tablename__ = "rolesacl"

    id = Column(Integer, primary_key=True, index=True)
    id_role = Column(Integer)
    id_task = Column(Integer)
    permission=Column(Boolean) 

