from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from .schemas import RoleAclCreate, RoleAclResponse  # Utilisation de roleacl avec une majuscule
from .models import RoleAcl   # Utilisation de roleacl avec une majuscule
from core.database import get_db

# Routeur
roleaclRouter = APIRouter()

@roleaclRouter.post("/roleacls/")
def create_roleacl(roleacl: RoleAclCreate, db: Session = Depends(get_db)):
    db_roleacl = RoleAcl(**roleacl.dict())
    db.add(db_roleacl)
    db.flush()  # pousse à la DB sans commit
    db.commit()

    return db_roleacl


# 🔹 2. Récupérer tous les roleacls
@roleaclRouter.get("/roleacls/", response_model=list[RoleAclResponse])  # Utilisation de roleaclResponse avec une majuscule
def get_roleacls(db: Session = Depends(get_db)):
    return db.query(RoleAcl).all()  # Utilisation de roleacl avec une majuscule

# 🔹 3. Récupérer un roleacl par ID
@roleaclRouter.get("/roleacls/{roleacl_id}", response_model=RoleAclResponse)  # Utilisation de roleaclResponse avec une majuscule
def get_roleacl(roleacl_id: int, db: Session = Depends(get_db)):
    roleacl = db.query(roleacl).filter(roleacl.id == roleacl_id).first()  # Utilisation de roleacl avec une majuscule
    if roleacl is None:
        raise HTTPException(status_code=404, detail="roleacl non trouvé")
    return roleacl

# 🔹 4. Mettre à jour un roleacl
@roleaclRouter.put("/roleacls/{roleacl_id}", response_model=RoleAclResponse)  # Utilisation de roleaclResponse avec une majuscule
def update_roleacl(roleacl_id: int, roleacl_data: RoleAclCreate, db: Session = Depends(get_db)):
    roleacl = db.query(roleacl).filter(roleacl.id == roleacl_id).first()  # Utilisation de roleacl avec une majuscule
    if roleacl is None:
        raise HTTPException(status_code=404, detail="roleacl non trouvé")
    
    for key, value in roleacl_data.dict().items():
        setattr(roleacl, key, value)

    db.commit()
    db.refresh(roleacl)
    return roleacl

# 🔹 5. Supprimer un roleacl
@roleaclRouter.delete("/roleacls/{roleacl_id}")
def delete_roleacl(roleacl_id: int, db: Session = Depends(get_db)):
    roleacl = db.query(roleacl).filter(roleacl.id == roleacl_id).first()  # Utilisation de roleacl avec une majuscule
    if roleacl is None:
        raise HTTPException(status_code=404, detail="roleacl non trouvé")
    
    db.delete(roleacl)
    db.commit()
    return {"message": "roleacl supprimé avec succès"}
