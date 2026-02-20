import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)

# Step 1: Create heavily skewed dataset (Income)
income = np.random.exponential(50000, 10000)

# Step 2: Store sample means
sample_means = []

# Step 3: Run 1000 simulations
for i in range(1000):
    sample = np.random.choice(income, 30)
    sample_mean = np.mean(sample)
    sample_means.append(sample_mean)

# Step 4: Plot distribution of sample means
sns.histplot(sample_means, kde=True)
plt.title("Distribution of Sample Means")
plt.show()