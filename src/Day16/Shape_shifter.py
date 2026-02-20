import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)

# Normal Distribution (Heights)
heights = np.random.normal(170, 10, 500)

# Right Skewed (Income)
income = np.random.exponential(50000, 500)

# Left Skewed (Easy Exam Scores)
scores = 100 - np.random.exponential(10, 500)

df = pd.DataFrame({
    "Heights": heights,
    "Income": income,
    "Scores": scores
})

# Plot Histograms
for column in df.columns:
    sns.histplot(df[column], kde=True)
    plt.title(column)
    plt.show()
    
    print(column)
    print("Mean:", df[column].mean())
    print("Median:", df[column].median())
    print("--------------------")