from fastapi import FastAPI
from app.api.v1.routes import item
from app.db.mongodb import connect, close

app = FastAPI()

@app.on_event("startup")
async def startup():
    await connect()

@app.on_event("shutdown")
async def shutdown():
    await close()

app.include_router(item.router, prefix="/api/v1/items", tags=["items"])
