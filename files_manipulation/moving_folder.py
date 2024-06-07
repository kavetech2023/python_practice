import os

source = "folder_moved"
destination = "C:\\Users\\kavet\\OneDrive\\Desktop\\folder_moved"

try:
    if os.path.exists(destination):
        print("There is already a folder there")
    else:
        os.replace(source,destination)
        print(source+ " was moved")
except FileNotFoundError:
    print(source+ "was not found")