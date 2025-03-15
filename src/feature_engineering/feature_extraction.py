"""
feature_extraction.py: Extracts and engineers features from raw data for modeling.
Includes creation of temporal features, rolling averages, and interaction terms.
"""

import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("FeatureExtraction")

def extract_features(df: pd.DataFrame) -> pd.DataFrame:
    """Extract and generate features from the raw DataFrame.
    
    Args:
        df (pd.DataFrame): Input DataFrame with raw booking data.
    
    Returns:
        pd.DataFrame: DataFrame with additional features.
    """
    # Ensure DepartureDate is in datetime format
    df['DepartureDate'] = pd.to_datetime(df['DepartureDate'], errors='coerce')
    
    # Extract temporal features
    df['DepartureMonth'] = df['DepartureDate'].dt.month
    df['DepartureDay'] = df['DepartureDate'].dt.day
    df['DepartureWeekday'] = df['DepartureDate'].dt.weekday
    
    # Create a rolling average of Price over a window of 3 (example)
    df['PriceRollingAvg'] = df['Price'].rolling(window=3, min_periods=1).mean()
    
    # Interaction term: Example, Price adjusted by a weekday factor
    df['WeekdayPriceFactor'] = df['Price'] * (df['DepartureWeekday'] + 1)
    
    logger.info("Feature extraction completed.")
    return df

if __name__ == "__main__":
    df = pd.read_csv("data/raw/bookings.csv")
    features_df = extract_features(df)
    print(features_df.head())
