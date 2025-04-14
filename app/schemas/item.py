from pydantic import BaseModel
from typing import Optional
from bson import ObjectId

class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class ItemInDB(ItemBase):
    id: str
