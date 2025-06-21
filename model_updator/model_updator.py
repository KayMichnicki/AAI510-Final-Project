import yfinance as yf
import pandas as pd
import boto3
from datetime import datetime
import os
import schedule
import time
import importlib.util

# Configuration
symbol = "AAPL"  # You can later extend this to a list of symbols
s3_bucket = "your-bucket-name"
file_name = f"daily_{symbol}_{datetime.now().date()}.csv"
s3_key = f"daily/{file_name}"

def fetch_and_upload():
    """
    Fetches the latest 1-day hourly stock data using yfinance, saves it as a CSV,
    and uploads it to the configured S3 bucket.
    """
    print(f"[{datetime.now()}] Fetching hourly data for {symbol}...")

    # Fetch 1-day hourly interval data
    df = yf.download(symbol, period="1d", interval="1h")

    # Save locally to CSV
    df.to_csv(file_name)
    print(f"Saved to {file_name}")

    # Upload to AWS S3
    s3 = boto3.client("s3")
    s3.upload_file(file_name, s3_bucket, s3_key)
    print(f"Uploaded {file_name} to s3://{s3_bucket}/{s3_key}")

def trigger_model_retraining():
    """
    Dynamically loads and triggers the training function from model_training directory.
    """
    print(f"[{datetime.now()}] Triggering model retraining...")

    # Path to training script
    training_script_path = os.path.join("model_training", "train_model.py")  # Adjust filename as needed

    # Load module dynamically
    spec = importlib.util.spec_from_file_location("train_model", training_script_path)
    train_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(train_module)

    # Call train_model function (assumes this function exists inside train_model.py)
    if hasattr(train_module, "train_model"):
        train_module.train_model()
        print("Model retraining completed.")
    else:
        print("train_model() function not found in model_training/train_model.py")

def daily_job():
    """
    Main scheduled job to be run nightly:
    - Downloads new stock data
    - Uploads it to S3
    - Retrains the ML model
    """
    fetch_and_upload()
    trigger_model_retraining()

# Schedule the job to run every night at 2 AM
schedule.every().day.at("02:00").do(daily_job)

print("Scheduler started. Waiting for the next execution...")

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)
