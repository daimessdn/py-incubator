import numpy as np

import matplotlib.pyplot as plt

def f(x):
	return np.sin(x)

x = np.arange(0, 10, 0.1)
y = f(x)

plt.plot(x,y)
plt.show()