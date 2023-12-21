import matplotlib.pyplot as pyplot
import numpy as np

x = np.linspace(0,10,100)
y = np.sin(x)

pyplot.plot(x,y)
pyplot.savefig("0-simple_test\\pytestfig.png")
pyplot.show()