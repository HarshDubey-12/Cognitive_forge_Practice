# Auto-generated from: 06_Multicollinearity_Variance_Inflation.ipynb
# Run as a script or import functions from this module.

import numpy as np
import statsmodels.api as sm

np.random.seed(0)

X1 = np.random.normal(0,1,100)
X2 = X1 + np.random.normal(0,0.01,100)
y = 3*X1 + 2*X2 + np.random.normal(0,1,100)

X = sm.add_constant(np.column_stack((X1,X2)))
model = sm.OLS(y,X).fit()

model.summary()

print(model.summary())

