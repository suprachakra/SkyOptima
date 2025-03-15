"""
xgboost_model.py: Implements a forecasting model using XGBoost.
"""

import pandas as pd
import xgboost as xgb
import numpy as np
import logging
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("XGBoostModel")

def prepare_features(df: pd.DataFrame, target_column: str, lag: int = 3):
    """Create lag-based features for forecasting.
    
    Args:
        df (pd.DataFrame): Input data.
        target_column (str): The target variable.
        lag (int): Number of lag features.
    
    Returns:
        X, y: Feature matrix and target vector.
    """
    for i in range(1, lag + 1):
        df[f"lag_{i}"] = df[target_column].shift(i)
    df = df.dropna()
    X = df[[f"lag_{i}" for i in range(1, lag + 1)]].values
    y = df[target_column].values
    return X, y

def train_xgboost_model(X, y):
    """Train an XGBoost regression model.
    
    Args:
        X (array): Feature matrix.
        y (array): Target vector.
    
    Returns:
        model: Trained XGBoost model.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)
    logger.info("XGBoost model trained successfully. MSE: %.2f", mse)
    return model

if __name__ == "__main__":
    df = pd.read_csv("data/processed/revenue_processed.csv", parse_dates=["Date"])
    df = df.sort_values("Date")
    X, y = prepare_features(df, "TotalRevenue", lag=3)
    model = train_xgboost_model(X, y)
