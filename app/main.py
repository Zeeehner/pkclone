from fastapi import FastAPI
from app import models
from app.db import engine
from app.api import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)

@app.get("/")
def root():
    return {"msg": "PK-Backend läuft"}

# @app.get("/health")
# def health_check():
#     return {"status": "ok"}
# Uncomment the health check endpoint if needed
# This endpoint can be used to check if the server is running and responsive.
