from pydantic import BaseModel

class RoleBase(BaseModel):
    id:int
    name: str
    Description: str

class RoleCreate(RoleBase):
    pass

class RoleResponse(RoleBase):
    id: int
    
    class Config:
        from_attributes = True
