from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from .schemas import ClientResponse, ClientCreate
from .models import Client
from core.database import get_db

clientRouter = APIRouter()

# 🔹 1. Créer un client
@clientRouter.post("/clients/", response_model=ClientResponse)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    db_client = Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

# 🔹 2. Récupérer tous les clients
@clientRouter.get("/clients/", response_model=list[ClientResponse])
def get_clients(db: Session = Depends(get_db)):
    return db.query(Client).all()

# 🔹 3. Récupérer un client par ID
@clientRouter.get("/clients/{client_id}", response_model=ClientResponse)
def get_client(client_id: int, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.id == client_id).first()
    if client is None:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return client

# 🔹 4. Mettre à jour un client
@clientRouter.put("/clients/{client_id}", response_model=ClientResponse)
def update_client(client_id: int, client_data: ClientCreate, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.id == client_id).first()
    if client is None:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    
    for key, value in client_data.dict().items():
        setattr(client, key, value)

    db.commit()
    db.refresh(client)
    return client

# 🔹 5. Supprimer un client
@clientRouter.delete("/clients/{client_id}")
def delete_client(client_id: int, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.id == client_id).first()
    if client is None:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    
    db.delete(client)
    db.commit()
    return {"message": "Client supprimé avec succès"}
