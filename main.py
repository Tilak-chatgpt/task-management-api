from fastapi import FastAPI

app = FastAPI()

@app.get("/") 
def taskapi(): 
    return {"message": "Hello World"}
