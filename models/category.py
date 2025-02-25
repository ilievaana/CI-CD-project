from typing import Optional

from pydantic import BaseModel


class Category(BaseModel):
    name: str
    description: Optional[str] = None