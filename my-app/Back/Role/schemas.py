from pydantic import BaseModel

class RoleBase(BaseModel):
    
    name: str

class RoleCreate(RoleBase):
    pass

class RoleRespnse(RoleBase):
    id: int

    class Config:
        from_attributes = True 
