from fastapi import FastAPI, Depends, HTTPException
from fastapi import APIRouter 

from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload




from .schemas import HotelBase, HotelResponse,HotelCreate 
from .models import Adresse, Hotel
from core.database import get_db
# Création du routeur pour les hôtels
hotelRouter = APIRouter()

# 🔹 1. Ajouter un hôtel
@hotelRouter.post("/hotels/")
def create_hotel(hotel: HotelCreate, db: Session = Depends(get_db)):
    id_adresse = Adresse.createAdresse(db, hotel.adresse)
    # Convertir en dict, retirer l'adresse, puis retransformer en HotelCreate
    hotel_data = hotel.dict()
    hotel_data.pop("adresse")

    hotel_base = HotelBase(**hotel_data)  # HotelBase doit correspondre à ce que attend createHotel
    hotel_id = Hotel.createHotel(db, hotel_base, id_adresse)

    return {"message": "Hotel Created succeffully", "id" : hotel_id}


# 🔹 2. Récupérer tous les hôtels
@hotelRouter.get("/hotels/", response_model=list[HotelResponse])
def get_hotels(db: Session = Depends(get_db)):
    #jointure avec la table adresse pour extraire les info d'adresse 
    return db.query(Hotel).options(joinedload(Hotel.adresse)).all()



# 🔹 3. Récupérer un hôtel par ID
@hotelRouter.get("/hotels/{hotel_id}", response_model=HotelResponse)
def get_hotel(hotel_id: int, db: Session = Depends(get_db)):
    #jointure avec table adreese 
    hotel = db.query(Hotel).options(joinedload(Hotel.adresse)).filter(Hotel.id == hotel_id).first()
    if hotel is None:
        raise HTTPException(status_code=404, detail="Hôtel non trouvé")
    return hotel

# 🔹 4. Mettre à jour un hôtel
@hotelRouter.put("/hotels/{hotel_id}", response_model=HotelResponse)
def update_hotel(hotel_id: int, hotel_data: HotelCreate, db: Session = Depends(get_db)):
    hotel = db.query(Hotel).filter(Hotel.id == hotel_id).first()
    if hotel is None:
        raise HTTPException(status_code=404, detail="Hôtel non trouvé")
    
    for key, value in hotel_data.dict().items():
        setattr(hotel, key, value)

    db.commit()
    db.refresh(hotel)
    return hotel

# 🔹 5. Supprimer un hôtel
@hotelRouter.delete("/hotels/{hotel_id}")
def delete_hotel(hotel_id: int, db: Session = Depends(get_db)):
    hotel = db.query(Hotel).filter(Hotel.id == hotel_id).first()
    if hotel is None:
        raise HTTPException(status_code=404, detail="Hôtel non trouvé")
    
    db.delete(hotel)
    db.commit()
    return {"message": "Hôtel supprimé avec succès"}
