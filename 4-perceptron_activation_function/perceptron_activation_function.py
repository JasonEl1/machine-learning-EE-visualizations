import matplotlib.pyplot as pyplot
import numpy as np

x1 = np.linspace(-2,0,100)
x2 = np.linspace(0,2,100)

y1 = [0]*len(x1)
y2 = [1]*len(x2)

pyplot.plot(x1,y1,color='b')
pyplot.plot(x2,y2,color='b')
pyplot.grid(True, alpha=0.3)
pyplot.xlim(-1.5,1.5)
pyplot.ylim(-1,2)

pyplot.savefig("4-perceptron_activation_function\\pyperceptron_activation_function.png")
pyplot.show()