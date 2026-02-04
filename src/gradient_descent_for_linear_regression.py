# Auto-generated from: Gradient Descent for linear regression.ipynb
# Run as a script or import functions from this module.

import numpy as np

np.random.seed(0)
X = 2 * np.random.rand(100,1)
y = 4 + 3*X + np.random.randn(100,1)

X_b = np.c_[np.ones((100,1)), X]
theta = np.random.randn(2,1)

alpha = 0.1
m = len(X)

for _ in range(1000):
    gradients = 2/m * X_b.T @ (X_b @ theta - y)
    theta -= alpha * gradients

theta


