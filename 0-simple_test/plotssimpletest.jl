using Plots

#x = range(0, 10, length=100)
f(x) = sin.(x)
plot(f,0,10)

savefig("0-simple_test\\jltestfig.png")
display(Plots.plot!())
sleep(10)