import matplotlib.pyplot as pyplot
import numpy as np
import os
from datetime import datetime

m = -1
b = 3

x = np.linspace(0,10,100)
y = m*x+b

above_scatter_y = m*x+b+(abs(2*np.random.randn(100)))*x
below_scatter_y = m*x+b-(abs(2*np.random.randn(100)))*x

pyplot.scatter(x,above_scatter_y)
pyplot.scatter(x,below_scatter_y)
pyplot.plot(x,y,color='red')
if os.name=="nt":
    pyplot.savefig(f"plot{datetime.timestamp(datetime.now())}.png")
else:
    pyplot.savefig(f"plot{datetime.timestamp(datetime.now())}.png")
pyplot.show()
