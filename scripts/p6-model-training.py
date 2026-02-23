import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

def train_fraud_model():
    # Load our balanced 50/50 dataset [cite: 2026-02-23]
    df = pd.read_csv('input-data/raw/balanced_creditcard.csv')
    
    # X = features (all columns except 'Class')
    # y = target (the 'Class' column) [cite: 2026-02-23]
    X = df.drop('Class', axis=1)
    y = df['Class']
    
    # Split: 80% to learn, 20% to test the AI's skills [cite: 2026-02-23]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the Logistic Regression model [cite: 2026-02-23]
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    
    # Get the results [cite: 2026-02-23]
    predictions = model.predict(X_test)
    print("\n" + "="*35)
    print("   PHASE 6: AI TRAINING RESULTS")
    print("="*35)
    print(classification_report(y_test, predictions))

if __name__ == "__main__":
    train_fraud_model()
