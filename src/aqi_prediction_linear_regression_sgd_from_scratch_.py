# Auto-generated from: AQI Prediction (Linear Regression + SGD from Scratch).ipynb
# Run as a script or import functions from this module.

!pip install --quiet numpy pandas matplotlib
print("Installation done or Libraries already existed")

#importing libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#loading the data 
Data_path = r"C:\Users\lovey\OneDrive\Desktop\DataSets\air_quality_health_dataset.csv"

df = pd.read_csv(Data_path)
print("Data successfully loaded")
print("Shape",df.shape)
df.head(10)

# Checking for clean data 
print("Column names",df.columns)
print("\n Data type",df.dtypes)
print("\n Missing Columns",df.isna().sum())

# Selecting features and target values

y_raw = df["AQI"].values.reshape(-1,1) # Updated step

y_mean = y_raw.mean()       # Updated step
y_std = y_raw.std()         # Updated step

y = (y_raw - y_mean)/y_std   # Updated step

# Numeric features 
numeric_features = [
    'PM2.5','PM10','NO2','SO2','CO','O3',
    'temperature','humidity','wind_speed','precipitation',
    'hospital_visits','emergency_visits','mobility_index',
    'school_closures','public_transport_usage','mask_usage_rate',
    'lockdown_status','industrial_activity','vehicle_count',
    'construction_activity','respiratory_admissions',
    'population_density','green_cover_percentage'
]

X_num = df[numeric_features].values

# Categorical features
X_cat = df["region"].values

print("target values, numeric features and categorical features are set")

# Manual One Hot encoding

X_region = pd.get_dummies(X_cat, drop_first=True).values

print("Numeric Shape:", X_num.shape)
print("Region Shape:", X_region.shape)

# Combining features 

X = np.hstack([X_num,X_region])
print("final feature matrix shape : ",X.shape)

# Manual feature scaling(Standardization)

X_mean = X.mean(axis=0)
X_std = X.std(axis=0)

#prevent devide by zero
X_std[X_std == 0] = 1

X_scaled = (X - X_mean)/X_std

# Same job as StandardScaler but fully manual.
print("Standardization is done")

# Add Bias(Intercept Column)

m = X_scaled.shape[0]

X_design = np.c_[np.ones((m,1)),X_scaled]
print("Design matrix shape",X_design.shape)

#This creates x₀ = 1 for θ₀ (bias).

# Manual test-train split

np.random.seed(42)
indices = np.random.permutation(m)

train_size = int(0.8*m)

train_idx = indices[:train_size]
test_idx = indices[train_size:]

X_train = X_design[train_idx]
y_train = y[train_idx]

X_test = X_design[test_idx]
y_test = y[test_idx]

print("Train Shape",X_train.shape,y_train.shape)
print("\n Test Shape",X_test.shape,y_test.shape)

# Hypothesis function
def predict(X, theta):
    return X @ theta

# Mean Squared Error Loss
def compute_loss(X, y, theta):
    m = len(y)
    return (1/(2*m)) * np.sum((predict(X, theta) - y)**2)

# Stochastic Gradient Descent WITH GRADIENT CLIPPING
def stochastic_gradient_descent(X, y, lr=0.001, epochs=100, clip_value=0.5):
    m, n = X.shape
    theta = np.zeros((n, 1))
    loss_history = []

    for epoch in range(epochs):
        indices = np.random.permutation(m)

        for i in indices:
            xi = X[i].reshape(1, -1)
            yi = y[i]

            gradient = xi.T @ (xi @ theta - yi)

            # GRADIENT CLIPPING (this prevents explosion)
            gradient = np.clip(gradient, -clip_value, clip_value)

            theta = theta - lr * gradient

        loss = compute_loss(X, y, theta)
        loss_history.append(loss)

        if epoch % 10 == 0:
            print(f"Epoch {epoch}, Loss: {loss:.6f}")

    return theta, loss_history

# Train the model

theta_sgd, loss_history = stochastic_gradient_descent(
    X_train,y_train,
    lr = 0.001,
    epochs = 150,
    clip_value = 0.5
)

# Predicting on test data 
y_pred_scaled = predict(X_test,theta_sgd)

# Unscaling predictions back to real AQI

y_pred_real = y_pred_scaled * y_std + y_mean
y_test_real = y_test * y_std + y_mean

# Final evaluation metrics(Real AQI)

rmse = np.sqrt(np.mean((y_test_real - y_pred_real)**2))
mae = np.mean(np.abs(y_test - y_pred_real))

ss_total = np.sum((y_test_real - y_test_real.mean())**2)
ss_residual = np.sum((y_test_real - y_pred_real)**2)
r2 = 1-ss_residual/ss_total

print("SCRATCH SGD LINEAR REGRESSION RESULTS (REAL AQI)")
print("RMSE:", rmse)
print("MAE :", mae)
print("R²  :", r2)

# ✅ FINAL CLEAN METRICS (FORCE RECALCULATION)

# Ensure both are REAL AQI values
print("Sanity check:")
print("y_test_real min:", y_test_real.min())
print("y_test_real max:", y_test_real.max())
print("y_pred_real min:", y_pred_real.min())
print("y_pred_real max:", y_pred_real.max())

# RMSE
rmse_clean = np.sqrt(np.mean((y_test_real - y_pred_real)**2))

# MAE
mae_clean = np.mean(np.abs(y_test_real - y_pred_real))

# R²
ss_total = np.sum((y_test_real - y_test_real.mean())**2)
ss_residual = np.sum((y_test_real - y_pred_real)**2)
r2_clean = 1 - ss_residual / ss_total

print("\n✅ FINAL CLEAN SCRATCH METRICS")
print("RMSE:", rmse_clean)
print("MAE :", mae_clean)
print("R²  :", r2_clean)

# True Vs Predicted Plot 

plt.figure(figsize=(6,6))
plt.scatter(y_test_real,y_pred_real, alpha = 0.6)
plt.plot([y_test_real.min(),y_test_real.max()],
         [y_test_real.min(),y_test_real.max()],
         'r--')
plt.xlabel("True AQI")
plt.ylabel("Predicted AQI")
plt.title("AQI Prediction (Linear Regression + SGD from Scratch)")
plt.show()


