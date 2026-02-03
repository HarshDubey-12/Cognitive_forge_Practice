"""Sampling distribution of the Pearson correlation coefficient."""
import numpy as np


def sample_correlations(n_rep=5000, sample_size=30, rho=0.6, seed=0):
    np.random.seed(seed)
    correlations = []
    for _ in range(n_rep):
        x = np.random.normal(0, 1, sample_size)
        y = rho * x + np.random.normal(0, 1, sample_size)
        correlations.append(np.corrcoef(x, y)[0, 1])
    return np.array(correlations)


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    corrs = sample_correlations()
    plt.hist(corrs, bins=50, density=True)
    plt.title("Sampling Distribution of Correlation")
    plt.show()
