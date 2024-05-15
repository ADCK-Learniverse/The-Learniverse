from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    email: EmailStr
    password: str = Field(..., max_length=45)
    firstname: str = Field(..., max_length=45)
    lastname: str = Field(..., max_length=45)
    role: str = Field(..., max_length=45)
    phone_number: Optional[str]
    other_accounts: Optional[str]


class Course(BaseModel):
    title: str = Field(min_length=5, max_length=45)
    description: str = Field(min_length=5, max_length=45)
    objectives: str = Field(min_length=5, max_length=45)
    status: str = Field(min_length=6, max_length=7)
    rating: Optional[int]
