import pandas as pd

# Phase 3: Exploratory Data Analysis (EDA)
# Data: creditcard.csv (150.8 MB)

def run_eda():
    try:
        # Loading the raw fraud data
        df = pd.read_csv('input-data/raw/creditcard.csv')
        
        print("--- Fraud Data Overview ---")
        print(df.info()) # Check memory usage and data types [cite: 2026-02-22]
        
        print("\n--- Missing Transactions ---")
        print(df.isnull().sum())
        
    except FileNotFoundError:
        print("Error: creditcard.csv not found in input-data/raw/")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_eda()
