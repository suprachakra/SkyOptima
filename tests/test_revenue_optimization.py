#!/usr/bin/env python3
"""
test_revenue_optimization.py: Unit tests for revenue optimization modules.
"""

import unittest
from src.models.revenue_optimization.pricing_strategy import calculate_optimal_price

class TestRevenueOptimization(unittest.TestCase):

    def test_pricing_strategy(self):
        base_price = 250.0
        forecast_demand = 120
        optimal_price = calculate_optimal_price(base_price, forecast_demand)
        # Assert optimal_price is a float and within a reasonable range
        self.assertIsInstance(optimal_price, float)
        self.assertGreater(optimal_price, 240)
        self.assertLess(optimal_price, 300)

if __name__ == '__main__':
    unittest.main()
