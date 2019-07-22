## Simple Bioinformatics Scripts

- [Overview](#overview)
- [Scripts](#scripts)
- [License](#license)

<a name="overview"/></a>
## Overview
This is the repository for the development of simple bioinformatics scripts.

<a name="scripts"></a>
## Scripts
Here is a list of all available scripts.
- [Simple NCBI Blastp](scripts/simple-ncbi-blastp.py)
  - This performs a simple protein BLAST on the NCBI NR database based on a user provided fasta file. This can perform singular BLASTs and a collection of BLASTs.
  - [Sample data](sample-data/simple-ncbi-blastp-sample.fa)

- [Collect Greatest Open Reading Frame](scripts/collect-greatest-frame.py)
  - This collects the greatest translated nucleotide sequence from a collection of open reading frames. 
  - [Sample data](sample-data/collect-greatest-frame-sample.fa)

- [Find name(s) in Fasta](scripts/find-names-in-fasta.py)
  - Collects all of the names of the sequences within a fasta query file and outputs it to a file.
  - [Sample data](sample-data/find-name-in-fasta-in.fa)

<a name="license"></a>
## License
[Project License](LICENSE.md)
