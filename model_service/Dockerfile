FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && \
    pip install flask xgboost joblib pandas boto3
CMD ["python", "model_service.py"]
