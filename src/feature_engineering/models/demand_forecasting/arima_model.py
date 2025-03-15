"""
arima_model.py: Implements ARIMA model for demand forecasting using statsmodels.
"""

import pandas as pd
import logging
from statsmodels.tsa.arima.model import ARIMA

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ARIMAModel")

def train_arima_model(time_series: pd.Series, order=(1, 1, 1)):
    """Train an ARIMA model on the provided time series.
    
    Args:
        time_series (pd.Series): The time series data.
        order (tuple): The (p, d, q) order of the ARIMA model.
    
    Returns:
        ARIMAResults: Fitted ARIMA model results.
    """
    try:
        model = ARIMA(time_series, order=order)
        model_fit = model.fit()
        logger.info("ARIMA model trained successfully with order %s", order)
        return model_fit
    except Exception as e:
        logger.error("Error training ARIMA model: %s", e)
        raise

if __name__ == "__main__":
    # Example: Load a sample time series from revenue_processed.csv
    df = pd.read_csv("data/processed/revenue_processed.csv", parse_dates=["Date"])
    df = df.sort_values("Date")
    ts = df["TotalRevenue"]
    model_fit = train_arima_model(ts)
    print(model_fit.summary())
