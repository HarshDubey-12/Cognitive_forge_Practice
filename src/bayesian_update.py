"""Bayesian sequential updating for a Bernoulli likelihood (Beta prior)."""
import numpy as np
from scipy.stats import beta


def sequential_update(data, a0=1, b0=1):
    a, b = a0, b0
    for obs in data:
        if obs == 1:
            a += 1
        else:
            b += 1
    return a, b


if __name__ == "__main__":
    np.random.seed(0)
    true_p = 0.7
    data = np.random.binomial(1, true_p, 50)
    a, b = sequential_update(data)
    x = np.linspace(0, 1, 1000)
    import matplotlib.pyplot as plt

    plt.plot(x, beta.pdf(x, a, b))
    plt.title("Final Posterior after Sequential Updating")
    plt.show()
