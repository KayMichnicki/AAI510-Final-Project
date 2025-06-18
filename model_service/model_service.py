from flask import Flask, request, jsonify
import joblib
import xgboost as xgb
import pandas as pd
import boto3
import os

app = Flask(__name__)
s3_bucket = "your-bucket-name"
model_key = "models/model.pkl"

s3 = boto3.client("s3")
s3.download_file(s3_bucket, model_key, "model.pkl")
model = joblib.load("model.pkl")

def prepare_input(symbol):
    return xgb.DMatrix([[0], [1]])

@app.route('/predict', methods=['POST'])
def predict():
    symbol = request.json.get("symbol")
    data = prepare_input(symbol)
    preds = model.predict(data)
    return jsonify({"symbol": symbol, "predictions": preds.tolist()})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)