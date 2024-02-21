import matplotlib.pyplot as pyplot
import numpy as np
import os
from datetime import datetime

x1 = np.linspace(-2,0,100)
x2 = np.linspace(0,2,100)

y1 = [0]*len(x1)
y2 = [1]*len(x2)

pyplot.plot(x1,y1,color='b')
pyplot.plot(x2,y2,color='b')
pyplot.grid(True, alpha=0.3)
pyplot.xlim(-1.5,1.5)
pyplot.ylim(-1,2)
if os.name=="nt":
    pyplot.savefig(f"plot{datetime.timestamp(datetime.now())}.png")
else:
    pyplot.savefig(f"plot{datetime.timestamp(datetime.now())}.png")
pyplot.show()
