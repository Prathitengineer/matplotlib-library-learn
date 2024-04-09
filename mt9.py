import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import style

style.use("ggplot")
# style.use("dark_background")

votes = np.array([10, 2, 5, 16, 22])
people = np.array(["A", "B", "C", "D", "E"])

plt.pie(votes, labels=None)
plt.legend(people)

plt.show()