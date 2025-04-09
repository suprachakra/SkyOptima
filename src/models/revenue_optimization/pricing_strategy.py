"""
pricing_strategy.py: Implements a dynamic pricing strategy module.
Uses forecasted demand and pricing rules to recommend optimal fares.
"""

import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("PricingStrategy")

def calculate_optimal_price(base_price, forecast_demand, elasticity=0.1, carbon_price=98, emissions=1.0):
    """
    Calculate the optimal price based on forecast demand, price elasticity, and carbon cost.
    
    Args:
        base_price (float): The baseline fare.
        forecast_demand (float): Forecasted demand (e.g., booking count).
        elasticity (float): Price elasticity factor.
        carbon_price (float): Carbon cost per ton (default from EU ETS, e.g., €98).
        emissions (float): Route-specific emission factor (tons CO2 per passenger).
    
    Returns:
        float: Recommended optimal price.
    """
    adjustment = elasticity * (forecast_demand - 100)  # Adjust if demand exceeds baseline
    carbon_adjustment = carbon_price * emissions  # Incorporate sustainability cost
    optimal_price = base_price + adjustment + carbon_adjustment
    return optimal_price

if __name__ == "__main__":
    base = 250.0
    demand_forecast = 120  # Example forecasted demand
    price = calculate_optimal_price(base, demand_forecast)
    print("Optimal Price:", price)
