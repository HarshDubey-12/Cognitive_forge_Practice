# Auto-generated from: 04_Monte_Carlo_Option_Pricing_Black_Scholes.ipynb
# Run as a script or import functions from this module.

import numpy as np

np.random.seed(0)

S0 = 100
K = 100
T = 1
r = 0.05
sigma = 0.2
n = 100000

Z = np.random.standard_normal(n)
ST = S0 * np.exp((r - 0.5*sigma**2)*T + sigma*np.sqrt(T)*Z)
payoff = np.maximum(ST - K, 0)

option_price = np.exp(-r*T) * np.mean(payoff)
option_price

# display the computed price
print(option_price)

