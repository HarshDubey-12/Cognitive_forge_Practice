# Auto-generated from: Binomial vs Simulation.ipynb
# Run as a script or import functions from this module.

import numpy as np
from scipy.stats import binom

n, p = 10, 0.5
simulated = np.random.binomial(n, p, 100000)
theoretical = binom.pmf(5, n, p)

np.mean(simulated == 5), theoretical

