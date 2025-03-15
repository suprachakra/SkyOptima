#!/bin/bash
# run_pipeline.sh: Executes the full ETL, modeling, and optimization pipeline.

echo "Starting SkyOptima Pipeline..."

# Activate virtual environment if needed
# source venv/bin/activate

# Run data ingestion
python3 src/data_ingestion/load_data.py --file data/raw/bookings.csv

# Run data cleaning
python3 src/data_ingestion/clean_data.py --file data/raw/bookings.csv

# Run feature extraction
python3 src/feature_engineering/feature_extraction.py --input data/raw/bookings.csv --output data/processed/bookings_processed.csv

# Train forecasting models (example for ARIMA)
python3 src/models/demand_forecasting/arima_model.py --input data/processed/revenue_processed.csv

# Execute revenue optimization simulation
python3 src/models/revenue_optimization/simulation.py

echo "Pipeline execution completed."
