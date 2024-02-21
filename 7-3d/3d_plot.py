# #import matplotlib.pyplot as pyplot
# from mpl_toolkits import mplot3d
# import os
# from datetime import datetime


# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib.tri import Triangulation

# def f(x, y):
#     #return np.sin(np.sqrt(x ** 2 + y ** 2))
#     return np.sin(x**2) + np.cos(y**2)
#     #return np.sin((y**2) + x)

# x = np.linspace(-6, 6, 30)
# y = np.linspace(-6, 6, 30)
# X, Y = np.meshgrid(x, y)
# Z = f(X, Y)

# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111, projection='3d')

# ax.plot_surface(X,Y,Z, cmap='viridis', edgecolor='none', alpha=1.0,rstride=1,cstride=1,linewidth=0)
# plt.margins(x=0.1,y=0.1)
# plt.show()
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from datetime import datetime

## to maximize rendering speed, we want the parameters rstride and cstride
## to be multiples of the number of rows-1 and columns-1
r=np.linspace(0,1,101)
theta=np.linspace(0,2*np.pi,10001)
R,Theta=np.meshgrid(r,theta)
X,Y=R*np.cos(Theta),R*np.sin(Theta)
Z=R*np.sin(Theta)*np.cos(Theta)

fig=plt.figure(1)
ax=fig.add_subplot(projection='3d')
ax.plot_surface(X,Y,Z,rstride=5,cstride=5,cmap='viridis',linewidth=0)
plt.savefig(f"plot{datetime.timestamp(datetime.now())}.png")
plt.show()
