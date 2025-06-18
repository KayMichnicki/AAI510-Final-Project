FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && \
    pip install xgboost pandas joblib boto3
CMD ["python", "model_training.py"]
