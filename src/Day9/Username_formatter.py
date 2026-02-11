import pandas as pd

Usernames= pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
white= Usernames.str.strip()
print("Whitespace removed:\n",white,end=" ")
low= Usernames.str.lower()
print("\nCleaned Series:\n",low, end=" ")
present= low.str.contains('a')
print("\nResult of a search:\n",present, end=" ")