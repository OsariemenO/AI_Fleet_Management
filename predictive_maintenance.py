import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample dataset
data = {
    'engine_hours': [1000, 2500, 500, 4000, 3000],
    'fuel_efficiency': [12, 10, 14, 8, 9],
    'maintenance_cost': [500, 1200, 200, 3000, 1500],
    'breakdown_risk': [0, 1, 0, 1, 1]  # 0: Low, 1: High
}

# Load dataset
df = pd.DataFrame(data)

# Features and target
X = df[['engine_hours', 'fuel_efficiency', 'maintenance_cost']]
y = df['breakdown_risk']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Sample prediction
new_vehicle = [[2000, 11, 800]]  # engine_hours, fuel_efficiency, maintenance_cost
risk_prediction = model.predict(new_vehicle)
print(f"Predicted Breakdown Risk: {'High' if risk_prediction[0] == 1 else 'Low'}")
