import pandas as pd

df= pd.read_csv("src/Day10/customer_orders.csv")
print("Shape Before:",df.shape)
print("\nMissing Values in each column:\n",df.isnull().sum())
df['Amount'].fillna(df["Amount"].median())
df['City'].fillna(df["City"].mode()[0])
print("\nDuplicated:",df.duplicated().sum())
df.drop_duplicates(inplace=True)
print("\n\nShape after cleaning:",df.shape)
print("\nFilled values:\n",df)