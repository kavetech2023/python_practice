import os

path = "C:\\Users\\kavet\\OneDrive\\Desktop\\text.txt"

if os.path.exists(path):     # 1) Check if file path actually exists.
    print("That Location Exists")
    if os.path.isfile(path): # 2) Check if the path is a file.
        print("That is a file")
    elif os.path.isdir(path):# 3) Check to see if it is a Directory.
        print(("That is a directory!"))    
else:
    print("That location doesn't exist!")    