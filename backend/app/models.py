from typing import Optional, Annotated

from fastapi import Depends
from pydantic import BaseModel, Field, EmailStr

from backend.app.api.services.login_services import get_current_user

user_dependency = Annotated[dict, Depends(get_current_user)]


class User(BaseModel):
    email: EmailStr
    password: str = Field(..., max_length=45)
    firstname: str = Field(..., max_length=45)
    lastname: str = Field(..., max_length=45)
    phone_number: Optional[str]
    # other_accounts: Optional[str]


class Section(BaseModel):
    title: str = Field(..., max_length=45)
    content: str = Field(..., max_length=1000)
    description: str = None
    information: str = None
    course_id: int = Field(...)


class Course(BaseModel):
    title: str = Field(min_length=5, max_length=45)
    description: str = Field(min_length=5, max_length=45)
    objectives: str = Field(min_length=5, max_length=45)
    status: str = Field(min_length=6, max_length=7)
    tags: list


class UpdateProfile(BaseModel):
    First_name: str = None
    Last_name: str = None
    Phone_number: str = None
    Password: str = None


