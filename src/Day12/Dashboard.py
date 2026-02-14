import matplotlib.pyplot as plt

categories= ['Electronics','Clothing','Home']
values= [300,450,200]

plt.subplot(1,2,1)
plt.bar(categories,values)
plt.title("Bar graph of Categories and Values")
plt.xlabel('Categories')
plt.ylabel('Values')

plt.subplot(1,2,2)
plt.plot(categories,values)
plt.title("Line graph of Categories and Values")
plt.xlabel('Categories')
plt.ylabel('Values')

plt.tight_layout()
plt.show()