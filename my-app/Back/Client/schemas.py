from pydantic import BaseModel

class ClientCreate(BaseModel):
    name: str
    number: int
    adresse: str
    email: str

    class Config:
        from_attributes = True  # ✅ remplace orm_mode (FastAPI 0.110+ avec Pydantic v2)

class ClientResponse(ClientCreate):
    id: int
