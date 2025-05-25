from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session, joinedload
from .schemas import UserResponse, UserCreate
from .models import User 
from core.database import get_db

# Routeur
UserRouter = APIRouter()

# 🔹 1. Ajouter un User
@UserRouter.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(**user.dict())
    db.add(db_user)
    db.flush()
    db.commit()
    return db_user

# 🔹 2. Récupérer tous les Users avec jointure sur l'adresse
@UserRouter.get("/Users/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    # Joindre l'adresse pour chaque utilisateur
    users = db.query(User).options(joinedload(User.adresse)).all()
    return users

# 🔹 3. Récupérer un user par ID avec jointure sur l'adresse
@UserRouter.get("/Users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    # Joindre l'adresse pour l'utilisateur spécifique
    user = db.query(User).filter(User.id == user_id).options(joinedload(User.adresse)).first()
    
    if user is None:
        raise HTTPException(status_code=404, detail="User non trouvé")
    
    return user

# 🔹 4. Mettre à jour un user
@UserRouter.put("/Users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_data: UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User non trouvé")
    
    for key, value in user_data.dict().items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user

# 🔹 5. Supprimer un User
@UserRouter.delete("/Users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User non trouvé")
    
    db.delete(user)
    db.commit()
    return {"message": "User supprimé avec succès"}
