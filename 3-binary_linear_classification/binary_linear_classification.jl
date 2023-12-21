using Plots

default(framestyle=:box,grid=false,legend=false)

m = -0.3
b = 5
linear_function(x) = m*x.+b

x=range(0,10,length=100)
y=linear_function.(x)

above_scatter_y = @. linear_function.(x)+abs(0.9*randn())
below_scatter_y = @. linear_function.(x)-abs(0.6*randn())

plot(x,above_scatter_y,seriestype=:scatter,markerstrokecolor=:auto)
plot!(x,below_scatter_y,seriestype=:scatter,markerstrokecolor=:auto)
plot!(x,y,linewidth=2,linecolor=:red)

savefig("3-binary_linear_classification\\jlbinary_linear_classification.png")
display(Plots.plot!())
wait()
exit()