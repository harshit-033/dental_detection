# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import torch
import os

app = FastAPI()
model = None
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class PredictRequest(BaseModel):
    inputs: list  # adapt to your input format

@app.on_event("startup")
async def load_model():
    global model
    model_path = os.environ.get("MODEL_PATH", "model.pt")
    # If the .pt is a full saved model
    model = torch.load(model_path, map_location=device)
    # If it's a state_dict, you'll need to instantiate the model class and load_state_dict
    # model = MyModelClass(...)
    # model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()

@app.post("/predict")
async def predict(req: PredictRequest):
    global model
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")
    with torch.no_grad():
        # example: convert list to tensor — adapt to your model
        x = torch.tensor(req.inputs).float().to(device)
        out = model(x)
        return {"result": out.cpu().numpy().tolist()}
