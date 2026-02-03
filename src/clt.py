"""Central Limit Theorem example
Run as a script or import `run_clt`.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def run_clt(n=40, trials=10000, scale=2):
    np.random.seed(0)
    sample_means = np.array([
        np.mean(np.random.exponential(scale=scale, size=n)) for _ in range(trials)
    ])
    mu = scale
    sigma = scale
    theoretical_std = sigma / np.sqrt(n)
    return sample_means, mu, theoretical_std


if __name__ == "__main__":
    sample_means, mu, theoretical_std = run_clt()
    x = np.linspace(min(sample_means), max(sample_means), 1000)
    plt.hist(sample_means, bins=50, density=True, alpha=0.6)
    plt.plot(x, norm.pdf(x, mu, theoretical_std), "r")
    plt.title("CLT with Theoretical Normal Overlay")
    plt.show()
