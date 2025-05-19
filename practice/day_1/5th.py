import os
#choose a directory path to list its contents
directory_path="/Program Files (x86)"
#list the contents of the directory
contents = os.listdir(directory_path)
# print the contents of the directory
print (contents)
