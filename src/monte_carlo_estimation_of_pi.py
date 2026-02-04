# Auto-generated from: Monte Carlo_estimation of _pi.ipynb
# Run as a script or import functions from this module.

import numpy as np

n = 1000000
x = np.random.uniform(-1,1,n)
y = np.random.uniform(-1,1,n)

inside = np.sum(x**2 + y**2 <= 1)
pi_estimate = 4 * inside / n
pi_estimate


