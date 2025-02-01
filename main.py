from fastapi import FastAPI
from pydantic import BaseModel, Field
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/version")
async def say_version():
    return {"version": "Hello ver : 12.0.0.1"}

class DataInput(BaseModel):
    name: str

class PredicOutput(BaseModel):
    prob: float
    prediction: int
@app.post("/pydantic", response_model=PredicOutput)
def pydantic_post(data_request:DataInput):
    return{'prob': 0.1, 'prediction': 5}