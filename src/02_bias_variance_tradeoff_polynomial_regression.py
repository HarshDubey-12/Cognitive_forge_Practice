# Auto-generated from: 02_Bias_Variance_Tradeoff_Polynomial_Regression.ipynb
# Run as a script or import functions from this module.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

np.random.seed(0)
X = np.linspace(0,1,100).reshape(-1,1)
y_true = np.sin(2*np.pi*X)
y = y_true + np.random.normal(0,0.3,(100,1))

models = []
degrees = [1,3,9]

for d in degrees:
    poly = PolynomialFeatures(d)
    X_poly = poly.fit_transform(X)
    model = LinearRegression().fit(X_poly, y)
    models.append((d, model, poly))

plt.scatter(X,y,s=10)
for d,model,poly in models:
    plt.plot(X, model.predict(poly.transform(X)), label=f"deg={d}")
plt.legend()
plt.title("Bias-Variance Tradeoff")
plt.show()

