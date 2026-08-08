from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="Heart Disease Risk Prediction API")

model = joblib.load('models/model.pkl')
encoders = joblib.load('models/encoders.pkl')

class PatientData(BaseModel):
    Age: int
    Sex: str
    ChestPainType: str
    RestingBP: int
    Cholesterol: int
    FastingBS: int
    RestingECG: str
    MaxHR: int
    ExerciseAngina: str
    Oldpeak: float
    ST_Slope: str

@app.post("/predict")
def predict(data: PatientData):
    df = pd.DataFrame([data.dict()])
    for col, le in encoders.items():
        df[col] = le.transform(df[col])

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return {
        "prediction": int(prediction),
        "risk_probability": round(float(probability), 3)
    }