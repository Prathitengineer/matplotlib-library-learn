import numpy as np
import matplotlib.pyplot as plt 
import random

heads_tails = [0,0]

for _ in range(50):
    heads_tails[random.randint(0,1)]+=1
    plt.bar(["Heads", "Tails"], heads_tails, color=['red', 'blue'])
    plt.pause(0.001)
plt.show()