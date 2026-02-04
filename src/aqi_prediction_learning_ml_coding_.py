# Auto-generated from: AQI prediction(learning_ML coding).ipynb
# Run as a script or import functions from this module.

!pip install --quiet numpy pandas matplotlib seaborn scikit-learn
print("\n Installation done or package already present")

# Basic imports used throughout the notebook
import os
import numpy as np
import pandas as pd

# plotting
import matplotlib.pyplot as plt
import seaborn as sns

# scikit-learn utilities we'll use
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Use seaborn's styling
sns.set_style("whitegrid")
sns.set_context("notebook")

#opening the folder where the csv file is
folder = r"C:\Users\lovey\OneDrive\Desktop\DataSets"
os.listdir(folder)

print("Notebook imports done.")

# show where data is expected
DATA_PATH = r"C:\Users\lovey\OneDrive\Desktop\DataSets\air_quality_health_dataset.csv"
print("Data path set to:", DATA_PATH)

#load csv and show first 10 rows
DATA_PATH = r"C:\Users\lovey\OneDrive\Desktop\DataSets\air_quality_health_dataset.csv"

df = pd.read_csv(DATA_PATH)
print("loaded dataframe. Shape",df.shape)
display(df.head(10))

#inspecting the dataframe

print("Shape",df.shape)

print("\n column name")
print(list(df.columns))

print("\n Data Type: ")
print(df.dtypes)

print("\n Missing values per columns")
print(df.isna().sum().sort_values(ascending=False))

# Prepare x(features) and y(targets)

#Target
y = df["AQI"]

#List numeric features
numeric_features = ['PM2.5','PM10','NO2','SO2','CO','O3','temperature','humidity','wind_speed','precipitation','hospital_visits','emergency_visits','mobility_index','school_closures','public_transport_usage','mask_usage_rate','lockdown_status','industrial_activity','vehicle_count','construction_activity','respiratory_admissions','population_density','green_cover_percentage']

#Categorical features 
categorical_features = ['region']

#Build feature matrix 
x = df[numeric_features + categorical_features].copy()

x.head()

#test_train split cell 

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

print("Training set shape",x_train.shape)
print("Test set shape",x_test.shape)

# Build pipeline and fit model

# numeric_features and categorical_features should already exist from your earlier cell.
# They are lists of column names.

# 1) Define transformers:
# - 'num' will standardize numeric columns (zero mean, unit variance).
#   This helps many models and keeps feature scales comparable.
# - 'cat' will one-hot encode the 'region' categorical column. handle_unknown='ignore'
#   ensures the transformer won't break if a new region appears during prediction.
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
        ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical_features),
    ],
    remainder="drop"  # drop any columns not listed in transformers (none expected)
)

# 2) Create a pipeline that first preprocesses, then fits a LinearRegression model.
# Pipeline ensures the same preprocessing is applied to training and test (and new) data.
model_pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

# 3) Fit the pipeline to the training data.
# This runs the StandardScaler.fit_transform on numeric_features,
# OneHotEncoder.fit on categorical_features, then fits LinearRegression on resulting features.
model_pipeline.fit(x_train, y_train)

print("Pipeline fitted. You can now predict with model_pipeline.predict(X_new).")

# Predict and evaluate

#1) predict AQI for the test set
y_pred = model_pipeline.predict(x_test)

#2) Compute common regression metrics
mse = mean_squared_error(y_test,y_pred)    #mean square error
rmse = np.sqrt(mse)    #root mean square error(same units as AQI)
mae = mean_absolute_error(y_test,y_pred)  #absolute mean error(robust to outliers)
r2 = r2_score(y_test,y_pred)   #R^2(Explained variance)

# 3) Print results nicely
print(f"Evaluation on test set:")
print(f"  RMSE: {rmse:.4f}")
print(f"  MAE : {mae:.4f}")
print(f"  R^2 : {r2:.4f}")

# Cell C: Visualization of predictions vs true values

plt.figure(figsize=(6,6))
plt.scatter(y_test, y_pred, alpha=0.5)
# Plot diagonal line y=x for reference
min_val = min(y_test.min(), y_pred.min())
max_val = max(y_test.max(), y_pred.max())
plt.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=1)
plt.xlabel("True AQI")
plt.ylabel("Predicted AQI")
plt.title("True vs Predicted AQI")
plt.grid(True)
plt.show()

# Cell D: Extract and display model coefficients mapped to original feature names

import numpy as np
import pandas as pd

# 1) Get the fitted preprocessor and regressor from the pipeline
preproc = model_pipeline.named_steps["preprocessor"]
reg = model_pipeline.named_steps["regressor"]

# 2) Numeric feature names (order preserved as we defined earlier)
num_feats = numeric_features[:]  # copy to be safe

# 3) One-hot encoded categorical names
ohe_feature_names = []
# Access the fitted OneHotEncoder inside the ColumnTransformer
ohe = preproc.named_transformers_.get("cat", None)

if ohe is not None:
    # sklearn >= 1.0 provides get_feature_names_out
    if hasattr(ohe, "get_feature_names_out"):
        # this returns names like "region_<category>"
        ohe_feature_names = ohe.get_feature_names_out(categorical_features).tolist()
    else:
        # fallback for very old sklearn: derive names from categories_
        categories = ohe.categories_
        for col, cats in zip(categorical_features, categories):
            ohe_feature_names += [f"{col}__{c}" for c in cats]

# 4) Combined feature names in the order the regressor expects
feature_names = num_feats + ohe_feature_names

# 5) Get coefficients (matching the order above) and intercept
coefficients = reg.coef_
intercept = reg.intercept_

# 6) Build DataFrame to view coefficients with absolute magnitude sorting
coef_df = pd.DataFrame({
    "feature": feature_names,
    "coefficient": coefficients,
    "abs_coeff": np.abs(coefficients)
}).sort_values(by="abs_coeff", ascending=False).reset_index(drop=True)

# 7) Print intercept and show coefficient table
print("Intercept (bias):", intercept)
display(coef_df.head(50))  # show top 50 (or fewer) features by absolute coefficient

import joblib

model_file = r"C:\Users\lovey\OneDrive\Desktop\DataSets\aqi_model_pipeline.joblib"

joblib.dump(model_pipeline, model_file)

print("Saved model pipeline to:", model_file)


