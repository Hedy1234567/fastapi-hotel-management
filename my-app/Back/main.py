from fastapi import FastAPI
import uvicorn
from core.database import engine, Base
from Hotel.views import hotelRouter
from User.views import UserRouter
from Role.views import roleRouter

# Initialisation de l'application FastAPI
app = FastAPI(
    title="Hotel API",
    description="API de gestion des hôtels avec FastAPI",
    version="1.0.0",
    docs_url="/docs",  # URL pour Swagger
    redoc_url="/redoc",  # URL pour ReDoc
    openapi_url="/openapi.json"  # URL pour récupérer le schéma OpenAPI
)

# Inclusion des routes
app.include_router(hotelRouter, prefix="/hotels", tags=["Hôtels"])
app.include_router(UserRouter, prefix="/users", tags=["Utilisateurs"])
app.include_router(roleRouter, prefix="/role", tags=["roles"])

# Route de test
@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API des hôtels 🚀"}

# Lancer le serveur si ce fichier est exécuté directement
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)

