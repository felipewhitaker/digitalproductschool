import sys
from datetime import datetime
from enum import Enum

from pathlib import Path

import pandas as pd
from src.models import models  # import all models for `pickle.load`

sys.modules["models"] = models  # from https://stackoverflow.com/a/2121918/14403987
import pickle

import uvicorn
from fastapi import Depends, FastAPI, Request


def get_prediction(model, year: int, month: int):
    date_str = f"{year}-{month}-01"
    n_steps = (
        pd.to_datetime(date_str).to_period("M") - model.end_date.to_period("M")
    ).n
    return model.forecast(steps=n_steps)[datetime(year, month, 1)]


async def store_ip(request: Request):
    with open("./ip.txt", "a+") as f:
        f.write(f"{datetime.now():%F %H:%M:%S}\t{request.client.host}\n")
    return


MODELS_PATH = Path("./src/models/")

MODELS = {}
for model in MODELS_PATH.glob("*.pkl"):
    if model.stem == "SARIMAX":
        # SARIMAX did not show good enough performance, and
        # `statsmodels` is quite heavy
        continue
    with open(model, "rb") as f:
        MODELS[model.stem.lower()] = pickle.load(f)
Models = Enum("Models", {key: key for key in MODELS.keys()})

app = FastAPI()


@app.get("/", dependencies=[Depends(store_ip)])
async def index():
    return {
        "message": (
            "Hi there! This was developed by Felipe Whitaker "
            "for Digital Product School 2023 challenge. Make a "
            "POST request to `/predict` with `year` and `month`  keys"
            "to receive a `prediction` on the total accidents in Munich"
        )
    }


@app.post("/predict/", dependencies=[Depends(store_ip)])
async def predict(year: int, month: int):
    global MODELS
    # although `Seasonal` was not the best performing model,
    # it is much lighter than SARIMAX and captures the pattern well
    model = MODELS["seasonal"]
    return {"prediction": get_prediction(model, year, month)}


@app.post("/predict/{model_name}", dependencies=[Depends(store_ip)])
async def predict(model_name: Models, year: int, month: int):
    global MODELS
    return {"prediction": get_prediction(MODELS[model_name.value], year, month)}


if __name__ == "__main__":
    uvicorn.run("main:app")
