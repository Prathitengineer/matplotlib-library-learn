import numpy as np
import matplotlib.pyplot as plt 

ax =plt.axes(projection="3d")

x =np.arange(-5, 5, 0.1)
y =np.arange(-5, 5, 0.1)

a,b = np.meshgrid(x,y)

z = np.sin(a) + np.cos(b)

ax.plot_surface(a,b,z, cmap="Spectral") 
ax.set_title("3D Plot")
ax.set_xlabel("test")
ax.view_init(azim=0,elev = 90)

plt.show()