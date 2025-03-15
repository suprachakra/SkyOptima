"""
test_feature_engineering.py: Unit tests for feature extraction functions.
"""

import unittest
import pandas as pd
from src.feature_engineering.feature_extraction import extract_features

class TestFeatureEngineering(unittest.TestCase):

    def test_extract_features(self):
        # Create a simple DataFrame for testing
        data = {
            "BookingID": ["B0001", "B0002", "B0003"],
            "PassengerName": ["John Doe", "Jane Smith", "Alex Johnson"],
            "FlightNumber": ["AI101", "AI102", "AI103"],
            "DepartureDate": ["2024-05-01", "2024-05-02", "2024-05-03"],
            "Price": [250, 450, 260]
        }
        df = pd.DataFrame(data)
        df = extract_features(df)
        # Check that new features are created
        self.assertIn("DepartureMonth", df.columns)
        self.assertIn("PriceRollingAvg", df.columns)
        self.assertIn("WeekdayPriceFactor", df.columns)

if __name__ == '__main__':
    unittest.main()
