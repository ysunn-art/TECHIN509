"""Linear regression models using closed-form solutions."""

import numpy as np
try:
    from .metrics import r2_score
except ImportError:
    from metrics import r2_score


class LinearRegressionClosedForm:
    """
    Linear Regression using the normal equation (closed-form solution).

    Supports:
    - Ordinary Least Squares (OLS) when alpha=0
    - Ridge Regression (L2 regularization) when alpha>0
    - Optional intercept fitting

    Parameters:
        fit_intercept (bool): Whether to calculate intercept (default: True)
        alpha (float): L2 regularization strength (default: 0.0)

    Attributes:
        coef_ (np.ndarray): Coefficient vector (weights)
        intercept_ (float): Intercept term

    Math:
        OLS:   β = (X^T X)^-1 X^T y
        Ridge: β = (X^T X + αI)^-1 X^T y  (intercept not penalized)
    """

    def __init__(self, fit_intercept=True, alpha=0.0):
        """
        Initialize the linear regression model.

        Args:
            fit_intercept (bool): If True, fit intercept term
            alpha (float): L2 regularization strength (>=0)
        """
        self.fit_intercept = fit_intercept
        self.alpha = alpha
        self.coef_ = None
        self.intercept_ = 0.0

    def fit(self, X, y):
        """
        Fit the linear regression model using the normal equation.

        Args:
            X (np.ndarray): Training features, shape (n_samples, n_features)
            y (np.ndarray): Training targets, shape (n_samples,)

        Returns:
            self: Fitted model instance
        """
        X = np.asarray(X)
        y = np.asarray(y)

        # Ensure X is 2D
        if X.ndim == 1:
            X = X.reshape(-1, 1)

        n_samples, n_features = X.shape

        # Handle intercept
        if self.fit_intercept:
            # Center the data (subtract mean)
            X_mean = np.mean(X, axis=0)
            y_mean = np.mean(y)
            X_centered = X - X_mean
            y_centered = y - y_mean
        else:
            X_centered = X
            y_centered = y
            X_mean = np.zeros(n_features)
            y_mean = 0.0

        # Compute coefficients using normal equation
        if self.alpha > 0:
            # Ridge regression: (X^T X + αI)^-1 X^T y
            # Note: Intercept is NOT penalized (we work with centered data)
            XtX = X_centered.T @ X_centered
            regularization = self.alpha * np.eye(n_features)
            self.coef_ = np.linalg.solve(XtX + regularization, X_centered.T @ y_centered)
        else:
            # OLS: (X^T X)^-1 X^T y
            XtX = X_centered.T @ X_centered
            self.coef_ = np.linalg.solve(XtX, X_centered.T @ y_centered)

        # Calculate intercept
        if self.fit_intercept:
            self.intercept_ = y_mean - np.dot(X_mean, self.coef_)
        else:
            self.intercept_ = 0.0

        return self

    def predict(self, X):
        """
        Predict using the linear model.

        Args:
            X (np.ndarray): Features, shape (n_samples, n_features)

        Returns:
            np.ndarray: Predicted values, shape (n_samples,)
        """
        if self.coef_ is None:
            raise ValueError("Model has not been fitted yet. Call fit() first.")

        X = np.asarray(X)

        # Ensure X is 2D
        if X.ndim == 1:
            X = X.reshape(-1, 1)

        return X @ self.coef_ + self.intercept_

    def score(self, X, y):
        """
        Calculate R² score on given data.

        Args:
            X (np.ndarray): Features, shape (n_samples, n_features)
            y (np.ndarray): True targets, shape (n_samples,)

        Returns:
            float: R² score
        """
        y_pred = self.predict(X)
        return r2_score(y, y_pred)
