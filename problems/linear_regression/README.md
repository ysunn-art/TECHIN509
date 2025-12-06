# Reusable Linear Regression Toolkit

This assignment focuses on building a small, reusable Linear Regression toolkit using plain Python classes + NumPy. Implement training via the normal equation with optional L2 (Ridge) regularization, plus a couple of helpers (scaling, polynomial features), metrics, and a short experiment notebook.

## Project Structure

Organize your toolkit as follows:

```
linear_regression/
├── __init__.py
├── linear_models.py      # LinearRegressionClosedForm only
├── metrics.py            # mse, r2_score
├── selection.py          # train_test_split
├── plotting.py           # (optional) residuals, predictions
├── examples/
│   └── demo.ipynb        # your experiments & short write-ups
├── tests/
│   └── test_core.py      # a few sanity tests
└── README.md
```

## File Descriptions

- **`__init__.py`**: Package initialization file
- **`linear_models.py`**: Contains the `LinearRegressionClosedForm` class implementation
- **`metrics.py`**: Evaluation metrics (`mse`, `r2_score`)
- **`selection.py`**: Data splitting utilities (`train_test_split`)
- **`plotting.py`**: Optional visualization functions for residuals and predictions
- **`examples/demo.ipynb`**: Jupyter notebook with experiments and analysis
- **`tests/test_core.py`**: Unit tests for core functionality



