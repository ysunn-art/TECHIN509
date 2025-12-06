"""Data splitting utilities."""

import numpy as np


def train_test_split(X, y, test_size=0.2, random_state=None, shuffle=True):
    """
    Split arrays into random train and test subsets.

    Args:
        X (np.ndarray): Feature matrix, shape (n_samples, n_features)
        y (np.ndarray): Target vector, shape (n_samples,)
        test_size (float): Proportion of dataset for test (0.0 to 1.0)
        random_state (int, optional): Random seed for reproducibility
        shuffle (bool): Whether to shuffle data before splitting

    Returns:
        tuple: (X_train, X_test, y_train, y_test)

    Example:
        >>> X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
        >>> y = np.array([1, 2, 3, 4])
        >>> X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
    """
    X = np.asarray(X)
    y = np.asarray(y)

    n_samples = X.shape[0]
    n_test = int(n_samples * test_size)
    n_train = n_samples - n_test

    # Set random seed for reproducibility
    if random_state is not None:
        np.random.seed(random_state)

    # Create indices
    indices = np.arange(n_samples)

    # Shuffle if requested
    if shuffle:
        np.random.shuffle(indices)

    # Split indices
    train_indices = indices[:n_train]
    test_indices = indices[n_train:]

    # Split data
    X_train = X[train_indices]
    X_test = X[test_indices]
    y_train = y[train_indices]
    y_test = y[test_indices]

    return X_train, X_test, y_train, y_test
