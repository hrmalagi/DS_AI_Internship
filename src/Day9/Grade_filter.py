import pandas as pd

Grades= pd.Series([85,None,92,45,None,78,55])
print("Original Series:\n",Grades)
Missing= Grades.isnull()
print("\nMissing Values:\n",Missing)
Filled=Grades.fillna(0)
print("\nFilled Series:\n",Filled)
filter= Grades[Grades>60]
print("\nFiltered Series:\n",filter)