import os

# The File path to the file we write to.
file_path = "C:\\Users\\kavet\\OneDrive\\Desktop\\text.txt"

# The text to write in the file.
text = """     
        Yoo This is a text.
        Let it work.
        """
        
#Open file and write to it.
with open(file_path,'w') as file:
    file.write(text)

