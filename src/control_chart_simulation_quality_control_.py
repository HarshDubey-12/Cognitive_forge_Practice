# Auto-generated from: Control Chart Simulation (Quality Control).ipynb
# Run as a script or import functions from this module.

import numpy as np
import matplotlib.pyplot as plt

process = np.random.normal(50, 2, 100)
mean = np.mean(process)
std = np.std(process)

UCL = mean + 3*std
LCL = mean - 3*std

plt.plot(process)
plt.axhline(UCL, color='red')
plt.axhline(LCL, color='red')
plt.axhline(mean, color='green')
plt.title("Control Chart")
plt.show()


