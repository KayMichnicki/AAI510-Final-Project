import yfinance as yf
import pandas as pd
import boto3
from datetime import datetime

symbol = "AAPL"
s3_bucket = "your-bucket-name"
file_name = f"daily_{symbol}_{datetime.now().date()}.csv"
s3_key = f"daily/{file_name}"

def fetch_and_upload():
    df = yf.download(symbol, period="1d", interval="1h")
    df.to_csv(file_name)
    s3 = boto3.client("s3")
    s3.upload_file(file_name, s3_bucket, s3_key)
    print("Uploaded to cloud storage.")

if __name__ == "__main__":
    fetch_and_upload()
