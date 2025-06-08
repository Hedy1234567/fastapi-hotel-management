from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

class ReservationBase(BaseModel):
    full_name: str
    email : str
    phone_number: int
    booking_reference_number: int
    check_in_date: date
    check_out_date: date
    number_of_guests: int
    id_type: str
    id_number: int
    emergency_contact_name: str
    emergency_contact_phone: int
    requests: Optional[str] = None
    language: str
    room_type: str

class ReservationCreate(ReservationBase):
    pass

class ReservationResponse(ReservationBase):
    id: int

    class Config:
        from_attributes = True
