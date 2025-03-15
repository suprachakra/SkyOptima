"""
simulation.py: Simulates various pricing scenarios using Monte Carlo methods.
"""

import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Simulation")

def monte_carlo_simulation(base_price, demand_forecast, iterations=1000):
    """
    Run Monte Carlo simulations to assess revenue outcomes under varying demand conditions.
    
    Args:
        base_price (float): The baseline fare.
        demand_forecast (float): Forecasted demand.
        iterations (int): Number of simulation iterations.
    
    Returns:
        float: Average simulated revenue.
    """
    revenues = []
    for i in range(iterations):
        # Simulate demand variation as a random factor around forecast
        simulated_demand = np.random.normal(loc=demand_forecast, scale=5)
        # Price adjustment as per a simple linear model (example)
        price = base_price + 0.1 * (simulated_demand - demand_forecast)
        revenue = price * simulated_demand
        revenues.append(revenue)
    avg_revenue = np.mean(revenues)
    logger.info("Monte Carlo Simulation: Average revenue = %.2f", avg_revenue)
    return avg_revenue

if __name__ == "__main__":
    base_price = 250.0
    forecast_demand = 120
    avg_rev = monte_carlo_simulation(base_price, forecast_demand, iterations=1000)
    print("Average Simulated Revenue:", avg_rev)
