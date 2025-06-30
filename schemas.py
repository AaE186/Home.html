from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    class Config:
        orm_mode = True

class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    pass

class NoteOut(NoteBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True

class ExpenseBase(BaseModel):
    amount: float
    category: str
    comment: Optional[str] = None

class ExpenseCreate(ExpenseBase):
    pass

class ExpenseOut(ExpenseBase):
    id: int
    date: datetime
    class Config:
        orm_mode = True

class TrainingBase(BaseModel):
    type: str
    duration: int
    comment: Optional[str] = None

class TrainingCreate(TrainingBase):
    pass

class TrainingOut(TrainingBase):
    id: int
    date: datetime
    class Config:
        orm_mode = True

class GoalBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = "active"
    deadline: Optional[datetime] = None

class GoalCreate(GoalBase):
    pass

class GoalOut(GoalBase):
    id: int
    class Config:
        orm_mode = True 