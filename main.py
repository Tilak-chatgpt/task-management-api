from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# students = {
#     1:{
#         "name": "John Doe",
#         "age": 20,
#         "course": "Computer Science"
#     }
# }


@app.get("/") 
def taskapi(): 
    return {"message": "Hello World"}

# @app.get("/get-taskapi/{students_id}")
# def get_students(students_id: int = Path(..., description="The ID should view in the data", gt= 0, lt= 3)):
#     return students[students_id]
task = {
    1:{
        "TASK 1":"Watch Anime",
        "TASK 2": "Create a website",
        "Task 3": "Learn Python",
        "name" : "John Doe",
    }, 
    2:{
        "TASK 1":"Watch Movie",
        "TASK 2": "Create a Mobile App",
        "Task 3": "Learn Java",
        "name" : "Meena Doe",
    },
    3:{
        "TASK 1":"Watch TV Show",
        "TASK 2": "Create a Game",
        "Task 3": "Learn C++",
        "name" : "Rohit Doe",
    }
}

@app.get("/tasks/{task_id}")
def tasks(task_id: int = Path(..., description="THE TASK IS VISIABLE IN THE SERVER")):
    return(task[task_id] )

@app.get("/task-by-name/{task_id}") 
def task_name(name:Optional[str] = None): 
    for tid in task:
        if task[tid]["name"] == name:
            return task[tid]
    return {"message": "Task not found"}


@app.get("/all-tasks")
def get_all_tasks():
    return task


class Task(BaseModel):
    id:int 
    title: str 
    completed : bool = False

task = []

@app.post("/tasks")
def create_task(task: Task):
    task.append(task.model_dump())

    return task 


