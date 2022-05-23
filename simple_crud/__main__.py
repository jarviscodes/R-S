from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

all_tasks = []

class Person(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: int


class Task(BaseModel):
    id: int
    description: str
    person: Person


@app.get("/")
def home():
    return {"status": "ok"}

@app.post("/")
def create_task(task: Task):
    all_tasks.append(task)
    return all_tasks
