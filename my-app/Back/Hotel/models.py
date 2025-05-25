from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from core.database import Base
from .schemas import HotelBase, AdresseBase  # Assure-toi que ces schemas existent

# TABLE HOTEL
class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(225))
    rating = Column(Integer)
    adresse_id = Column(Integer, ForeignKey("adresse.id"))
    suitesNumber = Column(Integer)
    doubleRoomNumber = Column(Integer)
    simpleRoomNumber = Column(Integer)
    Description = Column(Text)

    adresse = relationship("Adresse", back_populates="hotels")

    @staticmethod
    def createHotel(db: Session, hotel: HotelBase, id_adresse: int):
        db_hotel = Hotel(**hotel.dict())
        db_hotel.adresse_id = id_adresse
        db.add(db_hotel)
        db.commit()
        db.refresh(db_hotel)
        return db_hotel.id


# TABLE ADRESSE
class Adresse(Base):
    __tablename__ = "adresse"

    id = Column(Integer, primary_key=True, index=True)
    streetName = Column(String(225), index=True)
    streetNumber = Column(Integer)
    postalCode = Column(Integer)
    city = Column(String(225))
    country = Column(String(225))

    hotels = relationship("Hotel", back_populates="adresse")
    user = relationship("User", back_populates="adresse")

    @staticmethod
    def createAdresse(db: Session, adresse: AdresseBase):
        db_adresse = Adresse(**adresse.dict())
        db.add(db_adresse)
        db.commit()
        db.refresh(db_adresse)
        return db_adresse.id
