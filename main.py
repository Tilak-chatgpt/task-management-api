from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# DAY 5
task_db = {}
task_counter = 0 

# view tasks
@app.get("/tasks")
def all_tasks():
    return task_db

class Tasks(BaseModel):
    task : str 
    date : Optional[str] = None


@app.post("/tasks/{task_id}")
def create_task(task_id:int, task:Tasks):
    global task_counter
    task_counter+= 1
    task_db[task_counter] = task.model_dump()
    return {"id":task_counter, **task.model_dump()}





