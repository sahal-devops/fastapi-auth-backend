from fastapi import FastAPI
from app.database import engine, Base
from app.models.user import User
from app.routes.auth_routes import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)

print(app.routes)

@app.get("/")
def home():
    return {"message": "FastAPI Level 2 Backend Running"}