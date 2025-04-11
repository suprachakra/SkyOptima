"""
Module to calculate Passenger Revenue per Available Seat Kilometer (PRASK).

Formula:
    PRASK = TotalRevenue / (AvailableSeats * FlightDistance)
    
Assumptions:
    - TotalRevenue is in currency units (e.g., Euros).
    - AvailableSeatKm is the product of available seats and flight distance (e.g., seat-kilometers).
    - If AvailableSeatKm is zero, the function returns 0.0.
"""

import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("PRASK")

def calculate_prask(total_revenue: float, available_seat_km: float) -> float:
    """
    Calculate PRASK given total revenue and available seat kilometers.
    
    Args:
        total_revenue (float): Total passenger revenue.
        available_seat_km (float): Total available seat kilometers.
    
    Returns:
        float: The PRASK value. Returns 0 if available_seat_km is zero.
    """
    if available_seat_km == 0:
        logger.error("Available seat kilometers is zero, cannot compute PRASK.")
        return 0.0
    prask = total_revenue / available_seat_km
    logger.info("Calculated PRASK: %.2f", prask)
    return prask

if __name__ == "__main__":
    # Example usage: Load processed revenue data and compute PRASK for each flight.
    try:
        df = pd.read_csv("data/processed/revenue_processed.csv", parse_dates=["Date"])
    except Exception as e:
        logger.error("Error loading revenue_processed.csv: %s", e)
        exit(1)

    # If AvailableSeatKm is not provided, create a sample column for demonstration.
    if "AvailableSeatKm" not in df.columns:
        df["AvailableSeatKm"] = 100000  # Example default value: 100,000 seat-kilometers per flight

    # Calculate PRASK for each row
    df["PRASK"] = df.apply(lambda row: calculate_prask(row["TotalRevenue"], row["AvailableSeatKm"]), axis=1)
    
    logger.info("Sample PRASK results:")
    print(df[["Date", "FlightNumber", "TotalRevenue", "AvailableSeatKm", "PRASK"]].head())
