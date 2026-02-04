# Auto-generated from: 08_Sampling_Distribution_Correlation_Coefficient.ipynb
# Run as a script or import functions from this module.

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

correlations = []

for _ in range(5000):
    x = np.random.normal(0,1,30)
    y = 0.6*x + np.random.normal(0,1,30)
    correlations.append(np.corrcoef(x,y)[0,1])

plt.hist(correlations,bins=50,density=True)
plt.title("Sampling Distribution of Correlation")
plt.show()

