from fastapi import FastAPI
from typing import Dict

app = FastAPI()


@app.get("/")
def read_root() -> Dict[str, str]:
    return {"msg": "User-service is running!"}


@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": "Test User", "email": "user@example.com"}
