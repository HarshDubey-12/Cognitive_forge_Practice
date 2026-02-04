# Auto-generated from: 05_Bayesian_Sequential_Updating_Posterior_Evolution.ipynb
# Run as a script or import functions from this module.

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

np.random.seed(0)

true_p = 0.7
data = np.random.binomial(1,true_p,50)

a,b = 1,1
x = np.linspace(0,1,1000)

for i in range(len(data)):
    if data[i]==1:
        a+=1
    else:
        b+=1

plt.plot(x, beta.pdf(x,a,b))
plt.title("Final Posterior after Sequential Updating")
plt.show()

