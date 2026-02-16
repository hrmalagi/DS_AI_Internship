import pandas as pd
import numpy as np

# Creating sample housing dataset
data = {
    "Price": [200000, 250000, 300000, 450000, 500000, 600000, 750000, 800000, 1200000, 1500000],
    "City": ["Delhi", "Mumbai", "Delhi", "Bangalore", "Mumbai", 
             "Delhi", "Bangalore", "Delhi", "Mumbai", "Bangalore"]
}

df = pd.DataFrame(data)

print(df.head())

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
sns.histplot(df["Price"], kde=True)

plt.title("Distribution of Housing Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

skewness = df["Price"].skew()
kurtosis = df["Price"].kurt()

print("Skewness:", skewness)
print("Kurtosis:", kurtosis)

plt.figure(figsize=(6,4))
sns.countplot(x="City", data=df)

plt.title("Count of Houses by City")
plt.show()
