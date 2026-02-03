"""Multicollinearity demonstration using statsmodels OLS."""
import numpy as np
import statsmodels.api as sm


def run_multicollinearity(seed=0):
    np.random.seed(seed)
    X1 = np.random.normal(0, 1, 100)
    X2 = X1 + np.random.normal(0, 0.01, 100)
    y = 3 * X1 + 2 * X2 + np.random.normal(0, 1, 100)
    X = sm.add_constant(np.column_stack((X1, X2)))
    model = sm.OLS(y, X).fit()
    return model


if __name__ == "__main__":
    model = run_multicollinearity()
    print(model.summary())
