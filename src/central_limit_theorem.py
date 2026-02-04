# Auto-generated from: Central Limit Theorem.ipynb
# Run as a script or import functions from this module.

import numpy as np
import matplotlib.pyplot as plt

samples = [np.mean(np.random.exponential(scale=2, size=50)) for _ in range(10000)]

plt.hist(samples, bins=50, density=True)
plt.title("CLT: Distribution of Sample Means")
plt.show()


