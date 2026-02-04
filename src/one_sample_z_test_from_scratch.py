# Auto-generated from: One-Sample Z-Test From Scratch.ipynb
# Run as a script or import functions from this module.

import numpy as np
from scipy.stats import norm

np.random.seed(0)
sample = np.random.normal(loc=5, scale=2, size=50)

mu0 = 5
sigma = 2
z = (np.mean(sample) - mu0) / (sigma/np.sqrt(len(sample)))
p_value = 2 * (1 - norm.cdf(abs(z)))
z, p_value


