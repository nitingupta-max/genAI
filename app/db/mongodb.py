from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

class MongoDB:
    client: AsyncIOMotorClient = None

db = MongoDB()

async def connect():
    db.client = AsyncIOMotorClient(settings.MONGO_URI)
    print("MongoDB connected.")

async def close():
    db.client.close()
    print("MongoDB connection closed.")

def get_database():
    return db.client[settings.MONGO_DB_NAME]
