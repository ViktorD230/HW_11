from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class ContactBase(BaseModel):
    name: str
    surname: str
    email: str
    phone: str
    birthday: date
    additional_info: Optional[str] = None

class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    id: int

    class Config:
        orm_mode = True
