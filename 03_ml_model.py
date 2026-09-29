import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

print("Loading Cleaned Dataset...")
df = pd.read_csv('cleaned_churn_data.csv')

# Drop Identifier column
if 'CustomerID' in df.columns:
    df.drop(columns=['CustomerID'], inplace=True)

# Separate Features and Target
X_raw = df.drop(columns=['Churn'])
y = df['Churn']

# Categorical Encoding
X = pd.get_dummies(X_raw, drop_first=True)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Building
print("Training Random Forest Classifier...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print("\n==================================")
print(f"Model Accuracy Score : {acc * 100:.2f}%")
print("==================================\n")

# Save predictions for Power BI
df['Predicted_Churn'] = model.predict(X)
df['Churn_Probability'] = model.predict_proba(X)[:, 1].round(2)
df.to_csv('final_churn_predictions.csv', index=False)

print("SUCCESS! Final predictions saved as 'final_churn_predictions.csv'.")