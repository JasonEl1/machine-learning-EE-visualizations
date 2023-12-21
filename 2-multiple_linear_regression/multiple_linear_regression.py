import matplotlib.pyplot as pyplot
import numpy as np

def create_plot_and_noise(m,b,noise_coeff):
    noise = noise_coeff*np.random.randn(100)
    global x
    x = np.linspace(0,10,100)
    global y
    y=m*x+b+noise

    pyplot.scatter(x,y)
    pyplot.plot(x,m*x+b,linewidth=2,color='red')

create_plot_and_noise(0.3,5,0.3)
create_plot_and_noise(0.15,7,0.4)
create_plot_and_noise(0.1,6,0.3)

pyplot.margins(x=0.1,y=0.1)
pyplot.savefig("2-multiple_linear_regression\\pymultiple_linearregression.png")
pyplot.show()