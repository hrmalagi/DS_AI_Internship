import pandas as pd

data={"Location":["Chicago","New York","new york","NEW YORK"]}
df=pd.DataFrame(data)
print("Before Cleaning:\n",df)
df["Location"]= df["Location"].str.strip().str.title()
print("\nAfter Cleaning:\n",df["Location"])
print("\nUnique Cities:",df["Location"].unique())