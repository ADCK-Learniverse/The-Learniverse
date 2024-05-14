import imghdr

from fastapi import Query
from pydantic import BaseModel, Field, EmailStr
from typing import List
from datetime import datetime


class User(BaseModel):
    email: EmailStr
    password: str = Field(..., max_length=45)
    firstname: str = Field(..., max_length=45)
    lastname: str = Field(..., max_length=45)
    role: str = Field(..., max_length=45)
    phone_number: str = None
    other_accounts: str = None
    picture: imghdr = None



