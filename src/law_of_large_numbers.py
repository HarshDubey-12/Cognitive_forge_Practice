# Auto-generated from: Law_of_large numbers.ipynb
# Run as a script or import functions from this module.

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

n = 100000
coin_flips = np.random.binomial(1, 0.5, n)
cumulative_mean = np.cumsum(coin_flips) / np.arange(1, n+1)

plt.plot(cumulative_mean)
plt.axhline(0.5, color='red', linestyle='--')
plt.title("Law of Large Numbers")
plt.show()


