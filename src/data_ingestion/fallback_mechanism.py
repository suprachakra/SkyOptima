"""
fallback_mechanism.py: Provides a fallback mechanism for data ingestion.
If the primary data source fails, an alternative source is used.
"""

import logging
import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("FallbackMechanism")

def load_data_with_fallback(primary_path: str, fallback_path: str) -> pd.DataFrame:
    """Load data from the primary path, fallback to the alternative path on failure.
    
    Args:
        primary_path (str): Primary CSV file path.
        fallback_path (str): Fallback CSV file path.
    
    Returns:
        pd.DataFrame: Loaded DataFrame.
    """
    try:
        df = pd.read_csv(primary_path)
        logger.info("Data loaded successfully from primary source: %s", primary_path)
        return df
    except Exception as e:
        logger.error("Primary data load failed (%s), attempting fallback: %s", e, fallback_path)
        try:
            df = pd.read_csv(fallback_path)
            logger.info("Data loaded successfully from fallback source: %s", fallback_path)
            return df
        except Exception as e:
            logger.error("Fallback data load failed: %s", e)
            raise

if __name__ == "__main__":
    df = load_data_with_fallback("data/raw/bookings.csv", "data/raw/bookings_backup.csv")
    print(df.head())
