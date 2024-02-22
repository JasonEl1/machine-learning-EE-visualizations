import matplotlib.pyplot as pyplot
import numpy as np
import os
from datetime import datetime

x = np.linspace(0,10,100)
linear_y = 0.3*x+1.5
polynomial_y = -0.1*pow((x-6),2)+4
polynomial_y_noise = polynomial_y + 0.3*(np.random.randn(100))

pyplot.plot(x,linear_y,color='r', label='linear regression')
pyplot.plot(x,polynomial_y,color='b', label='polynomial regression')
pyplot.legend()
pyplot.scatter(x,polynomial_y_noise)
pyplot.savefig(f"plot{datetime.timestamp(datetime.now())}.png")
pyplot.show()
