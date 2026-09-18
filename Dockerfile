FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY infinite_slope_stability_calculator.py .

EXPOSE 7860

CMD ["python", "app.py"]
