import pandas as pd

data={"Items":['Laptop','Hard-Disk','Mouse','Keyboard'],
      "Price":['$700','$100','$30','$50'],
       "Date":["2024-01-5","2024-01-10","2024-01-15","2024-01-20"]}
                                                                 
df=pd.DataFrame(data)
print("Data Types:\n",df.dtypes)
df["Price"]= df["Price"].str.replace('$','').astype(float)
df["Date"]= pd.to_datetime(df["Date"])
print("\nCorrected Price and Date:\n",df["Price"],df["Date"])