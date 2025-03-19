from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .database import get_db
from .crud import create_task, get_tasks, update_task, delete_task
from .schemas import TaskCreate, TaskResponse, UserCreate, UserResponse
from .auth import authenticate_user, create_access_token, get_current_user, get_password_hash
from .models import User

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    user_exists = db.query(User).filter(User.username == user_data.username).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="Username already taken")
    
    hashed_password = get_password_hash(user_data.password)
    user = User(username=user_data.username, password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.post("/login")
def login(form_data: UserCreate, db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/tasks/", response_model=TaskResponse)
def create_task_api(task: TaskCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return create_task(db, task)

@router.get("/tasks/")
def get_tasks_api(skip: int = 0, limit: int = 10, priority: str = None, status: str = None, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return get_tasks(db, skip, limit, priority, status)

@router.put("/tasks/{task_id}")
def update_task_api(task_id: int, task: TaskCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return update_task(db, task_id, task)

@router.delete("/tasks/{task_id}")
def delete_task_api(task_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return delete_task(db, task_id)
