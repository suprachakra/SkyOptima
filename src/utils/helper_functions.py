"""
helper_functions.py: Contains common helper functions used across SkyOptima.
"""

import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("HelperFunctions")

def normalize_series(series: pd.Series) -> pd.Series:
    """Normalize a pandas Series between 0 and 1."""
    normalized = (series - series.min()) / (series.max() - series.min())
    logger.info("Series normalized.")
    return normalized

def fill_missing_with_mean(series: pd.Series) -> pd.Series:
    """Fill missing values in a Series with the mean."""
    filled = series.fillna(series.mean())
    logger.info("Missing values filled with mean.")
    return filled

def calculate_percentage_change(new, old):
    """Calculate percentage change between two values."""
    try:
        change = ((new - old) / old) * 100
    except ZeroDivisionError:
        change = 0
    return change

if __name__ == "__main__":
    # Example usage:
    s = pd.Series([1, 2, np.nan, 4])
    print(normalize_series(s))
    print(fill_missing_with_mean(s))
    print(calculate_percentage_change(120, 100))
