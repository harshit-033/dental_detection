# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import torch
import os

app = FastAPI()
model = None
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


class PredictRequest(BaseModel):
    inputs: list  # adapt this to your model input format


@app.on_event("startup")
async def load_model():
    """Load the PyTorch model when the app starts"""
    global model
    model_path = os.environ.get("MODEL_PATH", "model.pt")  # Use env variable if provided
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")

    # If your model is saved as full model
    model = torch.load(model_path, map_location=device)

    # If your model is saved as state_dict:
    # model = MyModelClass(...)  # instantiate your model
    # model.load_state_dict(torch.load(model_path, map_location=device))

    model.eval()
    print(f"Model loaded from {model_path} on {device}")


@app.post("/predict")
async def predict(req: PredictRequest):
    """Run prediction on incoming data"""
    global model
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")

    try:
        # Convert input list to tensor (adapt this to your model's input shape)
        x = torch.tensor(req.inputs).float().to(device)
        with torch.no_grad():
            out = model(x)
        return {"result": out.cpu().numpy().tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
