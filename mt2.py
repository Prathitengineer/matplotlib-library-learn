import numpy as np
import matplotlib.pyplot as plt

years = [2006 + x for x in range(16)]

waights = [80, 83, 84, 85, 86, 82, 81, 79, 83, 80,
           82, 82, 83, 81, 80, 79]

# plt.plot(years, waights, linestyle="--",lw=3)
plt.plot(years, waights, "r--", lw = 3)
plt.show()