from fastapi import FastAPI, Depends, HTTPException
from fastapi import APIRouter 

from sqlalchemy.orm import Session



from .schemas import UserResponse,UserCreate 
from .models import User
from core.database import get_db
# Création du routeur pour les User
UserRouter = APIRouter()

# 🔹 1. Ajouter un User
@UserRouter.post("/Users/", response_model=UserResponse)
def create_User(User: UserCreate, db: Session = Depends(get_db)):
    db_User = User(**User.dict())
    db.add(db_User)
    db.commit()
    db.refresh(db_User)
    return db_User

# 🔹 2. Récupérer tous les Users
UserRouter.get("/Users/", response_model=list[UserResponse])
def get_Users(db: Session = Depends(get_db)):
    return db.query(User).all()

# 🔹 3. Récupérer un user par ID
UserRouter.get("/Users/{User_id}", response_model=UserResponse)
def get_User(User_id: int, db: Session = Depends(get_db)):
    User = db.query(User).filter(User.id == User_id).first()
    if User is None:
        raise HTTPException(status_code=404, detail="User non trouvé")
    return User

# 🔹 4. Mettre à jour un user
UserRouter.put("/Users/{User_id}", response_model=UserResponse)
def update_User(User_id: int, User_data: UserCreate, db: Session = Depends(get_db)):
    User = db.query(User).filter(User.id == User_id).first()
    if User is None:
        raise HTTPException(status_code=404, detail="User non trouvé")
    
    for key, value in User_data.dict().items():
        setattr(User, key, value)

    db.commit()
    db.refresh(User)
    return User

# 🔹 5. Supprimer un User
UserRouter.delete("/Users/{User_id}")
def delete_User(User_id: int, db: Session = Depends(get_db)):
    User = db.query(User).filter(User.id == User_id).first()
    if User is None:
        raise HTTPException(status_code=404, detail="User non trouvé")
    
    db.delete(User)
    db.commit()
    return {"message": "User supprimé avec succès"}
