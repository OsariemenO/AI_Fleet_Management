# AI-Powered Fleet Management: Predictive Maintenance

## Overview

The AI-Powered Fleet Management project aims to revolutionize fleet operations by leveraging artificial intelligence to predict maintenance needs, optimize fuel consumption, and reduce overall operational costs. This platform combines machine learning models, IoT data, and predictive analytics to monitor fleet performance in real time, helping companies improve efficiency, reduce downtime, and contribute to sustainability goals.

### Key Features:
- Predictive maintenance to reduce vehicle breakdowns.
- Route optimization based on fuel efficiency and vehicle status.
- Real-time monitoring of fleet conditions.
- Integration with IoT data for comprehensive fleet management.

## Installation Instructions

### Prerequisites:
- Python 3.x
- `pip` for installing Python packages
- A virtual environment (optional, but recommended)

### Steps to Install:
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/OsariemenO/AI_Fleet_Management.git
   cd AI_Fleet_Management
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Instructions

1. To run the predictive maintenance model, execute the following in your terminal:
   ```bash
   python predict_maintenance.py
   ```

2. The model will output the accuracy of its predictions and predict the maintenance risk for a sample vehicle.

3. You can modify the sample input to test the model with different vehicle data.

## Methodology

This project utilizes a **Random Forest Classifier** model to predict vehicle maintenance needs based on several features, such as:
- Engine hours
- Fuel efficiency
- Maintenance cost

The model was trained on a sample dataset to predict the likelihood of a vehicle breakdown, enabling proactive maintenance scheduling.

### Model Training:
- The dataset includes historical maintenance data, such as engine hours, fuel efficiency, and repair costs.
- The model uses these features to predict the risk of breakdown, allowing fleet managers to make data-driven decisions about when to schedule maintenance.

## Contributions

Contributions are welcome! To contribute:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a pull request

Please ensure that your code is well-documented and that all tests pass before submitting a pull request.

## License

This project is licensed under the terms of the **Apache License 2.0**.
