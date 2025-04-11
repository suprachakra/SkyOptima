"""
Implements a Predictive Fare Neural Network using TensorFlow/Keras.
Incorporates an LSTM layer with an attention mechanism to aggregate multiple data inputs.
"""

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, LSTM, Dense, Dropout, Attention
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("GenAIPricing")

def build_predictive_fare_model(input_shape: tuple) -> Model:
    """
    Build and compile a predictive fare model with an attention mechanism.
    
    Args:
        input_shape (tuple): The shape of the input data (timesteps, features).
    
    Returns:
        Model: The compiled Keras model.
    """
    ts_input = Input(shape=input_shape, name="time_series_input")
    
    # LSTM layer for capturing temporal patterns
    lstm_out = LSTM(128, return_sequences=True, activation='tanh')(ts_input)
    dropout_out = Dropout(0.2)(lstm_out)
    
    # Attention mechanism to enhance important features
    attn_out = Attention(name="attention_layer")([dropout_out, dropout_out])
    
    # Dense output layer for fare prediction from the last timestep
    dense_out = Dense(1, activation="linear")(attn_out[:, -1, :])
    
    model = Model(inputs=ts_input, outputs=dense_out, name="PredictiveFareModel")
    model.compile(optimizer="adam", loss="mse")
    logger.info("Built Predictive Fare Model with input shape %s", input_shape)
    return model

if __name__ == "__main__":
    input_shape = (10, 5)
    model = build_predictive_fare_model(input_shape)
    model.summary()
    
    # Dummy data for training
    X_dummy = np.random.rand(100, 10, 5)
    y_dummy = np.random.rand(100, 1)
    model.fit(X_dummy, y_dummy, epochs=5, batch_size=8, verbose=1)
    logger.info("GenAI Pricing model training completed.")
