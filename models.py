# Python 
from uuid import UUID
from typing import Optional
from datetime import date, datetime


# Pydantic
from pydantic import BaseModel, Field, EmailStr


# FastAPI


class UserBase(BaseModel):
    user_ui: UUID = Field(...)
    email: EmailStr = Field(...)


class UserLogin(UserBase):
    password : str = Field(..., min_length=8)


class User(UserBase):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    birth_date: Optional[date] = Field(default=None)

class UserRegister(User, UserLogin):
    pass


class Tweet(BaseModel):
    tweet_id : UUID = Field(...)
    content: str = Field(..., min_length=1, max_length=256)
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)



