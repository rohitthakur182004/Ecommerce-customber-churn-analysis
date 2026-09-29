import pandas as pd
import numpy as np

print("Generating Fresh Cleaned Dataset...")

# Creating a realistic synthetic E-Commerce Churn Dataset
np.random.seed(42)
n_samples = 500

data = {
    'CustomerID': range(1001, 1001 + n_samples),
    'Age': np.random.randint(18, 65, size=n_samples),
    'Tenure': np.random.randint(1, 60, size=n_samples),
    'Usage_Frequency': np.random.randint(1, 30, size=n_samples),
    'Support_Calls': np.random.randint(0, 10, size=n_samples),
    'Payment_Delay': np.random.randint(0, 20, size=n_samples),
    'Subscription_Type': np.random.choice(['Basic', 'Standard', 'Premium'], size=n_samples),
    'Contract_Length': np.random.choice(['Monthly', 'Annual', 'Bi-Annual'], size=n_samples),
    'Total_Spend': np.random.uniform(100, 5000, size=n_samples).round(2),
    'Churn': np.random.choice([0, 1], size=n_samples, p=[0.7, 0.3])
}

df = pd.DataFrame(data)

# Save cleaned CSV directly
df.to_csv('cleaned_churn_data.csv', index=False)
print(f"Data Generation Successful! Created {df.shape[0]} rows and {df.shape[1]} columns.")