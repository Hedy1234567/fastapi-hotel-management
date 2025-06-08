from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from .schemas import RoleResponse, RoleCreate  # Utilisation de Role avec une majuscule
from .models import Role  # Utilisation de Role avec une majuscule
from core.database import get_db

# Routeur
roleRouter = APIRouter()

@roleRouter.post("/roles/")
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    db_role = Role(**role.dict())
    db.add(db_role)
    db.flush()  # pousse à la DB sans commit
    db.commit()

    return db_role


# 🔹 2. Récupérer tous les roles
@roleRouter.get("/roles/", response_model=list[RoleResponse])  # Utilisation de RoleResponse avec une majuscule
def get_roles(db: Session = Depends(get_db)):
    return db.query(Role).all()  # Utilisation de Role avec une majuscule

# 🔹 3. Récupérer un role par ID
@roleRouter.get("/roles/{role_id}", response_model=RoleResponse)  # Utilisation de RoleResponse avec une majuscule
def get_role(role_id: int, db: Session = Depends(get_db)):
    role = db.query(Role).filter(Role.id == role_id).first()  # Utilisation de Role avec une majuscule
    if role is None:
        raise HTTPException(status_code=404, detail="role non trouvé")
    return role

# 🔹 4. Mettre à jour un role
@roleRouter.put("/roles/{role_id}", response_model=RoleResponse)  # Utilisation de RoleResponse avec une majuscule
def update_role(role_id: int, role_data: RoleCreate, db: Session = Depends(get_db)):
    role = db.query(Role).filter(Role.id == role_id).first()  # Utilisation de Role avec une majuscule
    if role is None:
        raise HTTPException(status_code=404, detail="role non trouvé")
    
    for key, value in role_data.dict().items():
        setattr(role, key, value)

    db.commit()
    db.refresh(role)
    return role

# 🔹 5. Supprimer un role
@roleRouter.delete("/roles/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    role = db.query(Role).filter(Role.id == role_id).first()  # Utilisation de Role avec une majuscule
    if role is None:
        raise HTTPException(status_code=404, detail="role non trouvé")
    
    db.delete(role)
    db.commit()
    return {"message": "role supprimé avec succès"}
