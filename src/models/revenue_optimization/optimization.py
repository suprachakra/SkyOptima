"""
optimization.py: Determines the best pricing strategy using optimization techniques.
The module has been updated to factor in dynamic currency hedging.
"""

import numpy as np
import logging
from scipy.optimize import linprog

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Optimization")

def optimize_pricing(base_price: float, forecast_demand: float, currency_factor: float = 1.02) -> float:
    """
    Optimize pricing using linear programming, incorporating a dynamic currency hedge.
    
    Args:
        base_price (float): The baseline fare.
        forecast_demand (float): Forecasted demand.
        currency_factor (float): Currency hedge adjustment factor.
    
    Returns:
        float: Optimized price.
    """
    # Objective: maximize revenue = (base_price + x) * forecast_demand
    # For minimization: minimize -x * forecast_demand, because base_price is constant.
    c = [-forecast_demand]  # Negative coefficient to maximize x
    
    # Constraint: price adjustment x is between -20 and 20
    bounds = [(-20, 20)]
    
    result = linprog(c, bounds=bounds, method='highs')
    if result.success:
        optimized_price = (base_price + result.x[0]) * currency_factor
        logger.info("Optimized price calculated: %.2f", optimized_price)
        return optimized_price
    else:
        logger.error("Optimization failed: %s", result.message)
        return base_price

if __name__ == "__main__":
    base_price = 250.0
    forecast_demand = 120
    opt_price = optimize_pricing(base_price, forecast_demand)
    print("Optimized Price: €%.2f" % opt_price)
