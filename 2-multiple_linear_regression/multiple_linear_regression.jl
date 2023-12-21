using Plots

default(framestyle=:box,grid=false,legend=false)

function create_plot_and_noise(m,b,noise)
    linear_function(x) = m*x.+b

    x=range(0,10,length=100)
    y=linear_function.(x)
    y_noisy=@. linear_function.(x)+noise*randn()

    plot!(x,y,xlims=(minimum(x)-1,maximum(x)+1),linewidth=2)
    plot!(x,y_noisy,seriestype=:scatter,markerstrokecolor=:auto)
end

create_plot_and_noise(0.3,5,0.3)
create_plot_and_noise(0.15,7,0.4)
create_plot_and_noise(0.1,6,0.3)

savefig("2-multiple_linear_regression\\jlmultiple_linearregression.png")
display(Plots.plot!())
wait()
exit()create_plot_and_noise(0.15,7,0.4)
