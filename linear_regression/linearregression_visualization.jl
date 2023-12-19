using Plots

m = 0.3
b = 5
linear_function(x) = m*x.+b

x=range(0,10,length=100)
#x=0:0.1:10
y=linear_function.(x)
y_noisy=@. linear_function.(x)+0.3*randn()

plot(x,y,xlims=(minimum(x)-1,maximum(x)+1),linewidth=2)
plot!(x,y_noisy,seriestype=:scatter,markerstrokecolor=:auto)
savefig("linear_regression\\jllinearregression.png")
display(Plots.plot!())
wait()
error()
exit()