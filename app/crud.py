from sqlalchemy.orm import Session
from .models import Task
from .schemas import TaskCreate

def create_task(db: Session, task_data: TaskCreate):
    task = Task(**task_data.dict())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_tasks(db: Session, skip: int = 0, limit: int = 10, priority: str = None, status: str = None):
    query = db.query(Task)
    if priority:
        query = query.filter(Task.priority == priority)
    if status:
        query = query.filter(Task.status == status)
    return query.offset(skip).limit(limit).all()

def update_task(db: Session, task_id: int, task_data: TaskCreate):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        for key, value in task_data.dict().items():
            setattr(task, key, value)
        db.commit()
        db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return task
