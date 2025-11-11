from fastapi import FastAPI
from typing import Dict

app = FastAPI()


@app.get("/")
def read_root() -> Dict[str, str]:
    return {"msg": "Project-analytics-service is running!"}
