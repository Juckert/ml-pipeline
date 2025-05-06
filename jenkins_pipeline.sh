#!/bin/bash
set -e
echo "Step 1: Downloading data"
python3 download.py

echo "Step 2: Training model"
python3 train_model.py

echo "Step 3: Model trained and logged to mlflow"
