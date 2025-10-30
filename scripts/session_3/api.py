from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from enum import Enum

from scripts.session_3.router import predict


app = FastAPI()
app.include_router(predict.housing_router)

class Method(str, Enum):
    add = "add"
    subtract = "subtract"

class CalculateRequest(BaseModel):
    method: Method
    num1: float
    num2: float

class CalculateResponse(BaseModel): 
    result: float

@app.get("/")
def root():
    return {"message": "Hello, World!"}

@app.get("/health")
def health_check(dump_input: str):
    return {"status": "healthy", "input": dump_input}

@app.post("/calculate", response_model=CalculateResponse)
def calculate(request: CalculateRequest):
    if request.method == Method.add:
        result = request.num1 + request.num2
    elif request.method == Method.subtract:
        result = request.num1 - request.num2
    else:
        return {"error": "Invalid method"}
    return CalculateResponse(result=result)


if __name__ == "__main__":
    uvicorn.run("scripts.session_3.api:app", host="0.0.0.0", port=8000, reload=True)