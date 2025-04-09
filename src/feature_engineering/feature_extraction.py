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
    # Convert date and extract temporal features
    df['DepartureDate'] = pd.to_datetime(df['DepartureDate'], errors='coerce')
    df['DepartureMonth'] = df['DepartureDate'].dt.month
    df['DepartureDay'] = df['DepartureDate'].dt.day
    df['DepartureWeekday'] = df['DepartureDate'].dt.weekday

    # Rolling average of Price
    df['PriceRollingAvg'] = df['Price'].rolling(window=3, min_periods=1).mean()
    df['WeekdayPriceFactor'] = df['Price'] * (df['DepartureWeekday'] + 1)
    
    # Loyalty Feature Extraction
    # Assuming loyalty data is merged into the DataFrame with column 'GuestTier' (e.g., numeric tiers)
    if 'GuestTier' in df.columns:
        df['LoyaltyIndex'] = df['GuestTier'].apply(lambda x: x / 10)  # Normalize tier value (example)
        # Calculate a redemption probability using a logistic function
        df['RedemptionProbability'] = df['LoyaltyIndex'].apply(lambda x: 1 / (1 + np.exp(- (x - 0.5) * 10)))
    
    return df

if __name__ == "__main__":
    df = pd.read_csv("data/raw/bookings.csv")
    features_df = extract_features(df)
    print(features_df.head())
