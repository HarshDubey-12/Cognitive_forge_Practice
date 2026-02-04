# Auto-generated from: 03_Hypothesis_Testing_Power_Curve_Simulation.ipynb
# Run as a script or import functions from this module.

import numpy as np
from scipy.stats import ttest_1samp
import matplotlib.pyplot as plt

np.random.seed(0)
effect_sizes = np.linspace(0,1,20)
power = []

for effect in effect_sizes:
    rejections = 0
    for _ in range(500):
        sample = np.random.normal(effect,1,30)
        _, p = ttest_1samp(sample,0)
        if p < 0.05:
            rejections += 1
    power.append(rejections/500)

plt.plot(effect_sizes,power)
plt.title("Statistical Power Curve")
plt.xlabel("Effect Size")
plt.ylabel("Power")
plt.show()

