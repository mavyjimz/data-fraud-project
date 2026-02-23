import pandas as pd

def balance_data():
    # Phase 5: Under-sampling logic [cite: 2026-02-04]
    df = pd.read_csv('input-data/raw/creditcard.csv')

    # Separate the classes
    fraud_df = df[df['Class'] ==1]
    normal_df = df[df['Class'] == 0]

    # Randomly select 492 normal transactions to match fraud count
    normal_sample = normal_df.sample(n=492, random_state=492)

    # Combine them into a new balanced dataframe
    balanced_df = pd.concat([fraud_df, normal_sample], axis=0)

    print("---Balancing Complete ---")
    print(f"New Dataset Shape: {balanced_df.shape}")
    print(f"Value Counts:\n{balanced_df['Class'].value_counts()}")

    # Save the balanced data for training in Phase 6
    balanced_df.to_csv('input-data/raw/balanced_creditcard.csv', index=False)
    print("\nFile saved: input-data/raw/balanced_creditcard.csv")

if __name__ == "__main__":
    balance_data()
