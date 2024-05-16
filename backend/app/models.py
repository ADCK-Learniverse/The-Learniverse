from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    email: EmailStr
    password: str = Field(..., max_length=45)
    firstname: str = Field(..., max_length=45)
    lastname: str = Field(..., max_length=45)
    role: str = Field(..., max_length=45)
    phone_number: str = None
    other_accounts: str = None
    # picture: imghdr = None

class Section(BaseModel):
    title: str = Field(..., max_length=45)
    content: str = Field(..., max_length=1000)
    description:str = None
    information: str = None
    course_id: int = Field(...)

class Course(BaseModel):
    title: str = Field(min_length=5, max_length=45)
    description: str = Field(min_length=5, max_length=45)
    objectives: str = Field(min_length=5, max_length=45)
    status: str = Field(min_length=6, max_length=7)
    rating: Optional[int]
