import matplotlib.pyplot as plt

ages=[18,20,22,22,25,27,30,35,40,45,50]
plt.figure(figsize=(10,5))
plt.hist(ages,bins=5)
plt.title('Age Distribution')
plt.grid()
plt.show()