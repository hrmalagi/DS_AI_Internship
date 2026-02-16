import pandas as pd

data = {
    "SquareFootage": [800, 1000, 1200, 1500, 1800, 2000, 2500, 3000, 3500, 4000],
    "Price": [200000, 250000, 280000, 350000, 400000, 450000, 600000, 700000, 850000, 950000],
    "City": ["Delhi", "Mumbai", "Delhi", "Bangalore", "Mumbai",
             "Delhi", "Bangalore", "Delhi", "Mumbai", "Bangalore"]
}

df = pd.DataFrame(data)
print(df.head())

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
sns.scatterplot(x="SquareFootage", y="Price", data=df)

plt.title("Square Footage vs Price")
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.show()

plt.figure(figsize=(7,5))
sns.boxplot(x="City", y="Price", data=df)

plt.title("Price Distribution by City")
plt.show()

print("As SquareFootage increases, Price also seems to increase. This indicates a positive relationship between house size and price.")