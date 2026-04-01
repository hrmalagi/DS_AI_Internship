import numpy as np
import pandas as pd
import time

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

# 🔹 Step 1: Generate Dataset
X, y = make_classification(
    n_samples=1000,
    n_features=20,
    weights=[0.9, 0.1],   # imbalance
    random_state=42
)

# 🔹 Step 2: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 🔹 Step 3: Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 🔹 Step 4: Baseline Model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\n🔹 Baseline Results")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))

# 🔹 Step 5: Grid Search (Accuracy)
param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 10, 20],
    "min_samples_split": [2, 5, 10]
}

grid_acc = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    scoring="accuracy",
    cv=3
)

grid_acc.fit(X_train, y_train)

print("\n🔹 Best Parameters (Accuracy):", grid_acc.best_params_)

# 🔹 Step 6: Grid Search (F1)
grid_f1 = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    scoring="f1",
    cv=3
)

grid_f1.fit(X_train, y_train)

print("\n🔹 Best Parameters (F1):", grid_f1.best_params_)

# 🔹 Step 7: Time Comparison
start = time.time()
grid_acc.fit(X_train, y_train)
grid_time = time.time() - start

start = time.time()
rand_search = RandomizedSearchCV(
    RandomForestClassifier(random_state=42),
    param_distributions=param_grid,
    n_iter=10,
    scoring="f1",
    cv=3,
    random_state=42
)
rand_search.fit(X_train, y_train)
rand_time = time.time() - start

print("\n🔹 Time Comparison")
print("GridSearch Time:", round(grid_time, 2), "seconds")
print("RandomizedSearch Time:", round(rand_time, 2), "seconds")

# 🔹 Step 8: Best F1 Score
best_model = rand_search.best_estimator_
y_pred_best = best_model.predict(X_test)

print("\n🔹 Best Model F1 Score:", f1_score(y_test, y_pred_best))