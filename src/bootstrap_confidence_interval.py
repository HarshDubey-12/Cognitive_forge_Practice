# Auto-generated from: Bootstrap Confidence Interval.ipynb
# Run as a script or import functions from this module.

import numpy as np

data = np.random.normal(10,2,100)

boot_means = []
for _ in range(1000):
    sample = np.random.choice(data, size=len(data), replace=True)
    boot_means.append(np.mean(sample))

np.percentile(boot_means, [2.5,97.5])


