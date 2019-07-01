# Works with Python 3.7.2

# Constants
DELIM = '>'

# User input
input_path = input("What is the input path of the fasta file?")
output_path = input("What is the out path of the fasta file?")
num_of_frames = input("How many frames are in this fasta file?")

# Opens files based on user input.
fasta_string = open(input_path).read()
fasta_output = open(output_path, "w")

# Splits the fasta file based on the delim.
split_fasta = fasta_string.split(DELIM)

# Declare instance variables.
ctr = 0
greatest_strs = []
greatest_len = 0

# Iterates through all sequences in the fasta file.
for seq in split_fasta:
    # Adds the delim back to the front of the sequence.
    seq = DELIM + seq

    # Gets the sequence without the metadata.
    # The meta data of a fasta file is just the first line.
    seq_data = seq.split("\n", 1)[-1]

    # If the length is equal to the greatest.
    # Add it to the list since there is multiple greatest.
    if (len(seq_data) == greatest_len):
        greatest_strs.append(seq)

    # Else if, the length is greater than the greatest.
    elif (len(seq_data) > greatest_len):
        greatest_strs.clear()
        greatest_strs.append(seq)

        greatest_len = len(seq_data)

    # If we are on or over the last frame, reset and
    # add all of the greatests to output file.
    if (ctr >= num_of_frames):
        for elem in greatest_strs:
            fasta_output.write(elem)
        greatest_strs.clear()
        ctr = 0
        greatest_len = 0
    ctr += 1

# Close the output file.
fasta_output.close()