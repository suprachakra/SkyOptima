"""
clean_data.py: Cleans raw data by removing duplicates, handling missing values, and formatting columns.
"""

import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("CleanData")

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Clean the input DataFrame.
    
    Args:
        df (pd.DataFrame): Raw data DataFrame.
    
    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    # Remove duplicate rows
    initial_count = len(df)
    df = df.drop_duplicates()
    logger.info("Removed %d duplicate rows.", initial_count - len(df))
    
    # Handle missing values: For simplicity, drop rows with missing essential fields
    essential_columns = ['BookingID', 'PassengerName', 'FlightNumber', 'DepartureDate']
    df = df.dropna(subset=essential_columns)
    logger.info("Dropped rows with missing essential columns: %s", essential_columns)
    
    # Convert price to numeric and fill NaNs if any with 0
    if 'Price' in df.columns:
        df['Price'] = pd.to_numeric(df['Price'], errors='coerce').fillna(0)
    
    # Standardize date formats
    if 'DepartureDate' in df.columns:
        df['DepartureDate'] = pd.to_datetime(df['DepartureDate'], errors='coerce')
    
    logger.info("Data cleaning completed.")
    return df

if __name__ == "__main__":
    df = pd.read_csv("data/raw/bookings.csv")
    clean_df = clean_dataframe(df)
    print(clean_df.head())
