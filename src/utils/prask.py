"""
Module to calculate Passenger Revenue per Available Seat Kilometer (PRASK).

Formula:
    PRASK = TotalRevenue / (AvailableSeatKm)

Assumptions:
    - TotalRevenue is provided in currency units.
    - AvailableSeatKm is calculated as the product of available seats and flight distance.
    - Returns 0.0 if AvailableSeatKm is zero.
"""

import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("PRASK")

def calculate_prask(total_revenue: float, available_seat_km: float) -> float:
    """
    Calculate PRASK from total revenue and available seat kilometers.
    
    Args:
        total_revenue (float): Total passenger revenue.
        available_seat_km (float): Available seat kilometers.
    
    Returns:
        float: PRASK value.
    """
    if available_seat_km == 0:
        logger.error("Available seat kilometers is zero. Cannot compute PRASK.")
        return 0.0
    prask = total_revenue / available_seat_km
    logger.info("Calculated PRASK: %.2f", prask)
    return prask

if __name__ == "__main__":
    try:
        df = pd.read_csv("data/processed/revenue_processed.csv", parse_dates=["Date"])
    except Exception as e:
        logger.error("Error loading revenue_processed.csv: %s", e)
        exit(1)
    if "AvailableSeatKm" not in df.columns:
        df["AvailableSeatKm"] = 100000  # Default value for demonstration
    df["PRASK"] = df.apply(lambda row: calculate_prask(row["TotalRevenue"], row["AvailableSeatKm"]), axis=1)
    logger.info("Sample PRASK results:")
    print(df[["Date", "FlightNumber", "TotalRevenue", "AvailableSeatKm", "PRASK"]].head())
