"""
Monitoring block for bike demand prediction.
"""

import os
import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

FINAL_DATA_PATH = 'data/final'
PREDICTIONS_PATH = 'data/predictions'
REPORTS_PATH = 'reports'

def execute(**kwargs):
    """Generate monitoring reports using Evidently."""
    try:
        print("Starting monitoring...")

        # Ensure reports directory exists
        os.makedirs(REPORTS_PATH, exist_ok=True)
        print(f"Reports directory: {REPORTS_PATH}")

        # Load test data
        test_file = os.path.join(FINAL_DATA_PATH, 'test_bikes_final.csv')
        predictions_file = os.path.join(PREDICTIONS_PATH, 'predictions.csv')
        print(f"Loading test data from {test_file}")
        print(f"Loading predictions from {predictions_file}")

        test_data = pd.read_csv(test_file)
        predictions = pd.read_csv(predictions_file)

        # Combine test data and predictions for analysis
        if 'prediction' not in predictions.columns:
            raise ValueError("Predictions file must contain a 'prediction' column.")

        test_data['prediction'] = predictions['prediction']

        print("Columns in test data before Evidently:")
        print(test_data.columns)

        # Data Drift Report
        drift_report = Report(metrics=[DataDriftPreset()])
        drift_report.run(reference_data=test_data, current_data=test_data)
        drift_report_file = os.path.join(REPORTS_PATH, 'drift_report.html')
        drift_report.save_html(drift_report_file)
        print(f"Drift report saved to {drift_report_file}")

        print("Monitoring completed successfully.")

    except FileNotFoundError as e:
        print(f"File not found: {e}")
        raise
    except Exception as e:
        print(f"An error occurred during monitoring: {e}")
        raise


if __name__ == "__main__":
    execute()
