import imghdr
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
    references: str = None

