import matplotlib.pyplot as pyplot
import numpy as np
import os
from datetime import datetime
import math

x = np.linspace(-10,10,100)
y = 1 / (1 + (math.e ** -x))

pyplot.plot(x,y)
pyplot.title("Sigmoid Activation Function")
pyplot.savefig(f"plot{datetime.timestamp(datetime.now())}.png")
pyplot.show()
