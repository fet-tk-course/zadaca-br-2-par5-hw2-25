from fastapi import FastAPI
from contextlib import asynccontextmanager

from database import create_db_and_tables
from routes_b import router as booking_router 

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(
    title="Turistička Agencija",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(booking_router)


@app.get("/")
def read_root():
    return {
        "message": "Dobrodošli na  Turističke agencije",
        "docs": "Posjetite /docs za Swagger dokumentaciju"
    }