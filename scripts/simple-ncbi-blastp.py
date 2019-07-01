# Works with Python 3.7.2
# Install Biopython -> "pip install biopython"

# Import libraries
from Bio.Blast import NCBIWWW 
from Bio.Blast import NCBIXML
import os

# Open file

input_path = input("What is the file path of the fasta query?")
output_path = input("What is the output file path of the fasta query?")
fasta_string = open(input_path).read()

# Process the BLASTp
result_handle = NCBIWWW.qblast("blastp", "nr", fasta_string)

# Parses the result handle to collect all of the BLAST records.
blast_records = NCBIXML.parse(result_handle)

# Opens the output file.
aFile = open(output_path, "w")

# Set the e value threshold to determine which records
# are pulled from the database.
# For more info -> http://pathblast.org/docs/e_value.html
E_VALUE_THRESH = 0.05

# Outputs some basic info about blast hits.
for blast_record in blast_records:
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < E_VALUE_THRESH:
                aFile.write("****Alignment****")
                aFile.write("sequence:", alignment.title)
                aFile.write("length:", alignment.length)
                aFile.write("e value:", hsp.expect)
                aFile.write(hsp.query[0:75] + "...")
                aFile.write(hsp.match[0:75] + "...")
                aFile.write(hsp.sbjct[0:75] + "...")

# Closes the result handle.
result_handle.close()

# Closes the file.
aFile.close()