from pydantic import BaseModel

class RoleAclBase(BaseModel):
    id:int
    id_role: int
    id_task: int
    permission : bool

class RoleAclCreate(RoleAclBase):
    pass

class RoleAclResponse(RoleAclBase):
    id: int
    
    class Config:
        from_attributes = True
