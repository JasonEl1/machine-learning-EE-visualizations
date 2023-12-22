using Plots

default(framestyle=:box,legend=false,grid=false,linecolor=:blue)

x = range(0,10,length=100)
linear_function(x) = 0.3*x+1.5
polynomial_function(x) = -0.1*(x-6)^2+4

linear_y = linear_function.(x)
polynomial_y = polynomial_function.(x)
polynomial_y_noise = @. polynomial_function.(x).+ 0.3*randn()

plot(x,linear_y,linecolor="blue",linewidth=2)
plot!(x,polynomial_y,linecolor="red",linewidth=2)
plot!(x,polynomial_y_noise,seriestype=:scatter,ylims=(0,5),color=:blue)

savefig("5-polynomial_and_linear_regression\\jlpolynomial_and_linear_regression.png")

display(Plots.plot!())
wait()
exit(0)