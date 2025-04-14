from fastapi import FastAPI, Depends, HTTPException
from fastapi import APIRouter 

from sqlalchemy.orm import Session



from .schemas import RoleResponse,RoleCreate 
from .models import Role
from core.database import get_db
# Création du routeur pour les Role
RoleRouter = APIRouter()

# 🔹 1. Ajouter un Role
@RoleRouter.post("/Roles/", response_model=RoleResponse)
def create_Role(Role: RoleCreate, db: Session = Depends(get_db)):
    db_Role = Role(**Role.dict())
    db.add(db_Role)
    db.commit()
    db.refresh(db_Role)
    return db_Role

# 🔹 2. Récupérer tous les Roles
RoleRouter.get("/Roles/", response_model=list[RoleResponse])
def get_Roles(db: Session = Depends(get_db)):
    return db.query(Role).all()

# 🔹 3. Récupérer un Role par ID
RoleRouter.get("/Roles/{Role_id}", response_model=RoleResponse)
def get_Role(Role_id: int, db: Session = Depends(get_db)):
    Role = db.query(Role).filter(Role.id == Role_id).first()
    if Role is None:
        raise HTTPException(status_code=404, detail="Role non trouvé")
    return Role

# 🔹 4. Mettre à jour un Role
RoleRouter.put("/Roles/{Role_id}", response_model=RoleResponse)
def update_Role(Role_id: int, Role_data: RoleCreate, db: Session = Depends(get_db)):
    Role = db.query(Role).filter(Role.id == Role_id).first()
    if Role is None:
        raise HTTPException(status_code=404, detail="Role non trouvé")
    
    for key, value in Role_data.dict().items():
        setattr(Role, key, value)

    db.commit()
    db.refresh(Role)
    return Role

# 🔹 5. Supprimer un Role
RoleRouter.delete("/Roles/{Role_id}")
def delete_Role(Role_id: int, db: Session = Depends(get_db)):
    Role = db.query(Role).filter(Role.id == Role_id).first()
    if Role is None:
        raise HTTPException(status_code=404, detail="Role non trouvé")
    
    db.delete(Role)
    db.commit()
    return {"message": "Role supprimé avec succès"}
