import os
import pandas as pd

# Path Configuration
RAW_DATA_PATH = "input-data/raw/creditcard.csv"

def verify_ingestion():
    print("Starting Phase 1: Ingestion Verification...")

    if os.path.exists(RAW_DATA_PATH):
        file_size = os.path.getsize(RAW_DATA_PATH) / (1024 * 1024)
        print(f"Success: Raw data found at {RAW_DATA_PATH}")
        print(f"File Size: {file_size:.2f} MB")
    else:
        print(f"Error: Raw data NOT found at {RAW_DATA_PATH}")

if __name__ == "__main__":
    verify_ingestion()
