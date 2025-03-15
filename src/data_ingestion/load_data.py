"""
load_data.py: Loads CSV data from a given file path into a pandas DataFrame.
This module supports loading raw data for further processing.
"""

import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("LoadData")

def load_csv(file_path: str) -> pd.DataFrame:
    """Load CSV file into a DataFrame.
    
    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: DataFrame containing CSV data.
    """
    try:
        df = pd.read_csv(file_path)
        logger.info("Successfully loaded data from %s", file_path)
        return df
    except Exception as e:
        logger.error("Error loading data from %s: %s", file_path, e)
        raise

if __name__ == "__main__":
    # Example usage
    df = load_csv("data/raw/bookings.csv")
    print(df.head())
