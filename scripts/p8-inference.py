import pandas as pd
import joblib

def run_detector():
    # Load the saved model brain
    model = joblib.load('models/fraud_detector_v1.pkl')
    
    # Load data for testing
    df = pd.read_csv('input-data/raw/balanced_creditcard.csv')
    
    # Pick 1 random transaction
    sample = df.sample(1)
    true_label = sample['Class'].values[0]
    features = sample.drop('Class', axis=1)
    
    # Predict!
    prediction = model.predict(features)[0]
    
    print("\n" + "*" * 30)
    print("   PHASE 8: FRAUD DETECTOR")
    print("*" * 30)
    print(f"AI PREDICTION: {'FRAUD DETECTED' if prediction == 1 else 'NORMAL TRANSACTION'}")
    print(f"ACTUAL LABEL:  {'FRAUD' if true_label == 1 else 'NORMAL'}")
    print("-" * 30)

if __name__ == "__main__":
    run_detector()
