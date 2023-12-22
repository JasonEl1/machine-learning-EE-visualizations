import os
import subprocess

outer_folder = os.getcwd()
inner_folders = [f.path for f in os.scandir(outer_folder) if f.is_dir()]

for folder in inner_folders:
    files = [f.name for f in os.scandir(folder) if f.is_file()]

    for filename in files:
        if filename.endswith(".py"):
            path = os.path.join(folder,filename)
            subprocess.run(['python',path])

print(f"Done running all python scripts in {outer_folder}")