import joblib
import pandas as pd

class StudentPerformanceModel:
    """
    Predicts final grade (G3, 0-20 scale) from a student's first two
    grading periods (G1, G2), absences, age, family relations, health,
    reason for choosing the school, and whether they receive school support.
    Validated R² ~ 0.77 (Random Forest, reduced feature set).
    """
    CATEGORICAL_FEATURES = ["reason", "schoolsup"]
    NUMERIC_FEATURES = ["G1", "G2", "absences", "age", "famrel", "health"]
    ALL_FEATURES = CATEGORICAL_FEATURES + NUMERIC_FEATURES

    def __init__(self, model_path="model_lean.pkl"):
        self.model = joblib.load(model_path)

    def predict(self, input_dict: dict) -> float:
        df = pd.DataFrame([input_dict], columns=self.ALL_FEATURES)
        prediction = self.model.predict(df)[0]
        return round(float(prediction), 2)
    