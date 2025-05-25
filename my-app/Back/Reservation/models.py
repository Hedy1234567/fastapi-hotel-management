from sqlalchemy import Column, Date, Integer, String, Text
from core.database import Base

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255))
    email = Column(String(255))
    phone_number = Column(Integer)
    booking_reference_number = Column(Integer)
    check_in_date = Column(Date)
    check_out_date = Column(Date)
    number_of_guests = Column(Integer)
    id_type = Column(String(255))
    id_number = Column(Integer)
    emergency_contact_name = Column(String(255))
    emergency_contact_phone = Column(Integer)
    requests = Column(String(255))
    language = Column(String(255))
    room_type = Column(String(255))
