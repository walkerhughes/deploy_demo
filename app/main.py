from fastapi import FastAPI
from pydantic import BaseModel
from dataclasses import dataclass
from app.model.model import predict, model_version

app = FastAPI() 

class IntIn(BaseModel): 
    input_int: int 

class IntOut(BaseModel): 
    output_int: int 

@app.get("/")
def home(): 
    return {"status": "OK", "version": model_version}

@app.post("/predict", response_model=IntOut)
def predict_endpoint(payload: IntIn):
    result = predict(payload.input_int)  
    return {"output_int": result}

