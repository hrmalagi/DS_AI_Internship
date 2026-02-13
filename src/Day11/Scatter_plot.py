#Two Scatter Plots in One Graph
import matplotlib.pyplot as plt

hours= [1,2,3,4,5]
marks_2024= [40,50,60,70,80]
marks_2025= [35,48,55,65,76]
plt.scatter(hours,marks_2024,color="Blue",label=marks_2024)
plt.scatter(hours,marks_2025,color="Red",label=marks_2025)
plt.xlabel("Hours ->")
plt.ylabel("Marks ->")
plt.grid()
plt.legend()
plt.show()