"""Unit tests for linear regression toolkit."""

import unittest
import numpy as np
import sys
sys.path.append('..')
from linear_models import LinearRegressionClosedForm
from metrics import mse, r2_score
from selection import train_test_split


class TestLinearRegressionClosedForm(unittest.TestCase):
    """Test cases for LinearRegressionClosedForm class."""

    def test_predict_output_shape(self):
        """Test that predict() returns correct shape."""
        # Create simple dataset
        X = np.array([[1], [2], [3], [4], [5]])
        y = np.array([2, 4, 6, 8, 10])

        # Fit model
        model = LinearRegressionClosedForm()
        model.fit(X, y)

        # Predict
        y_pred = model.predict(X)

        # Check shape
        self.assertEqual(y_pred.shape, (5,))
        self.assertEqual(len(y_pred), len(y))

    def test_coefficient_recovery_perfect_data(self):
        """Test that model recovers true coefficients on perfect linear data."""
        # Generate perfect linear data: y = 3 + 2x
        np.random.seed(42)
        X = np.linspace(0, 10, 100).reshape(-1, 1)
        y = 3 + 2 * X.flatten()  # True intercept=3, slope=2

        # Fit model
        model = LinearRegressionClosedForm(fit_intercept=True, alpha=0.0)
        model.fit(X, y)

        # Check recovered parameters
        self.assertAlmostEqual(model.intercept_, 3.0, places=10)
        self.assertAlmostEqual(model.coef_[0], 2.0, places=10)

        # Check R² is 1.0 (perfect fit)
        r2 = model.score(X, y)
        self.assertAlmostEqual(r2, 1.0, places=10)

    def test_ridge_reduces_coefficients_on_collinear_features(self):
        """Test that increasing alpha reduces coefficient magnitude with collinear features."""
        # Create highly collinear features
        np.random.seed(42)
        n_samples = 100
        x1 = np.random.randn(n_samples)
        x2 = x1 + 0.01 * np.random.randn(n_samples)  # x2 highly correlated with x1
        X = np.column_stack([x1, x2])
        y = 3 * x1 + 2 * x2 + np.random.randn(n_samples) * 0.1

        # Fit with alpha=0 (OLS)
        model_ols = LinearRegressionClosedForm(alpha=0.0)
        model_ols.fit(X, y)
        coef_norm_ols = np.linalg.norm(model_ols.coef_)

        # Fit with alpha=1.0 (Ridge)
        model_ridge = LinearRegressionClosedForm(alpha=1.0)
        model_ridge.fit(X, y)
        coef_norm_ridge = np.linalg.norm(model_ridge.coef_)

        # Ridge should have smaller coefficient norm
        self.assertLess(coef_norm_ridge, coef_norm_ols)

    def test_fit_without_intercept(self):
        """Test model fitting with fit_intercept=False."""
        X = np.array([[1], [2], [3], [4]])
        y = np.array([2, 4, 6, 8])  # y = 2x (no intercept)

        model = LinearRegressionClosedForm(fit_intercept=False)
        model.fit(X, y)

        self.assertAlmostEqual(model.intercept_, 0.0)
        self.assertAlmostEqual(model.coef_[0], 2.0, places=10)


class TestMetrics(unittest.TestCase):
    """Test cases for metrics functions."""

    def test_mse_perfect_predictions(self):
        """Test MSE on perfect predictions."""
        y_true = np.array([1, 2, 3, 4, 5])
        y_pred = np.array([1, 2, 3, 4, 5])

        self.assertAlmostEqual(mse(y_true, y_pred), 0.0)

    def test_mse_known_value(self):
        """Test MSE calculation with known result."""
        y_true = np.array([1, 2, 3])
        y_pred = np.array([1.5, 2.5, 3.5])
        # MSE = mean((0.5, 0.5, 0.5)^2) = mean(0.25, 0.25, 0.25) = 0.25

        self.assertAlmostEqual(mse(y_true, y_pred), 0.25)

    def test_r2_score_perfect_predictions(self):
        """Test R² score on perfect predictions."""
        y_true = np.array([1, 2, 3, 4, 5])
        y_pred = np.array([1, 2, 3, 4, 5])

        self.assertAlmostEqual(r2_score(y_true, y_pred), 1.0)


class TestTrainTestSplit(unittest.TestCase):
    """Test cases for train_test_split function."""

    def test_split_proportions(self):
        """Test that split creates correct proportions."""
        X = np.arange(100).reshape(-1, 1)
        y = np.arange(100)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        self.assertEqual(len(X_train), 80)
        self.assertEqual(len(X_test), 20)
        self.assertEqual(len(y_train), 80)
        self.assertEqual(len(y_test), 20)

    def test_random_state_reproducibility(self):
        """Test that random_state produces reproducible splits."""
        X = np.arange(100).reshape(-1, 1)
        y = np.arange(100)

        X_train1, X_test1, y_train1, y_test1 = train_test_split(X, y, random_state=42)
        X_train2, X_test2, y_train2, y_test2 = train_test_split(X, y, random_state=42)

        np.testing.assert_array_equal(X_train1, X_train2)
        np.testing.assert_array_equal(X_test1, X_test2)


if __name__ == "__main__":
    unittest.main()
