from pydantic import BaseModel

class HotelBase(BaseModel):
    name: str
    city: str
    rating: int

class HotelCreate(HotelBase):
    pass

class HotelResponse(HotelBase):
    id: int

    class Config:
        from_attributes = True
