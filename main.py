from fastapi import FastAPI,Path

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
        "Task 3": "Learn Python"
    }, 
    2:{
        "TASK 1":"Watch Movie",
        "TASK 2": "Create a Mobile App",
        "Task 3": "Learn Java"
    },
    3:{
        "TASK 1":"Watch TV Show",
        "TASK 2": "Create a Game",
        "Task 3": "Learn C++"
    }
}

@app.get("/tasks/{task_id}")
def tasks(task_id: int = Path(..., description="THE TASK IS VISIABLE IN THE SERVER")):
    return(task[task_id] )

