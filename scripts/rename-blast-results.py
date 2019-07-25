# Works with Python 3.7.2
import os
import re

# User input
directory_path = input("What is the path of the directory that the query files are in?")

# Opens the directory.
directory = os.fsencode(directory_path)

# Get all the files in the directory
files = os.listdir(directory)

# Iterates through all files in a directory.
for file in files:
    # Gets the filename.
    filename = os.fsdecode(file)

    # Opens the file.
    file_to_open = directory_path + "\\" + filename
    file = open(file_to_open)

    # Reads the file to a string.
    file_str = file.read()

    # Finds the name of query. (Presumes there is no spaces in name.)
    matches = re.findall(r'Query= (.+?) ',file_str)
    if len(matches) > 0:
        name = matches[0]
        name = name.strip()
        # print(name)
    file.close()

    # Renames the file.
    os.rename(file_to_open, directory_path + "\\" + name + ".txt")