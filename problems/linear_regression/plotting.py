"""Plotting utilities for linear regression analysis."""

import numpy as np
import matplotlib.pyplot as plt


def plot_predictions(y_true, y_pred, title="Predictions vs True Values"):
    """
    Plot predicted vs true values with y=x reference line.

    Args:
        y_true (np.ndarray): True target values
        y_pred (np.ndarray): Predicted values
        title (str): Plot title
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(y_true, y_pred, alpha=0.6, edgecolors='k')

    # Add y=x reference line
    min_val = min(y_true.min(), y_pred.min())
    max_val = max(y_true.max(), y_pred.max())
    plt.plot([min_val, max_val], [min_val, max_val], 'r--', lw=2, label='Perfect Prediction')

    plt.xlabel('True Values', fontsize=12)
    plt.ylabel('Predicted Values', fontsize=12)
    plt.title(title, fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_residuals(y_true, y_pred, title="Residual Plot"):
    """
    Plot residuals (errors) vs predicted values.

    Args:
        y_true (np.ndarray): True target values
        y_pred (np.ndarray): Predicted values
        title (str): Plot title
    """
    residuals = y_true - y_pred

    plt.figure(figsize=(8, 6))
    plt.scatter(y_pred, residuals, alpha=0.6, edgecolors='k')
    plt.axhline(y=0, color='r', linestyle='--', lw=2)

    plt.xlabel('Predicted Values', fontsize=12)
    plt.ylabel('Residuals', fontsize=12)
    plt.title(title, fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_fitted_curve(X, y_true, y_pred, title="Fitted Curve"):
    """
    Plot true data points and fitted curve (for 1D features).

    Args:
        X (np.ndarray): Feature values (1D)
        y_true (np.ndarray): True target values
        y_pred (np.ndarray): Predicted values
        title (str): Plot title
    """
    # Sort by X for smooth curve
    sort_idx = np.argsort(X.flatten())
    X_sorted = X.flatten()[sort_idx]
    y_pred_sorted = y_pred[sort_idx]

    plt.figure(figsize=(8, 6))
    plt.scatter(X, y_true, alpha=0.6, label='True Data', edgecolors='k')
    plt.plot(X_sorted, y_pred_sorted, 'r-', lw=2, label='Fitted Curve')

    plt.xlabel('X', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title(title, fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
