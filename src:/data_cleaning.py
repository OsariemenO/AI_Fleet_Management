import pandas as pd
from sklearn.preprocessing import StandardScaler

# Function to clean and preprocess fleet data
def clean_fleet_data(df):
    # Fill missing values in 'fuel_efficiency' column with the mean
    df['fuel_efficiency'].fillna(df['fuel_efficiency'].mean(), inplace=True)
    
    # Handle categorical data (converting 'vehicle_type' to numerical codes)
    df['vehicle_type'] = df['vehicle_type'].astype('category')
    df['vehicle_type'] = df['vehicle_type'].cat.codes

    # Normalize numerical columns (e.g., 'engine_hours' and 'maintenance_cost')
    scaler = StandardScaler()
    df[['engine_hours', 'maintenance_cost']] = scaler.fit_transform(df[['engine_hours', 'maintenance_cost']])

    return df

# Load the data and clean it
fleet_data = pd.read_csv('data/fleet_data.csv')
cleaned_fleet_data = clean_fleet_data(fleet_data)
cleaned_fleet_data.to_csv('data/cleaned_fleet_data.csv', index=False)

print("Data cleaning complete!")
