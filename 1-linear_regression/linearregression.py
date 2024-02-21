import matplotlib.pyplot as pyplot
import numpy as np
import os
from datetime import datetime

noise = 3*np.random.randn(50)
m = 2
b = 3

x = np.linspace(0,10,50)
y = m*x+b+noise

pyplot.scatter(x,y)
pyplot.plot(x,m*x+b,linewidth=2,color='red')
pyplot.margins(x=0.1,y=0.1)
if os.name=="nt":
    pyplot.savefig(f"plot{datetime.timestamp(datetime.now())}.png")
else:
    pyplot.savefig(f"plot{datetime.timestamp(datetime.now())}.png")
pyplot.show()
