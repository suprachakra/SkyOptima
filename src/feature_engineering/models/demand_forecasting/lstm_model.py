"""
lstm_model.py: Implements an LSTM model for sequential demand forecasting using TensorFlow/Keras.
"""

import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("LSTMModel")

def prepare_data(series, window_size=5):
    """Prepare data for LSTM: create sequences and labels.
    
    Args:
        series (pd.Series): Time series data.
        window_size (int): Number of time steps per sample.
    
    Returns:
        X, y: Arrays for model training.
    """
    X, y = [], []
    for i in range(len(series) - window_size):
        X.append(series[i:i+window_size].values)
        y.append(series[i+window_size])
    return np.array(X), np.array(y)

def build_lstm_model(input_shape):
    """Builds an LSTM model.
    
    Args:
        input_shape (tuple): Shape of the input data (window_size, features).
    
    Returns:
        model: Compiled Keras model.
    """
    model = Sequential([
        LSTM(50, activation='relu', input_shape=input_shape, return_sequences=True),
        Dropout(0.2),
        LSTM(25, activation='relu'),
        Dropout(0.2),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    logger.info("LSTM model built successfully.")
    return model

if __name__ == "__main__":
    # Example usage
    df = pd.read_csv("data/processed/revenue_processed.csv", parse_dates=["Date"])
    df = df.sort_values("Date")
    series = df["TotalRevenue"]
    window_size = 5
    X, y = prepare_data(series, window_size)
    X = X.reshape((X.shape[0], X.shape[1], 1))
    model = build_lstm_model((window_size, 1))
    model.fit(X, y, epochs=10, batch_size=4, verbose=1)
    logger.info("LSTM model training complete.")
