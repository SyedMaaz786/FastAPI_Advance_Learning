from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello There! This is Syed Maaz."}

@app.get("/greet/{name}")  # Here we have created a route which takes input from the url itself and prints it in the result page
async def greet_name(name: str, age: int) -> dict:  #This is the example of path and Query parameter
    return {"message":f"Welcome {name}", "age": age}
