# Auto-generated from: 07_Markov_Chain_Stationary_Distribution.ipynb
# Run as a script or import functions from this module.

import numpy as np

P = np.array([[0.9,0.1],
              [0.4,0.6]])

state = 0
counts = [0,0]

for _ in range(100000):
    state = np.random.choice([0,1], p=P[state])
    counts[state]+=1

np.array(counts)/sum(counts)

print(np.array(counts)/sum(counts))

