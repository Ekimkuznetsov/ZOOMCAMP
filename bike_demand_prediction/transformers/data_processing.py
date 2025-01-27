if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


from mage_ai.data_preparation.decorators import transformer
import pandas as pd
import os

PROCESSED_DATA_PATH = 'data/processed'
FINAL_DATA_PATH = 'data/final'

@custom
def process_data(*args, **kwargs):
    """
    Process the data and prepare it for model training.
    """
    try:
        print("Starting data processing...")

        # Ensure final data directory exists
        os.makedirs(FINAL_DATA_PATH, exist_ok=True)
        print(f"Final data directory: {FINAL_DATA_PATH}")

        # Load processed data
        train_file = os.path.join(PROCESSED_DATA_PATH, 'train_bikes_processed.csv')
        test_file = os.path.join(PROCESSED_DATA_PATH, 'test_bikes_processed.csv')

        print(f"Loading train data from {train_file}")
        print(f"Loading test data from {test_file}")

        train_data = pd.read_csv(train_file)
        test_data = pd.read_csv(test_file)

        # Feature engineering: Extract datetime features
        for df, name in zip([train_data, test_data], ["train", "test"]):
            df['datetime'] = pd.to_datetime(df['datetime'])
            df['hour'] = df['datetime'].dt.hour
            df['day_of_week'] = df['datetime'].dt.dayofweek
            df['month'] = df['datetime'].dt.month

            # Drop columns not needed
            df.drop(['datetime'], axis=1, inplace=True)

            # Save processed data
            output_file = os.path.join(FINAL_DATA_PATH, f"{name}_bikes_final.csv")
            df.to_csv(output_file, index=False)
            print(f"{name.capitalize()} data saved to {output_file}")

        print("Data processing completed successfully.")

        # Return processed data for further usage in pipeline
        return {
            'train': train_data,
            'test': test_data,
        }

    except FileNotFoundError as e:
        print(f"File not found: {e}")
        raise
    except Exception as e:
        print(f"An error occurred during data processing: {e}")
        raise