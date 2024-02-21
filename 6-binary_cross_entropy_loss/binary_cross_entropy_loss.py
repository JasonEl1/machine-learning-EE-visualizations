import matplotlib.pyplot as pyplot
import numpy as np
import os
from datetime import datetime
import math

x = np.linspace(0,1,100)
left_y = -(np.log(x))
right_y = -(np.log(1-x))

pyplot.plot(x,left_y,color='r')
pyplot.plot(x,right_y,color='b')


pyplot.savefig(f"plot{datetime.timestamp(datetime.now())}.png")
pyplot.show()
