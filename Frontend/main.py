from fastapi import FastAPI

app = FastAPI() 

#End Point
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}