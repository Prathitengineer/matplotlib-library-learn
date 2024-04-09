import numpy as np
import matplotlib.pyplot as plt

x_data = np.random.random(1000) *100
y_data = np.random.random(1000) *100

print(y_data)

plt.scatter(x_data, y_data, c= "red",marker = "*",alpha=0.3)
plt.show()