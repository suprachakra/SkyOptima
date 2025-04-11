"""
Extracts and engineers features from raw data for modeling.
Enhanced to incorporate Islamic travel calendars and customer loyalty features.
"""

import pandas as pd
import numpy as np
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("FeatureExtraction")

def add_temporal_features(df: pd.DataFrame) -> pd.DataFrame:
    """Extract basic temporal features."""
    df['DepartureDate'] = pd.to_datetime(df['DepartureDate'], errors='coerce')
    df['DepartureMonth'] = df['DepartureDate'].dt.month
    df['DepartureDay'] = df['DepartureDate'].dt.day
    df['DepartureWeekday'] = df['DepartureDate'].dt.weekday
    return df

def add_rolling_features(df: pd.DataFrame, window: int = 3) -> pd.DataFrame:
    """Compute rolling averages for price."""
    if 'Price' in df.columns:
        df['PriceRollingAvg'] = df['Price'].rolling(window=window, min_periods=1).mean()
    return df

def integrate_halal_calendar(df: pd.DataFrame) -> pd.DataFrame:
    """
    Incorporate a Halal event indicator based on an external Islamic travel event calendar.
    For demonstration, mark dates between 2024-06-10 and 2024-06-20 as Halal event period.
    """
    df['HalalEventIndicator'] = df['DepartureDate'].apply(
        lambda date: 1 if pd.notnull(date) and datetime(2024, 6, 10) <= date <= datetime(2024, 6, 20) else 0)
    return df

def integrate_loyalty_data(df: pd.DataFrame, loyalty_df: pd.DataFrame) -> pd.DataFrame:
    """
    Merge loyalty program data into the main DataFrame to create a LoyaltyIndex feature.
    
    Assumes loyalty_df contains columns 'BookingID' and 'LoyaltyScore'.
    """
    merged_df = pd.merge(df, loyalty_df[['BookingID', 'LoyaltyScore']], on='BookingID', how='left')
    merged_df['LoyaltyScore'] = merged_df['LoyaltyScore'].fillna(0)
    return merged_df

def extract_features(df: pd.DataFrame, loyalty_df: pd.DataFrame = None) -> pd.DataFrame:
    """
    Extract and generate features from the raw DataFrame.
    Optionally integrate loyalty data if provided.
    """
    df = add_temporal_features(df)
    df = add_rolling_features(df)
    df = integrate_halal_calendar(df)
    if loyalty_df is not None:
        df = integrate_loyalty_data(df, loyalty_df)
    if 'Price' in df.columns and 'DepartureWeekday' in df.columns:
        df['WeekdayPriceFactor'] = df['Price'] * (df['DepartureWeekday'] + 1)
    logger.info("Feature extraction completed with extended features.")
    return df

if __name__ == "__main__":
    df = pd.read_csv("data/raw/bookings.csv")
    # Simulate loyalty data
    loyalty_data = {"BookingID": df["BookingID"].unique(), "LoyaltyScore": np.random.randint(1, 6, size=len(df["BookingID"].unique()))}
    loyalty_df = pd.DataFrame(loyalty_data)
    features_df = extract_features(df, loyalty_df)
    print(features_df.head())
