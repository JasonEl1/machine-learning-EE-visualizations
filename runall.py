import os
import subprocess

system_type = os.name
if system_type == "posix":
    python_name = "python3"
    pip_name = "pip3"
elif system_type == "nt":
    python_name = "python"
    pip_name = "pip"
else:
    exit()

outer_folder = os.getcwd()

subprocess.run([f"{pip_name}","install","-r",os.path.join(outer_folder,"requirements.txt")])

inner_folders = [f.path for f in os.scandir(outer_folder) if f.is_dir()]

for folder in inner_folders:
    files = [f.name for f in os.scandir(folder) if f.is_file()]

    for filename in files:
        if filename.endswith(".py"):
            path = os.path.join(folder,filename)
            subprocess.run([f"{python_name}",path])

print(f"Done running all python scripts in {outer_folder}")
