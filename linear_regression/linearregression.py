import matplotlib.pyplot as pyplot
import numpy as np

noise = 0.3*np.random.randn(100)
m = 0.3
b = 5

x = np.linspace(0,10,100)
y = m*x+b+noise

pyplot.scatter(x,y)
pyplot.plot(x,m*x+b,linewidth=2,color='red')
pyplot.margins(x=0.1,y=0.1)
pyplot.savefig("linear_regression\pylinearregression.png")
pyplot.show()