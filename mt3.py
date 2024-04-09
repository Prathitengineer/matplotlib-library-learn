import numpy as np
import matplotlib.pyplot as plt

x = ["c++", "c#", "Python","java", "Go"]
y = [20,50,140,1,45]

# plt.plot(years, waights, linestyle="--",lw=3)
# plt.bar(x, y)
plt.bar(x, y, color="r",align="edge",width=0.1, edgecolor="green",lw=6)
plt.show()