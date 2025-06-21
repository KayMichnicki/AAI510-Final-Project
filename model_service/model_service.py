from flask import Flask, request, jsonify
import joblib
import xgboost as xgb
import pandas as pd
import boto3
import os

# Initialize Flask application
app = Flask(__name__)

# S3 bucket and local model directory configuration
S3_BUCKET = "your-bucket-name"
MODEL_S3_PREFIX = "models/"
LOCAL_MODEL_DIR = "saved_models"

# Ensure the local model directory exists
os.makedirs(LOCAL_MODEL_DIR, exist_ok=True)

# Initialize S3 client
s3 = boto3.client("s3")

# Dictionary to hold all loaded models with their names as keys
models = {}

# ---------------------- FUNCTION DEFINITIONS ----------------------

def download_all_models_from_s3():
    """
    Download all .pkl model files from an S3 bucket to the local model directory.
    """
    response = s3.list_objects_v2(Bucket=S3_BUCKET, Prefix=MODEL_S3_PREFIX)

    # Exit early if no files found
    if "Contents" not in response:
        print("No models found in S3 bucket.")
        return

    # Download each .pkl file in the specified prefix
    for obj in response["Contents"]:
        key = obj["Key"]
        if key.endswith(".pkl"):
            local_path = os.path.join(LOCAL_MODEL_DIR, os.path.basename(key))
            s3.download_file(S3_BUCKET, key, local_path)
            print(f"Downloaded {key} to {local_path}")

def load_models_from_directory(directory):
    """
    Load all .pkl models from the given directory into the global models dictionary.
    """
    for file in os.listdir(directory):
        if file.endswith(".pkl"):
            model_path = os.path.join(directory, file)
            model_name = os.path.splitext(file)[0]  # Use file name without extension as key
            models[model_name] = joblib.load(model_path)
            print(f"Loaded model: {model_name}")

def prepare_input(symbol):
    """
    Prepare dummy input for prediction. 
    Replace with actual feature extraction logic based on 'symbol'.
    """
    return xgb.DMatrix([[0], [1]])  # Dummy 2-row input

# ---------------------- FLASK ROUTES ----------------------

@app.route('/predict', methods=['POST'])
def predict():
    """
    Handle POST request for prediction using a specified model.
    Expects JSON with 'symbol' and 'model_name'.
    """
    # Extract request data
    symbol = request.json.get("symbol")
    model_name = request.json.get("model_name")

    # Validate that requested model exists
    if model_name not in models:
        return jsonify({"error": f"Model '{model_name}' not found."}), 404

    # Prepare input data (currently dummy)
    data = prepare_input(symbol)

    # Make prediction using the selected model
    preds = models[model_name].predict(data)

    # Return predictions as JSON
    return jsonify({
        "model": model_name,
        "symbol": symbol,
        "predictions": preds.tolist()
    })

# ---------------------- APP ENTRY POINT ----------------------

if __name__ == '__main__':
    # Step 1: Download models from S3 bucket
    download_all_models_from_s3()

    # Step 2: Load all models into memory
    load_models_from_directory(LOCAL_MODEL_DIR)

    # Step 3: Start the Flask app
    app.run(host="0.0.0.0", port=5000)
