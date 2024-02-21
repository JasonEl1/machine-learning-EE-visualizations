import matplotlib.pyplot as pyplot
import numpy as np
import os
from datetime import datetime



x = np.linspace(-10,10,100)
y = np.maximum(0,x)

pyplot.plot(x,y)
pyplot.title("ReLU Activation Function")
pyplot.savefig(f"plot{datetime.timestamp(datetime.now())}.png")
pyplot.show()
