# Works with Python 3.7.2
import re

# User input
fasta_query_path = input("What is the path of the fasta query file?")
fasta_names_path = input("What is the path of the fasta names file?")
output_path = input("What is the path of the output file?")

# The dictionary for parsing the fasta query.
fasta_dict = {}

# Opens the output file.
file_out = open(output_path, "w")

# Opens the fasta query file.
with open(fasta_query_path) as fp:
    # Split the queries up.
    fasta_list = fp.read().split(">")
    # Iterate through the queries.
    for name in fasta_list:
        # Gets the name of the fasta query.
        name = ">" + name
        name = re.findall(r'>(.+?) ', name)
        # If the fasta query has a name, add it to
        # the dictionary with the name as the key
        # and the whole fasta sequence as the value.
        if (len(name) > 0):
            fasta_dict[name[0].strip()] = name

# Opens the fasta name file.
with open(fasta_names_path) as fp:
    # Splits the file into lines.
    fasta_names = fp.read().split("\n")
    # Iterates through the names.
    for name in fasta_names:
        # Try to retrieve the fasta sequences from the
        # dictionary and output it to the output file.
        try:
            file_out.write(fasta_dict[name.strip()])
        # If it can't be written, continue to next name.
        except:
            print(name + " does not exist in " + fasta_query_path)
            continue

# Close the output file.
file_out.close()