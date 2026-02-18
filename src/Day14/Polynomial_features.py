import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

# Step 1: Create curved dataset
X = np.array([1, 2, 3, 4, 5]).reshape(-1,1)
y = np.array([1, 4, 9, 16, 25])  # y = x^2

# Step 2: Train Linear Regression on original data
model_linear = LinearRegression()
model_linear.fit(X, y)
y_pred_linear = model_linear.predict(X)
r2_linear = r2_score(y, y_pred_linear)

# Step 3: Create Polynomial Features (degree 2)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Step 4: Train Linear Regression on polynomial data
model_poly = LinearRegression()
model_poly.fit(X_poly, y)
y_pred_poly = model_poly.predict(X_poly)
r2_poly = r2_score(y, y_pred_poly)

# Step 5: Print R2 scores
print("R2 Score (Linear):", r2_linear)
print("R2 Score (Polynomial):", r2_poly)

# Step 6: Plot
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, y_pred_linear, color='red', label='Linear Fit')
plt.plot(X, y_pred_poly, color='green', label='Polynomial Fit')
plt.legend()
plt.title("Linear vs Polynomial Regression")
plt.show()