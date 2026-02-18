import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Step 1: Create dataset
data = {
    "Age": [25, 30, 35, 40, 45],
    "Salary": [25000, 40000, 60000, 80000, 90000]
}

df = pd.DataFrame(data)
print("Original Data:")
print(df)

# Step 2: Standardization
scaler_standard = StandardScaler()
df_standardized = pd.DataFrame(
    scaler_standard.fit_transform(df),
    columns=df.columns
)

print("\nStandardized Data:")
print(df_standardized)

# Step 3: Normalization
scaler_minmax = MinMaxScaler()
df_normalized = pd.DataFrame(
    scaler_minmax.fit_transform(df),
    columns=df.columns
)

print("\nNormalized Data:")
print(df_normalized)

# Step 4: Plot histogram before and after scaling
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.hist(df["Salary"], bins=5)
plt.title("Original Salary")

plt.subplot(1,2,2)
plt.hist(df_standardized["Salary"], bins=5)
plt.title("Standardized Salary")

plt.tight_layout()
plt.show()