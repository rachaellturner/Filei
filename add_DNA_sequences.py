# Modules
from Bio import SeqIO
import re

records = []
regex = re.compile(r"^[a-zA-Z0-9]+_[a-zA-Z0-9]+_([a-zA-Z0-9]+)")
regex2 = re.compile(r"([0-9]+)-([0-9]+)")

OUTF = open("LINEs_with_sequences.csv", "wt")
OUTF.write("repName\tgenoStart\tgenoEnd\tDNAseq\n")

# Updates list with description and sequence in tuple format (description, sequence)
for seq_record in SeqIO.parse("LINE_sequences.txt", "fasta"):
	print("Processing sequences...")
	records.append((seq_record.description, str(seq_record.seq)))
	
# Creates CSV file from list of tuples

OUTF = open("LINEs_with_sequences.csv", "wt")
OUTF.write("repName\tgenoStart\tgenoEnd\tDNAseq\n")

for pair in records:
	print("Writing sequences to output file...")
	coord = re.search(regex2, pair[0])
	genoStart = coord.group(1)
	genoEnd =  coord.group(2)
	OUTF.write((regex.search(pair[0])).group(1)+"\t"+genoStart+"\t"+genoEnd+"\t"+pair[1]+"\n")

OUTF.close()
