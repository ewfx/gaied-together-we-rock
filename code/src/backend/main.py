from fastapi import FastAPI
from database import engine, Base
from api import router

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Register router
app.include_router(router)
