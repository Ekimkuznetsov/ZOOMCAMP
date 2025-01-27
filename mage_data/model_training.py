"""
Model training block for bike demand prediction.
"""

import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import mlflow
import mlflow.sklearn

FINAL_DATA_PATH = 'data/final'
DEFAULT_MODEL_PATH = 'models/random_forest_model.pkl'


def execute(model_path=DEFAULT_MODEL_PATH, **kwargs):
    """Train a Random Forest model and log results to MLflow.

    Args:
        model_path (str): Path to save the trained model.
    """
    try:
        print("Starting model training...")

        # Ensure model directory exists
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        print(f"Model directory: {os.path.dirname(model_path)}")

        # Load final training data
        train_file = os.path.join(FINAL_DATA_PATH, 'train_bikes_final.csv')
        print(f"Loading training data from {train_file}")
        train_data = pd.read_csv(train_file)

        # Prepare features and target
        X_train = train_data.drop(columns=['count', 'casual', 'registered'])  # Exclude 'casual' and 'registered'
        y_train = train_data['count']

        # Initialize MLflow
        mlflow.set_experiment('Bike Demand Prediction')

        with mlflow.start_run():
            # Train model
            model = RandomForestRegressor(n_estimators=100, random_state=42)
            model.fit(X_train, y_train)

            # Log model to MLflow
            mlflow.sklearn.log_model(model, "model")
            print("Model logged to MLflow.")

            # Compute and log metrics
            y_pred = model.predict(X_train)
            rmse = np.sqrt(mean_squared_error(y_train, y_pred))
            mlflow.log_metric("rmse", rmse)
            print(f"Training RMSE: {rmse}")

            # Save model locally
            mlflow.sklearn.save_model(model, model_path)
            print(f"Model saved to {model_path}")

        print("Model training completed successfully.")

    except FileNotFoundError as e:
        print(f"File not found: {e}")
        raise
    except Exception as e:
        print(f"An error occurred during model training: {e}")
        raise


if __name__ == "__main__":
    execute()
