import matplotlib.pyplot as pyplot
import numpy as np
import os
from datetime import datetime

x = np.linspace(0,10,100)
y = np.sin(x)

pyplot.plot(x,y)
if os.name=="nt":
    pyplot.savefig(f"plot{datetime.timestamp(datetime.now())}.png")
else:
    pyplot.savefig(f"plot{datetime.timestamp(datetime.now())}.png")
pyplot.show()
