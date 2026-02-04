# Auto-generated from: 01_Central_Limit_Theorem_Quantitative_Convergence.ipynb
# Run as a script or import functions from this module.

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

np.random.seed(0)

n = 40
sample_means = np.array([np.mean(np.random.exponential(scale=2, size=n)) 
                         for _ in range(10000)])

mu = 2
sigma = 2
theoretical_std = sigma / np.sqrt(n)

x = np.linspace(min(sample_means), max(sample_means), 1000)

plt.hist(sample_means, bins=50, density=True, alpha=0.6)
plt.plot(x, norm.pdf(x, mu, theoretical_std), 'r')
plt.title("CLT with Theoretical Normal Overlay")
plt.show()

