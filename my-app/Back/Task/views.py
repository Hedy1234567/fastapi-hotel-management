from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from .schemas import TaskResponse , TaskCreate  # Utilisation de task avec une majuscule
from .models import Task   # Utilisation de task avec une majuscule
from core.database import get_db

# Routeur
taskRouter = APIRouter()

@taskRouter.post("/tasks/")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(**task.dict())
    db.add(db_task)
    db.flush()  # pousse à la DB sans commit
    db.commit()

    return db_task


# 🔹 2. Récupérer tous les tasks
@taskRouter.get("/tasks/", response_model=list[TaskResponse])  # Utilisation de taskResponse avec une majuscule
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()  # Utilisation de task avec une majuscule

# 🔹 3. Récupérer un task par ID
@taskRouter.get("/tasks/{task_id}", response_model=TaskResponse)  # Utilisation de taskResponse avec une majuscule
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(task).filter(task.id == task_id).first()  # Utilisation de task avec une majuscule
    if task is None:
        raise HTTPException(status_code=404, detail="task non trouvé")
    return task

# 🔹 4. Mettre à jour un task
@taskRouter.put("/tasks/{task_id}", response_model=TaskResponse)  # Utilisation de taskResponse avec une majuscule
def update_task(task_id: int, task_data: TaskCreate, db: Session = Depends(get_db)):
    task = db.query(task).filter(task.id == task_id).first()  # Utilisation de task avec une majuscule
    if task is None:
        raise HTTPException(status_code=404, detail="task non trouvé")
    
    for key, value in task_data.dict().items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)
    return task

# 🔹 5. Supprimer un task
@taskRouter.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(task).filter(task.id == task_id).first()  # Utilisation de task avec une majuscule
    if task is None:
        raise HTTPException(status_code=404, detail="task non trouvé")
    
    db.delete(task)
    db.commit()
    return {"message": "task supprimé avec succès"}
