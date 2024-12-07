from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# Function to build and train predictive maintenance model
def train_predictive_model(df):
    # Define features and target variable
    X = df[['engine_hours', 'fuel_efficiency', 'maintenance_cost']]
    y = df['breakdown_risk']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    return model, accuracy

# Load the cleaned data
cleaned_data = pd.read_csv('data/cleaned_fleet_data.csv')
model, accuracy = train_predictive_model(cleaned_data)

print(f'Model accuracy: {accuracy * 100:.2f}%')
