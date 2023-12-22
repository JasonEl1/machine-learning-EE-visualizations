# outer_folder = pwd()
# inner_folders = filter(isdir,readdir(outer_folder))

# for folder in inner_folders
#     files = readdir(joinpath(outer_folder,folder))
    
#     for filename in files
#         if endswith(filename,".jl")
#             path = joinpath(outer_folder,folder,filename)
#             println("Running $path")
#             run(`julia $path`)
#         end
#     end
# end

# println("Done running all julia scripts in $outer_folder")