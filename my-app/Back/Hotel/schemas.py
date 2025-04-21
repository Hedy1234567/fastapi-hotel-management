from pydantic import BaseModel


class AdresseBase(BaseModel):
    streetName: str
    streetNumber: int
    postalCode : int 
    city : str
    country: str
 
class HotelBase(BaseModel):
    name: str
    rating: int
    suitesNumber : int
    doubleRoomNumber : int
    simpleRoomNumber : int
    Description : str



class HotelCreate(HotelBase):
    adresse : AdresseBase

class HotelResponse(HotelBase):
    id: int

    class Config:
        from_attributes = True 
