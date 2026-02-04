# Auto-generated from: 09_Poisson_Process_Interarrival_Times.ipynb
# Run as a script or import functions from this module.

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

rate = 3
inter_arrivals = np.random.exponential(1/rate,1000)
arrival_times = np.cumsum(inter_arrivals)

plt.step(arrival_times, range(len(arrival_times)))
plt.title("Poisson Process Simulation")
plt.show()

