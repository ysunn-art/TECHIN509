"""
Linear Regression Toolkit

A lightweight implementation of linear regression using closed-form solutions.
Supports ordinary least squares (OLS) and Ridge regression (L2 regularization).
"""

from .linear_models import LinearRegressionClosedForm
from .metrics import mse, r2_score
from .selection import train_test_split
from .plotting import plot_predictions, plot_residuals, plot_fitted_curve

__all__ = [
    'LinearRegressionClosedForm',
    'mse',
    'r2_score',
    'train_test_split',
    'plot_predictions',
    'plot_residuals',
    'plot_fitted_curve',
]

__version__ = '1.0.0'
