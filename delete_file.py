import os


#path = "test.text"
#os.remove(path)

path_directory = "empty_dir" # The directory to be deleted
try:
    os.rmdir(path_directory)
except FileNotFoundError:
    print("That folder was not found")
except PermissionError:
    print("You do not have permission to delete that")
else:
    print(path_directory+ " was deleted")

