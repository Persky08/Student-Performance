from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import pandas as pd

app = FastAPI(title="Student Performance Predictor")

CATEGORICAL_FEATURES = ["reason", "schoolsup"]
NUMERIC_FEATURES = ["G1", "G2", "absences", "age", "famrel", "health"]
ALL_FEATURES = CATEGORICAL_FEATURES + NUMERIC_FEATURES

model = joblib.load("model_lean.pkl")

class StudentFeatures(BaseModel):
    reason: str
    schoolsup: str
    G1: float = Field(..., ge=0, le=20)
    G2: float = Field(..., ge=0, le=20)
    absences: float = Field(..., ge=0, le=100)
    age: float = Field(..., ge=10, le=25)
    famrel: float = Field(..., ge=1, le=5)
    health: float = Field(..., ge=1, le=5)

@app.get("/")
def root():
    return {"message": "Student Performance Predictor API is running"}

@app.post("/predict")
def predict(features: StudentFeatures):
    try:
        input_df = pd.DataFrame([[
            features.reason, features.schoolsup, features.G1, features.G2,
            features.absences, features.age, features.famrel, features.health
        ]], columns=ALL_FEATURES)

        prediction = model.predict(input_df)[0]
        return {"predicted_final_grade": round(float(prediction), 2)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")