"""
pricing_strategy.py: Implements a dynamic pricing strategy module.
Uses forecasted demand and pricing rules to recommend optimal fares.
"""

import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("PricingStrategy")

def calculate_optimal_price(base_price, forecast_demand, elasticity=0.1):
    """
    Calculate the optimal price based on forecast demand and price elasticity.
    
    Args:
        base_price (float): The baseline fare.
        forecast_demand (float): Forecasted demand (e.g., booking count).
        elasticity (float): Price elasticity factor.
    
    Returns:
        float: Recommended optimal price.
    """
    # For example: if demand is high, price increases proportionally
    adjustment = elasticity * (forecast_demand - 100)  # 100 as baseline demand
    optimal_price = base_price + adjustment
    logger.info("Calculated optimal price: %.2f (Base: %.2f, Demand: %.2f)", optimal_price, base_price, forecast_demand)
    return optimal_price

if __name__ == "__main__":
    base = 250.0
    demand_forecast = 120  # Example forecasted demand
    price = calculate_optimal_price(base, demand_forecast)
    print("Optimal Price:", price)
