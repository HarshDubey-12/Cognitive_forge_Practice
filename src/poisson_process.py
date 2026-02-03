"""Poisson process simulation (interarrival times)."""
import numpy as np


def simulate_poisson(rate=3, n=1000, seed=0):
    np.random.seed(seed)
    inter_arrivals = np.random.exponential(1 / rate, n)
    arrival_times = np.cumsum(inter_arrivals)
    return arrival_times


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    arrival_times = simulate_poisson()
    plt.step(arrival_times, range(len(arrival_times)))
    plt.title("Poisson Process Simulation")
    plt.show()
