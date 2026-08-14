FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY model_wrapper.py .
COPY model_lean.pkl .
COPY dashboard.py .
COPY start.sh .

RUN chmod +x start.sh

EXPOSE 7860

CMD ["./start.sh"]