import requests

payload = {
    "reason": "course",
    "schoolsup": "yes",
    "G1": 15,
    "G2": 16,
    "absences": 10,
    "age": 18,
    "famrel": 4,
    "health": 3
}

response = requests.post("http://localhost:8000/predict", json=payload)
print(response.json())
