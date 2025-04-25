from pydantic import BaseModel

class ClientBase(BaseModel):
    name: str
    adresse: str
    number: int
    email: str

class ClientCreate(ClientBase):
    pass

class ClientResponse(ClientBase):
    id: int

    class Config:
        from_attributes = True
