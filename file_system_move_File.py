import os

source = "main.txt"
destination = "newfile.txt"
os.rename(source,destination)
print("Source renamed to the destination path succesfully")