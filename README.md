[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/vMCKbY5v)
# TECHIN 509: Week 8 Assignment

## Submission Instructions

Organize your repository as follows for your submission. Each problem folder must include its own README.md file that clearly states:
- The problem description (copied or summarized).
- How to run the solution (including dependencies and command-line instructions).
- Associate explanations.
- Sample input and output if applicable.

```cmd
root/
│
├── tic_tac_toe/
│   ├── README.md
│   └── (source code files)
│
├── LR/
│   ├── README.md
│   └── (source code files)
│
├── GW/
│   ├── README.md
│   └── (source code files)
│
└── main README.md (optional)
```


## Tic-Tac-Toe Game

You have now implemented a few functions as parts of a Tic-Tac-Toe game. In this assignment, you will complete the provided templates to implement a simple Tic-Tac-Toe game. 

Please carefully read through the README document in problems/tic-tac-toe to understand the project. Then you need to accomplish the following tasks:

1. Create a virtual environment, and install packages in requirements.txt

2. Complete the "draw_board" method of Board class (in board.py file). Commit all your changes and push them to remote.

3. Complete the "check_winner" method of Board class (in board.py file). Commit all your changes and push them to remote.

4. In tests/test_check_winner.py, perform unit test on the check_winner method. Commit all your changes and push them to remote.

5. Play a few games, and record the data. Commit all your changes and push them to remote. 

For tasks 2-3, You may find your previous homework submission helpful. However, you do not necessarily need them all. 


## Linear Regression Toolkit

In this problem, you will implement a small, reusable Linear Regression toolkit using plain classes and NumPy. You’ll build:
- A closed-form linear regression model (with optional L2 regularization)
- Simple preprocessing helpers,
- Metrics for evaluation,
- A train/test split function,
- A Jupyter notebook with experiments.
No packages beyond NumPy and matplotlib for plots.

### **Task 1. Implement the Linear Regression Model**

* Create a class `LinearRegressionClosedForm` in `linear_models.py`.
* The class should support:

  * `fit(X, y)`: estimate coefficients using the **normal equation** with optional L2 regularization.
  * `predict(X)`: return predictions.
  * `score(X, y)`: return R² score.
* Store model parameters in attributes:

  * `coef_` (NumPy array of weights),
  * `intercept_` (float).
* Handle `fit_intercept=True/False`. Ensure intercept is **not penalized** when `alpha > 0`.

### **Task 2. Metrics**

* In `metrics.py`, implement two functions:

  * `mse(y_true, y_pred)` – Mean Squared Error.
  * `r2_score(y_true, y_pred)` – Coefficient of determination.


### **Task 3. Train/Test Split**

* In `selection.py`, implement `train_test_split(X, y, test_size=0.2, random_state=None, shuffle=True)`.
* Return `X_train, X_test, y_train, y_test`.


### **Task 4. Experiments (Notebook)**

Use `examples/demo.ipynb` to demonstrate and test your toolkit. Complete **three experiments**:

1. **Straight Line with Noise**

   * Generate synthetic data: $y = 3 + 2x + \epsilon$, $\epsilon \sim \mathcal{N}(0, 1)$.
   * Split into train/test.
   * Fit the model with `alpha=0.0`.
   * Report learned coefficients, intercept, MSE, and R².
   * Plot predicted vs true values (scatter + y=x line).

2. **Collinearity and Ridge Regularization**

   * Create two highly correlated features (e.g., `x2 = x1 + 0.01 * noise`).
   * Fit models with `alpha ∈ {0.0, 1e-3, 1e-2, 1e-1, 1.0}`.
   * For each `alpha`, record test MSE and weight vector norm $||coef_||_2$.
   * Discuss (3–5 sentences) how increasing `alpha` changes results.

3. **Polynomial Regression**

   * Generate nonlinear data: $y = 1 + 2x - 0.3x^2 + \epsilon$.
   * Compare degree 1, 2, and 5 polynomial features (with and without scaling).
   * Plot fitted curves vs ground truth.
   * Comment briefly: which degree fits best and why?


### **Task 5. Plotting Utilities**

* In `plotting.py`, add helper functions such as:

  * `plot_residuals(y_true, y_pred)`
  * `plot_predictions(y_true, y_pred)`

### **Task 6. Testing**

* Add a file `tests/test_core.py` with at least 3 unit tests:

  1. `predict(X)` output shape matches `(n_samples,)`.
  2. On nearly perfect linear data, recovered `coef_` and `intercept_` are close to true values.
  3. Increasing `alpha` reduces the size of coefficients when features are collinear.

## Deliverables

* source code package with your classes and functions.
* `examples/demo.ipynb` notebook with experiments, plots, and commentary.
* `tests/test_core.py` with basic tests.
* `README.md` describing project structure, usage, and results.


# Grid World Navigation

Build a simple **grid world navigation system**. You will create classes to represent positions, a world with walls, an agent that moves, and a pathfinder that can find the shortest path from a start to a goal.

## Tasks

### **Task 1. Represent Positions**

* Implement a class `Position(row, col)` that represents a grid cell.
* Add:

  * `neighbors_4()` → returns the four neighboring positions (up, down, left, right).
  * `__eq__` and `__hash__` → so positions can be compared and stored in sets/dicts.
  * `__repr__` → returns a nice string like `"(2,3)"`.

### **Task 2. Build the Grid World**

* Implement `GridWorld(rows, cols, walls=None, start=None, goal=None)` with:

  * `in_bounds(pos)` → returns `True` if inside the grid.
  * `passable(pos)` → returns `True` if not a wall.
  * `is_goal(pos)` → returns `True` if this position is the goal.
  * `place_wall(pos)` / `remove_wall(pos)` → allow modifying the world.
  * `render(path=None, agent=None)` → prints the grid in ASCII, using:

    * `#` for walls, `.` for empty, `S` for start, `G` for goal, `A` for agent, `*` for path.


### **Task 3. Control an Agent**

* Implement `Agent(world, pos=None)` with:

  * `at` (current position, starts at `world.start` if not given).
  * `can_move_to(pos)` → checks if the position is inside the grid and not a wall.
  * `step(direction)` → moves up/down/left/right if possible, returns `True` if moved.
  * `reset(pos)` → teleports the agent (used for testing).

### **Task 4. Implement Pathfinding**

* Create `Pathfinder(world)` with:

  * `find_path(start, goal)` → returns a list of positions from start to goal (or `None` if no path).

---

### **Task 5. Demonstrate in a Script or Notebook**

* Build a small 5×7 world with:

  * A start position (S), a goal (G), and some walls.
* Print the initial world.
* Use BFS to find a path.
* Print the path length and nodes expanded.
* Render the path on the grid.
* Step the agent along the path, re-rendering at each step.


