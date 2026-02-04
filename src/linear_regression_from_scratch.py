# Auto-generated from: linear regression from scratch.ipynb
# Run as a script or import functions from this module.

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
X = 2 * np.random.rand(100,1)
y = 4 + 3*X + np.random.randn(100,1)

X_b = np.c_[np.ones((100,1)), X]
theta = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y
theta


