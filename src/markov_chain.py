"""Markov chain simulation to estimate stationary distribution."""
import numpy as np


def simulate_markov(P=None, steps=100000, seed=0):
    if P is None:
        P = np.array([[0.9, 0.1], [0.4, 0.6]])
    np.random.seed(seed)
    state = 0
    counts = [0, 0]
    for _ in range(steps):
        state = np.random.choice([0, 1], p=P[state])
        counts[state] += 1
    return np.array(counts) / sum(counts)


if __name__ == "__main__":
    dist = simulate_markov()
    print("Estimated stationary distribution:", dist)
