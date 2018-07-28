import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

x = np.arange(-3, 3, 0.25)
y = np.arange(-3, 3, 0.25)
X, Y = np.meshgrid(x, y)
Z = 6*X*X + 4*X*Y + 3*Y*Y

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_wireframe(X,Y,Z) 

plt.show()
