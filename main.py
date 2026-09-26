from fastapi import FastAPI
from sqlalchemy import text

from database import engine
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


app = FastAPI()


@app.get("/users")
def get_users():

    with engine.connect() as connection:

        result = connection.execute(
            text("SELECT * FROM users")
        )

        users = []

        for row in result:
            users.append({
                "id": row.id,
                "name": row.name,
                "age": row.age
            })

        return users


@app.get("/users/{name}")
def get_age(name: str):

    with engine.connect() as connection:

        result = connection.execute(
            text("SELECT age FROM users WHERE name = :name"),
            {"name": name}
        )

        row = result.fetchone()

        if row is None:
            return {"message": "User not found"}

        return {"age": row.age}

@app.post("/users")
def add_user(user: User):

    with engine.begin() as connection:

        result = connection.execute(
            text("""
                INSERT INTO users (name, age)
                VALUES (:name, :age)
                RETURNING id, name, age
            """),
            {
                "name": user.name,
                "age": user.age
            }
        )

        row = result.fetchone()

        return {
            "id": row.id,
            "name": row.name,
            "age": row.age
        }