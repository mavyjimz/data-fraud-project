import pandas as pd

def check_imbalance():
    # Phase 4: Class Distribution Analysis
    # Path is relative to the project root
    df = pd.read_csv('input-data/raw/creditcard.csv')

    counts = df['Class'].value_counts()
    percentage = df['Class'].value_counts(normalize=True) * 100

    print("\n" + "="*30)
    print("    FRAUD CLASS DISTRIBUTION")
    print("="*30)
    print(f"Normal (0): {counts[0]:>7} transactions ({percentage[0]:.2f}%)")
    print(f"Fraud  (1): {counts[1]:>7} transactions ({percentage[1]:.2f}%)")
    print("="*30)

    if percentage[1] < 1.0:
        print("\nALERT: Extreme class imbalance detected!")
        print("Model Training will require special handling (Phase 5).")

if __name__== "__main__":
    check_imbalance() 
