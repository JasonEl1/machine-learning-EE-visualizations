using Plots

default(framestyle=:box,legend=false,linecolor=:blue)

x1 = range(-2,0,length=100)
x2 = range(0,2,length=100)

y1 = fill(0,length(x1))
y2 = fill(1,length(x2))

plot(x1,y1,ylims=(-1,2),xlims=(-1.5,1.5))
plot!(x2,y2)

xticks!(-2:0.5:2)
yticks!(-1:0.5:2)

savefig("4-perceptron_activation_function\\jlperceptron_activation_function.png")
display(Plots.plot!())
wait()
exit()