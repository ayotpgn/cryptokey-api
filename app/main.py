
from fastapi import FastAPI
from app.api import auth_routes, secrets_routes
from app.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_routes.router, prefix="/auth")
app.include_router(secrets_routes.router, prefix="/api")
