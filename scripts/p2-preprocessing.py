import pandas as pd
import os

# Configuration for absolute clarity
INPUT_PATH = "input-data/raw/creditcard.csv"
OUTPUT_DIR = "input-data/processed"
OUTPUT_FILE = f"{OUTPUT_DIR}/cleaned_fraud_data.csv"

def run_preprocessing():
    print("Starting Phase 2: Data Cleaning and Export...")
    
    # Validation step to prevent pathing errors
    if not os.path.exists(INPUT_PATH):
        print(f"Error: Raw dataset not found at {INPUT_PATH}")
        return

    # Loading 143.84 MB dataset
    try:
        df = pd.read_csv(INPUT_PATH)
        print(f"Initial Load Complete. Shape: {df.shape}")
    except Exception as e:
        print(f"Error during CSV ingestion: {e}")
        return
    
    # Step 1: Quality Audit
    null_count = df.isnull().sum().sum()
    dup_count = df.duplicated().sum()
    print(f"Audit Results: {null_count} Nulls, {dup_count} Duplicates found.")
    
    # Step 2: Cleaning Execution
    if dup_count > 0:
        df = df.drop_duplicates()
        print(f"Duplicates removed. New Shape: {df.shape}")
    
    # Step 3: Secure Export
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        df.to_csv(OUTPUT_FILE, index=False)
        print(f"Cleaned data successfully saved to: {OUTPUT_FILE}")
    except Exception as e:
        print(f"Error during data export: {e}")

    print("Phase 2 Process Finalized.")

if __name__ == "__main__":
    run_preprocessing()
