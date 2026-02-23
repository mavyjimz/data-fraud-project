import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression

def persist_trained_model():
    # Load the balanced 50/50 dataset from Phase 5 [cite: 2026-02-23]
    df = pd.read_csv('input-data/raw/balanced_creditcard.csv')
    X = df.drop('Class', axis=1)
    y = df['Class']
    
    # Train the model one final time on all available balanced data [cite: 2026-02-23]
    # We use 1000 iterations to match our Phase 6 success
    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)
    
    # Save the "brain" to your models folder [cite: 2026-02-20]
    # .pkl is the standard extension for serialized Python objects [cite: 2026-02-23]
    joblib.dump(model, 'models/fraud_detector_v1.pkl')
    
    print("\n" + "="*30)
    print("   PHASE 7: MODEL SAVED")
    print("="*30)
    print("Target: models/fraud_detector_v1.pkl")

if __name__ == "__main__":
    persist_trained_model()
