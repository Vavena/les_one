import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math

def func(x,y):
    return (x - 1) ** 2 - (y + 2) ** 2
    #return(1/4*math.sin(1/2*x**2-y)-math.e**(-(x-5)**2+(y-2)**2))

x = np.linspace(2,8,6)
y = np.linspace(0,5,5)
X, Y = np.meshgrid(x,y)
Z = func(X,Y)
fig, ax = plt.subplots(1, 1, figsize=(6, 5))
obj = ax.imshow(Z, cmap=plt.cm.seismic, vmin=-400, vmax=400)
fig.colorbar(obj, vmin=-400, vmax=400)

