# Auto-generated from: Matplotlib_Generic_graphs.ipynb
# Run as a script or import functions from this module.

import matplotlib.pyplot as plt
import seaborn as sn

x_lable = []
y_lable = []

n = int(input("Enter the limiter: "))

for i in range(-n,n):
    x_lable.append(i)
    y_lable.append(i**2)

plt.figure()
plt.plot(x_lable,y_lable)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Quadratic curve")
plt.grid(True)
plt.show()


