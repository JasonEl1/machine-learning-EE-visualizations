using Plots

x = range(0, 10, length=100)
y = sin.(x)
plot(x, y)

#gui()~
savefig("jltestfig.png")