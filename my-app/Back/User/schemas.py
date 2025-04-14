from pydantic import BaseModel

class UserBase(BaseModel):
    Age: int
    email: str
    Number:int
    name: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True 
