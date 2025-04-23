from pydantic import BaseModel

class UserBase(BaseModel):
    id:int
    name: str
    email: str
    role:str
    adresse: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    
    class Config:
        from_attributes = True 
