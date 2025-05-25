# schemas/task.py
from pydantic import BaseModel

class TaskBase(BaseModel):
    id: int 
    name: str

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    
    class Config:
        from_attributes = True