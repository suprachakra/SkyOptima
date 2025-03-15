"""
test_data_ingestion.py: Unit tests for data ingestion modules.
"""

import unittest
import pandas as pd
from src.data_ingestion.load_data import load_csv

class TestDataIngestion(unittest.TestCase):

    def test_load_csv_success(self):
        # Create a small CSV file for testing
        test_csv = "tests/test_bookings.csv"
        data = "BookingID,PassengerName,FlightNumber,DepartureDate,Class,Price,Status\nB0001,John Doe,AI101,2024-05-01,Economy,250,Confirmed"
        with open(test_csv, "w") as f:
            f.write(data)
        df = load_csv(test_csv)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 1)
    
    def test_load_csv_failure(self):
        with self.assertRaises(Exception):
            load_csv("non_existent_file.csv")

if __name__ == '__main__':
    unittest.main()
