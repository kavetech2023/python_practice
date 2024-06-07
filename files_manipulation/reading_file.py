"""Reading contents of a file using python
   NOTE: Closes the file automatically
"""

file_path = "C:\\Users\\kavet\\OneDrive\\Desktop\\text.txt"
file_path_fake = ""

try:
    with open(file_path_fake) as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found.")