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
    # We can return dicts
    return {"status": "ok"}

@app.post("/")
def create_task(task: Task):
    all_tasks.append(task)
    # A single object
    return task

@app.get("/all")
def get_all_tasks():
    # Or even an iterable of objects
    return all_tasks


@app.get("/{user_id}")
def get_tasks_for_user(user_id: int):
    # Example filtering
    tasks_for_user = [
        task for task in all_tasks
        if task.person.id == user_id
    ]
    return tasks_for_user