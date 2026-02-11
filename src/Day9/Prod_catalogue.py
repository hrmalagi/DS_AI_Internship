import pandas as pd

Products= pd.Series([700,150,300],index=['Laptop','Mouse','Keyboard'])
print("Products:\n",Products)
print("\nPrice for Laptop:",Products['Laptop'])
print("\nFirst two products:\n", Products.iloc[[0,1]])