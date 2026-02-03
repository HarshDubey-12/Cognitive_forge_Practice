"""Monte Carlo Option Pricing (Black–Scholes)"""
import numpy as np


def price_option_mc(S0=100, K=100, T=1.0, r=0.05, sigma=0.2, n=100000, seed=0):
    np.random.seed(seed)
    Z = np.random.standard_normal(n)
    ST = S0 * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * Z)
    payoff = np.maximum(ST - K, 0)
    option_price = np.exp(-r * T) * np.mean(payoff)
    return option_price


if __name__ == "__main__":
    price = price_option_mc()
    print("Estimated European call price:", price)
