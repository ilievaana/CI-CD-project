from typing import Optional

from pydantic import BaseModel


class Article(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    category_id: Optional[str] = None