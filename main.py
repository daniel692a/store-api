from fastapi import FastAPI
from routes.user import user

app = FastAPI(title="Store API", description="Store API", version="0.1")

app.include_router(user)