from fastapi import FastAPI,Request
from pydantic import BaseModel


app = FastAPI()
# # DAY 5
# task_db = {}
# task_counter = 0 

# # view tasks
# @app.get("/tasks")
# def all_tasks():
#     return task_db

# class Tasks(BaseModel):
#     task : str 
#     date : Optional[str] = None


# @app.post("/tasks/{task_id}")
# def create_task(task_id:int, task:Tasks):
#     global task_counter
#     task_counter+= 1
#     task_db[task_counter] = task.model_dump()
#     return {"id":task_counter, **task.model_dump()}

# Again restarting from the basics DAY 4 

@app.get("/")
def home():
    return "welcome to Home Page!"

tasks = [
    {
        "id":1,
        "task1":"How to complete this task"
    },
    {
        "id":2,
        "task2":"Nice Work !!"
    }
]

@app.get("/tasks")
def get_tasks():
    return tasks

#path Parameters/params
@app.get("/task/{task_id}")
def get_tsk(task_id:int):
    for oneTask in tasks:
        if oneTask.get("id") == task_id:
            return oneTask
    
    return  {
        "error":"Task id Not Found"
        }
#query parameters/params
@app.get("/greet")
def greet(request:Request):
    query_params = dict(request.query_params)
    print(query_params)
    return f"hello , NiceWork !"


# pydantic (BaseModel)
class Tasks(BaseModel):
    id : int
    decription : str 
    lst_tasks : str | None = None 
#types of HTTP Methods 

@app.post("/create_task")
def create_one_task(task_data:Tasks):
    # task_data = task_data.model_dump()
    # print(task_data)
    return{"message":"Created succesfully!", 
            "task":task_data.model_dump()
            }







