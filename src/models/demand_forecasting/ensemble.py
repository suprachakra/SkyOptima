"""
ensemble.py: Combines predictions from multiple forecasting models using weighted averaging.
"""

import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("EnsembleModel")

def ensemble_predictions(preds_list, weights=None):
    """
    Ensemble multiple model predictions.
    
    Args:
        preds_list (list of np.array): List of prediction arrays from different models.
        weights (list of float, optional): List of weights for each model's predictions. 
                                             If None, equal weights are assumed.
    
    Returns:
        np.array: Combined prediction.
    """
    preds = np.array(preds_list)
    if weights is None:
        weights = np.ones(preds.shape[0]) / preds.shape[0]
    else:
        weights = np.array(weights)
    ensemble_pred = np.average(preds, axis=0, weights=weights)
    logger.info("Ensembled predictions using weights: %s", weights)
    return ensemble_pred

if __name__ == "__main__":
    # Example predictions from 3 models
    pred1 = np.array([100, 110, 120])
    pred2 = np.array([105, 115, 125])
    pred3 = np.array([102, 112, 122])
    combined = ensemble_predictions([pred1, pred2, pred3], weights=[0.3, 0.4, 0.3])
    print("Ensembled Prediction:", combined)
