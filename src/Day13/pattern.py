import pandas as pd

data = {
    "SquareFootage": [800, 1000, 1200, 1500, 1800, 2000, 2500, 3000, 3500, 4000],
    "Bedrooms": [1, 2, 2, 3, 3, 3, 4, 4, 5, 5],
    "Price": [200000, 250000, 280000, 350000, 400000, 450000, 600000, 700000, 850000, 950000]
}

df = pd.DataFrame(data)
print(df.head())

correlation_matrix = df.corr()
print(correlation_matrix)

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(6,5))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")

plt.title("Correlation Matrix Heatmap")
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(y=df["Price"])

plt.title("Boxplot of Price")
plt.show()