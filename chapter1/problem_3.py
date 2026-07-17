import os 

#specify the directory you want to list
directory_path ="/"

#list all files and directories in the specified path
contents = os.listdir(directory_path)

for item in contents:
    print(item)