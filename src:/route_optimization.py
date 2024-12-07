import numpy as np
from scipy.spatial.distance import cdist

# Function to calculate optimal routes using Euclidean distance
def calculate_route(locations):
    # Calculate distance matrix
    dist_matrix = cdist(locations, locations, metric='euclidean')

    # Print the distance matrix (example)
    print("Distance Matrix:")
    print(dist_matrix)

    # Additional logic for optimization could be added here (e.g., using TSP algorithms)
    # For now, let's return the distance matrix
    return dist_matrix

# Example: list of locations (latitude, longitude)
locations = [(34.0522, -118.2437), (36.1699, -115.1398), (37.7749, -122.4194)]
route_distances = calculate_route(locations)
