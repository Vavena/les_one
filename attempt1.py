import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math


plt.figure(figsize=(8,3))
plt.grid(lw=0.5, ls='--')
x = np.linspace(-10,10,1000)
y = (np.sin(2*x)**2)*np.exp((x+2)/10)**2
plt.plot(x,y, lw = 4.0,color='red')
plt.plot(x,y, lw = 5.0, color='black', zorder=0)
plt.plot(x, y)
plt.show()