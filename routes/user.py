from fastapi import APIRouter, Response, status
from config.db import conn
from models.user import users
from schemas.user import User
from starlette.status import HTTP_204_NO_CONTENT, HTTP_200_OK
import hashlib

user = APIRouter()

@user.get("/users", response_model=list[User], tags=["users"])
def get_users():
    return conn.execute(users.select()).fetchall()

@user.post("/users/create/", response_model=int, tags=["users"])
def create_user(user: User):
    new_user = {"name": user.name, "email": user.email}
    new_user["password"] = user.password
    result = conn.execute(users.insert().values(new_user))
    return result.lastrowid

@user.get("/users/{id}", response_model=User, tags=["users"])
def get_users(id: int):
    return conn.execute(users.select().where(users.c.id == id)).first()


@user.delete("/users/delete/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
def delete_user(id: int):
    result = conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@user.put("/users/update/{id}", response_model=int, tags=["users"])
def update_user(id: int, user: User):
    conn.execute(users.update().values(
        name=user.name,
        email=user.email,
        password=user.password).where(users.c.id == id))
    return Response(status_code=HTTP_200_OK)