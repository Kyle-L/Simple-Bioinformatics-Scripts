# Works with Python 3.7.2
import re

# User input
file_in_path = input("What is the input path of the fasta file?")
file_out_path = input("What is the out path where the names will go?")

# Opens the output file.
file_out = open(file_out_path, "w")

# Opens the input file.
with open(file_in_path) as fp:
    # Iterates through each line.
    line = fp.readline()
    while line:
        # Finds a line that meets the regex expression of '>name of sequence'
        matches = re.findall(r'>(.+?) ', line)
        # If a match is found, output to the output file.
        if len(matches) > 0:
            file_out.write(matches[0] + "\n")
        # Read the next line.
        line = fp.readline()

# Close the output file.
file_out.close()

