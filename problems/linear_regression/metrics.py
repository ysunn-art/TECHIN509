"""Evaluation metrics for regression models."""

import numpy as np


def mse(y_true, y_pred):
    """
    Calculate Mean Squared Error.

    Args:
        y_true (np.ndarray): True target values, shape (n_samples,)
        y_pred (np.ndarray): Predicted values, shape (n_samples,)

    Returns:
        float: Mean squared error

    Formula:
        MSE = (1/n) * Σ(y_true - y_pred)²
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    return np.mean((y_true - y_pred) ** 2)


def r2_score(y_true, y_pred):
    """
    Calculate R² (coefficient of determination) score.

    Args:
        y_true (np.ndarray): True target values, shape (n_samples,)
        y_pred (np.ndarray): Predicted values, shape (n_samples,)

    Returns:
        float: R² score (1.0 is perfect, can be negative)

    Formula:
        R² = 1 - (SS_res / SS_tot)
        where SS_res = Σ(y_true - y_pred)²
              SS_tot = Σ(y_true - mean(y_true))²
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)

    return 1 - (ss_res / ss_tot)
