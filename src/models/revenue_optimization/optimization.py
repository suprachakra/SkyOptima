"""
optimization.py: Uses optimization techniques to determine the best pricing strategy.
Here we use a simplified linear programming example.
"""

import numpy as np
import logging
from scipy.optimize import linprog

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Optimization")

def optimize_pricing(base_price, demand_forecast):
    """
    Optimize pricing using linear programming.
    
    Args:
        base_price (float): The baseline fare.
        demand_forecast (float): Forecasted demand.
    
    Returns:
        float: Optimized price.
    """
    # Objective: maximize revenue, which is price * demand.
    # For a linear programming formulation, we minimize the negative revenue.
    # Variables: price adjustment x.
    # Revenue = (base_price + x) * demand_forecast.
    # To linearize, we consider the demand forecast as constant.
    
    # In our simple LP, we minimize: - (base_price + x) * demand_forecast.
    # Since demand_forecast is constant, minimize: -x * demand_forecast (base price constant).
    c = [-demand_forecast]  # coefficient for x
    
    # Constraints: price adjustment between -20 and 20.
    bounds = [(-20, 20)]
    
    result = linprog(c, bounds=bounds, method='highs')
    if result.success:
        optimized_price = base_price + result.x[0]
        logger.info("Optimized price calculated: %.2f", optimized_price)
        return optimized_price
    else:
        logger.error("Optimization failed: %s", result.message)
        return base_price

if __name__ == "__main__":
    base_price = 250.0
    forecast_demand = 120
    opt_price = optimize_pricing(base_price, forecast_demand)
    print("Optimized Price:", opt_price)
