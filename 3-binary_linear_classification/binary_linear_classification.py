import matplotlib.pyplot as pyplot
import numpy as np

m = -0.3
b = 5

x = np.linspace(0,10,100)
y = m*x+b

above_scatter_y = m*x+b+(abs(0.8*np.random.randn(100)))
below_scatter_y = m*x+b-(abs(0.5*np.random.randn(100)))

pyplot.scatter(x,above_scatter_y)
pyplot.scatter(x,below_scatter_y)
pyplot.plot(x,y,color='red')

pyplot.savefig("3-binary_linear_classification\\pybinary_linear_classification.png")
pyplot.show()