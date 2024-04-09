import numpy as np
import matplotlib.pyplot as plt 

ax =plt.axes(projection="3d")

# x = np.random.random(100)
# y = np.random.random(100)
# z = np.random.random(100)
# ax.scatter(x,y,z)

# x = np.arange(1,50,0.1)
# y = np.sin(x)
# z = np.cos(x)
#ax.plot(x,y,z)

x = np.arange(0,50,0.1)
y = np.arange(0,50,0.1)
z = np.cos(x + y)

ax.plot(x,y,z)
ax.set_title("3D Plot")
ax.set_xlabel("test")

plt.show()