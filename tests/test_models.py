"""
test_models.py: Unit tests for forecasting models.
Tests ARIMA model training as an example.
"""

import unittest
import pandas as pd
from src.models.demand_forecasting.arima_model import train_arima_model

class TestModels(unittest.TestCase):

    def test_arima_model_training(self):
        # Create a simple time series
        dates = pd.date_range(start="2024-05-01", periods=10, freq='D')
        data = [50000 + i*100 for i in range(10)]
        df = pd.DataFrame({"Date": dates, "TotalRevenue": data})
        df.sort_values("Date", inplace=True)
        time_series = df["TotalRevenue"]
        model_fit = train_arima_model(time_series, order=(1,1,1))
        # Assert that model_fit has the necessary attributes
        self.assertTrue(hasattr(model_fit, 'forecast'))
    
if __name__ == '__main__':
    unittest.main()
