"""
Batch prediction block for bike demand prediction.
"""

import os
import pandas as pd
import mlflow.sklearn

FINAL_DATA_PATH = 'data/final'
MODEL_PATH = 'models'
PREDICTIONS_PATH = 'data/predictions'

def execute(**kwargs):
    """Generate predictions using the trained model."""
    try:
        print("Starting batch prediction...")

        # Ensure predictions directory exists
        os.makedirs(PREDICTIONS_PATH, exist_ok=True)
        print(f"Predictions directory: {PREDICTIONS_PATH}")

        # Load the trained model
        model_file = os.path.join(MODEL_PATH, 'random_forest_model.pkl')
        print(f"Loading model from {model_file}")
        model = mlflow.sklearn.load_model(model_file)

        # Load test data
        test_file = os.path.join(FINAL_DATA_PATH, 'test_bikes_final.csv')
        print(f"Loading test data from {test_file}")
        test_data = pd.read_csv(test_file)

        # Generate predictions
        predictions = model.predict(test_data)

        # Save predictions
        predictions_df = pd.DataFrame({'prediction': predictions})
        predictions_file = os.path.join(PREDICTIONS_PATH, 'predictions.csv')
        predictions_df.to_csv(predictions_file, index=False)
        print(f"Predictions saved to {predictions_file}")

        print("Batch prediction completed successfully.")

    except FileNotFoundError as e:
        print(f"File not found: {e}")
        raise
    except Exception as e:
        print(f"An error occurred during batch prediction: {e}")
        raise


if __name__ == "__main__":
    execute()
