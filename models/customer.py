import uuid

from pydantic import BaseModel, Field, EmailStr, SecretStr


class Customer(BaseModel):
    name: str
    email: str
    password: SecretStr=None

    class Config:
        populate_by_name = True