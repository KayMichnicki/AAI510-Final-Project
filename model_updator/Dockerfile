FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && \
    pip install yfinance boto3 pandas
CMD ["python", "model_updator.py"]
