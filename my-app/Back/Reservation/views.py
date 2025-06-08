from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from .schemas import  ReservationCreate, ReservationResponse # Utilisation de Reservation avec une majuscule
from .models import Reservation  # Utilisation de Reservation avec une majuscule
from core.database import get_db

# Routeur
reservationRouter = APIRouter()

@reservationRouter.post("/reservations/")
def create_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    db_reservation = Reservation(**reservation.dict())
    db.add(db_reservation)
    db.flush()  # pousse à la DB sans commit
    db.commit()
    return db_reservation 


# 🔹 2. Récupérer tous les Reservations
@reservationRouter.get("/Reservations/", response_model=list[ReservationResponse])  # Utilisation de ReservationResponse avec une majuscule
def get_Reservations(db: Session = Depends(get_db)):
    return db.query(Reservation).all()  # Utilisation de Reservation avec une majuscule

# 🔹 3. Récupérer un Reservation par ID
@reservationRouter.get("/Reservations/{Reservation_id}", response_model=ReservationResponse)  # Utilisation de ReservationResponse avec une majuscule
def get_Reservation(Reservation_id: int, db: Session = Depends(get_db)):
    Reservation = db.query(Reservation).filter(Reservation.id == Reservation_id).first()  # Utilisation de Reservation avec une majuscule
    if Reservation is None:
        raise HTTPException(status_code=404, detail="Reservation non trouvé")
    return Reservation

# 🔹 4. Mettre à jour un Reservation
@reservationRouter.put("/Reservations/{Reservation_id}", response_model=ReservationResponse)  # Utilisation de ReservationResponse avec une majuscule
def update_Reservation(Reservation_id: int, Reservation_data: ReservationCreate, db: Session = Depends(get_db)):
    Reservation = db.query(Reservation).filter(Reservation.id == Reservation_id).first()  # Utilisation de Reservation avec une majuscule
    if Reservation is None:
        raise HTTPException(status_code=404, detail="Reservation non trouvé")
    
    for key, value in Reservation_data.dict().items():
        setattr(Reservation, key, value)

    db.commit()
    db.refresh(Reservation)
    return Reservation

# 🔹 5. Supprimer un Reservation
@reservationRouter.delete("/Reservations/{Reservation_id}")
def delete_Reservation(Reservation_id: int, db: Session = Depends(get_db)):
    Reservation = db.query(Reservation).filter(Reservation.id == Reservation_id).first()  # Utilisation de Reservation avec une majuscule
    if Reservation is None:
        raise HTTPException(status_code=404, detail="Reservation non trouvé")
    
    db.delete(Reservation)
    db.commit()
    return {"message": "Reservation supprimé avec succès"}
