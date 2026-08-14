# Student Performance Predictor

Predicts a student's final grade (G3, 0-20 scale) using their first two grading
periods, absences, age, family relations, health, and other factors.

## Model
Random Forest, trained on the UCI Student Performance dataset. Feature set
reduced from 30 to 8 based on importance analysis (R² 0.81 → 0.77 tradeoff
for a much simpler API — see `notebook/` for full analysis).

## Run locally
docker build -t student-performance-api .
docker run -p 8000:8000 student-performance-api
# visit http://localhost:8000/docs

## Live demo
[Hugging Face Space link — add once deployed]
