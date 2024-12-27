from mage_ai.io.file import FileIO
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import os
import pandas as pd

RAW_DATA_PATH = 'data/raw'
PROCESSED_DATA_PATH = 'data/processed'

@data_loader
def load_data(*args, **kwargs):
    """
    Load raw data, process it, and save the processed data.
    """
    try:
        print("Starting data ingestion...")

        # Ensure processed data directory exists
        os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)
        print(f"Processed data directory: {PROCESSED_DATA_PATH}")

        # Load raw data
        train_file = os.path.join(RAW_DATA_PATH, 'train_bikes.csv')
        test_file = os.path.join(RAW_DATA_PATH, 'test_bikes.csv')

        print(f"Loading train data from {train_file}")
        print(f"Loading test data from {test_file}")

        train_data = pd.read_csv(train_file)
        test_data = pd.read_csv(test_file)

        # Perform basic checks
        assert 'datetime' in train_data.columns, "Train data missing 'datetime' column."
        assert 'datetime' in test_data.columns, "Test data missing 'datetime' column."

        # Save processed data using FileIO
        train_output = os.path.join(PROCESSED_DATA_PATH, 'train_bikes_processed.csv')
        test_output = os.path.join(PROCESSED_DATA_PATH, 'test_bikes_processed.csv')

        FileIO().export(train_data, train_output)
        FileIO().export(test_data, test_output)

        print(f"Train data saved to {train_output}")
        print(f"Test data saved to {test_output}")
        print("Data ingestion completed successfully.")

        # Return processed data for further usage
        return {
            'train': train_data,
            'test': test_data,
        }

    except FileNotFoundError as e:
        print(f"File not found: {e}")
        raise
    except Exception as e:
        print(f"An error occurred during data ingestion: {e}")
        raise


@test
def test_output(output, *args) -> None:
    """
    Test the output of the load_data function.
    """
    assert output is not None, 'The output is undefined'
    assert 'train' in output and 'test' in output, 'Output missing train or test data'
    assert isinstance(output['train'], pd.DataFrame), 'Train output is not a DataFrame'
    assert isinstance(output['test'], pd.DataFrame), 'Test output is not a DataFrame'
    print("All tests passed successfully!")
