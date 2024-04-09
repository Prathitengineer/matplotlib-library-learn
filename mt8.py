import numpy as np
import matplotlib.pyplot as plt

stock_a = np.array([100, 102, 99, 101, 101, 100,102])
stock_b = np.array([98 ,95, 102, 104, 105, 103, 109])
stock_c = np.array([100, 115, 100, 105, 100, 98, 95])

plt.plot(stock_a,label = "company1")
plt.plot(stock_b,label = "company2")
plt.plot(stock_c,label = "company3")

plt.legend(loc="lower center")

plt.show()
