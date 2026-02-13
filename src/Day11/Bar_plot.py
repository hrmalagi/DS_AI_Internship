#Two Year Comparison
import numpy as np
import matplotlib.pyplot as plt

products= ['A','B','C','D']
sales_2024= [40,60,30,50]
sales_2025= [50,70,45,65]
plt.figure(figsize=(8,5))
x=np.arange(len(products))       #creates positions for bars
width=0.5                        #width for bars

plt.bar(x-width/2,sales_2024,width,color='Blue',label=sales_2024)    #0.5 width is divided among two bars (0.25-2024)
plt.bar(x+width/2,sales_2025,width,color='Red',label=sales_2025)     #0.5 width is divided among two bars (0.25-2025)

plt.xticks(x,products)         #relaces positions(1,2,3,4) with product names

plt.title("Two Year Sales Comparisson")
plt.xlabel('Products')
plt.ylabel('Sales')
plt.legend()
plt.grid(axis='y')
plt.show()