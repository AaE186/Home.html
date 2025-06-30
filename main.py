from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from . import models, schemas, database, auth
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import IntegrityError
from datetime import datetime

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(auth.get_db)):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Пользователь с таким email уже существует")
    return db_user

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(auth.get_db)):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Неверный email или пароль")
    access_token = auth.create_access_token(data={"sub": user.id})
    return {"access_token": access_token, "token_type": "bearer"}

# CRUD для заметок
@app.post("/notes", response_model=schemas.NoteOut)
def create_note(note: schemas.NoteCreate, db: Session = Depends(auth.get_db), current_user: models.User = Depends(auth.get_current_user)):
    db_note = models.Note(**note.dict(), owner_id=current_user.id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

@app.get("/notes", response_model=list[schemas.NoteOut])
def get_notes(db: Session = Depends(auth.get_db), current_user: models.User = Depends(auth.get_current_user)):
    return db.query(models.Note).filter(models.Note.owner_id == current_user.id).all()

@app.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(auth.get_db), current_user: models.User = Depends(auth.get_current_user)):
    note = db.query(models.Note).filter(models.Note.id == note_id, models.Note.owner_id == current_user.id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Заметка не найдена")
    db.delete(note)
    db.commit()
    return {"ok": True}

# CRUD для расходов
@app.post("/expenses", response_model=schemas.ExpenseOut)
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(auth.get_db), current_user: models.User = Depends(auth.get_current_user)):
    db_expense = models.Expense(**expense.dict(), owner_id=current_user.id)
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

@app.get("/expenses", response_model=list[schemas.ExpenseOut])
def get_expenses(db: Session = Depends(auth.get_db), current_user: models.User = Depends(auth.get_current_user)):
    return db.query(models.Expense).filter(models.Expense.owner_id == current_user.id).all()

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(auth.get_db), current_user: models.User = Depends(auth.get_current_user)):
    expense = db.query(models.Expense).filter(models.Expense.id == expense_id, models.Expense.owner_id == current_user.id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Расход не найден")
    db.delete(expense)
    db.commit()
    return {"ok": True}

# CRUD для тренировок
@app.post("/trainings", response_model=schemas.TrainingOut)
def create_training(training: schemas.TrainingCreate, db: Session = Depends(auth.get_db), current_user: models.User = Depends(auth.get_current_user)):
    db_training = models.Training(**training.dict(), owner_id=current_user.id)
    db.add(db_training)
    db.commit()
    db.refresh(db_training)
    return db_training

@app.get("/trainings", response_model=list[schemas.TrainingOut])
def get_trainings(db: Session = Depends(auth.get_db), current_user: models.User = Depends(auth.get_current_user)):
    return db.query(models.Training).filter(models.Training.owner_id == current_user.id).all()

@app.delete("/trainings/{training_id}")
def delete_training(training_id: int, db: Session = Depends(auth.get_db), current_user: models.User = Depends(auth.get_current_user)):
    training = db.query(models.Training).filter(models.Training.id == training_id, models.Training.owner_id == current_user.id).first()
    if not training:
        raise HTTPException(status_code=404, detail="Тренировка не найдена")
    db.delete(training)
    db.commit()
    return {"ok": True}

# CRUD для целей
@app.post("/goals", response_model=schemas.GoalOut)
def create_goal(goal: schemas.GoalCreate, db: Session = Depends(auth.get_db), current_user: models.User = Depends(auth.get_current_user)):
    db_goal = models.Goal(**goal.dict(), owner_id=current_user.id)
    db.add(db_goal)
    db.commit()
    db.refresh(db_goal)
    return db_goal

@app.get("/goals", response_model=list[schemas.GoalOut])
def get_goals(db: Session = Depends(auth.get_db), current_user: models.User = Depends(auth.get_current_user)):
    return db.query(models.Goal).filter(models.Goal.owner_id == current_user.id).all()

@app.delete("/goals/{goal_id}")
def delete_goal(goal_id: int, db: Session = Depends(auth.get_db), current_user: models.User = Depends(auth.get_current_user)):
    goal = db.query(models.Goal).filter(models.Goal.id == goal_id, models.Goal.owner_id == current_user.id).first()
    if not goal:
        raise HTTPException(status_code=404, detail="Цель не найдена")
    db.delete(goal)
    db.commit()
    return {"ok": True} 