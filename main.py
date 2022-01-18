from fastapi import FastAPI
from routes.user import user

app = FastAPI(title="Store API", description="Store API", version="0.0.1", openapi_tags=[{"name": "users", "description": "User operations"}])

app.include_router(user)