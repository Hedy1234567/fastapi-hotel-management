from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database

app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
models.Base.metadata.create_all(bind=database.engine)

# Dépendance pour la session DB
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🔹 1. Ajouter un hôtel
@app.post("/hotels/", response_model=schemas.HotelResponse)
def create_hotel(hotel: schemas.HotelCreate, db: Session = Depends(get_db)):
    db_hotel = models.Hotel(**hotel.dict())
    db.add(db_hotel)
    db.commit()
    db.refresh(db_hotel)
    return db_hotel

# 🔹 2. Récupérer tous les hôtels
@app.get("/hotels/", response_model=list[schemas.HotelResponse])
def get_hotels(db: Session = Depends(get_db)):
    return db.query(models.Hotel).all()

# 🔹 3. Récupérer un hôtel par ID
@app.get("/hotels/{hotel_id}", response_model=schemas.HotelResponse)
def get_hotel(hotel_id: int, db: Session = Depends(get_db)):
    hotel = db.query(models.Hotel).filter(models.Hotel.id == hotel_id).first()
    if hotel is None:
        raise HTTPException(status_code=404, detail="Hôtel non trouvé")
    return hotel

# 🔹 4. Mettre à jour un hôtel
@app.put("/hotels/{hotel_id}", response_model=schemas.HotelResponse)
def update_hotel(hotel_id: int, hotel_data: schemas.HotelCreate, db: Session = Depends(get_db)):
    hotel = db.query(models.Hotel).filter(models.Hotel.id == hotel_id).first()
    if hotel is None:
        raise HTTPException(status_code=404, detail="Hôtel non trouvé")
    
    for key, value in hotel_data.dict().items():
        setattr(hotel, key, value)

    db.commit()
    db.refresh(hotel)
    return hotel

# 🔹 5. Supprimer un hôtel
@app.delete("/hotels/{hotel_id}")
def delete_hotel(hotel_id: int, db: Session = Depends(get_db)):
    hotel = db.query(models.Hotel).filter(models.Hotel.id == hotel_id).first()
    if hotel is None:
        raise HTTPException(status_code=404, detail="Hôtel non trouvé")
    
    db.delete(hotel)
    db.commit()
    return {"message": "Hôtel supprimé avec succès"}
