import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Create Dash app
app = dash.Dash(__name__)

# Load sample data
df = pd.read_csv('data/cleaned_fleet_data.csv')

# Define the layout and components of the dashboard
app.layout = html.Div([
    dcc.Graph(
        id='fuel-efficiency',
        figure=px.scatter(df, x='engine_hours', y='fuel_efficiency', color='breakdown_risk')
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
