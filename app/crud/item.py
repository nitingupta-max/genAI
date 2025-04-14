from app.schemas.item import ItemCreate, ItemInDB
from bson.objectid import ObjectId
from typing import List

collection_name = "items"

async def create_item(db, item: ItemCreate) -> ItemInDB:
    result = await db[collection_name].insert_one(item.dict())
    return ItemInDB(**item.dict(), id=str(result.inserted_id))

async def get_item(db, item_id: str) -> ItemInDB | None:
    result = await db[collection_name].find_one({"_id": ObjectId(item_id)})
    if result:
        result["id"] = str(result["_id"])
        return ItemInDB(**result)
    return None

async def get_all_items(db) -> List[ItemInDB]:
    items = []
    cursor = db[collection_name].find({})
    async for document in cursor:
        document["id"] = str(document["_id"])
        items.append(ItemInDB(**document))
    return items
