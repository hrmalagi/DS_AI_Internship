import numpy as np
import pandas as pd

np.random.seed(42)

income = np.random.exponential(50000, 500)

df = pd.DataFrame({
    "Income": income
})

# Using Income column
mean = df["Income"].mean()
std = df["Income"].std()

df["z_score"] = (df["Income"] - mean) / std

outliers = df[abs(df["z_score"]) > 3]

print("Mean:", mean)
print("Standard Deviation:", std)
print("Outliers:")
print(outliers)