"""Statistical power curve simulation."""
import numpy as np
from scipy.stats import ttest_1samp


def compute_power(effect_sizes=None, n_sim=500, n=30, alpha=0.05):
    if effect_sizes is None:
        effect_sizes = np.linspace(0, 1, 20)
    power = []
    np.random.seed(0)
    for effect in effect_sizes:
        rejections = 0
        for _ in range(n_sim):
            sample = np.random.normal(effect, 1, n)
            _, p = ttest_1samp(sample, 0)
            if p < alpha:
                rejections += 1
        power.append(rejections / n_sim)
    return effect_sizes, np.array(power)


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    effects, power = compute_power()
    plt.plot(effects, power)
    plt.title("Statistical Power Curve")
    plt.xlabel("Effect Size")
    plt.ylabel("Power")
    plt.show()
