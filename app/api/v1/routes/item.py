from fastapi import APIRouter, HTTPException, Depends
from typing import List

from app.schemas.item import ItemCreate, ItemInDB
from app.crud import item as crud_item
from app.db.mongodb import get_database

router = APIRouter()

@router.post("/", response_model=ItemInDB)
async def create(item: ItemCreate, db=Depends(get_database)):
    return await crud_item.create_item(db, item)

@router.get("/{item_id}", response_model=ItemInDB)
async def read(item_id: str, db=Depends(get_database)):
    item = await crud_item.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.get("/", response_model=List[ItemInDB])
async def read_all_items(db=Depends(get_database)):
    return await crud_item.get_all_items(db)
