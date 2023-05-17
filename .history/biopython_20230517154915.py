

from Bio import SeqIO
for sequence in SeqIO.parse("rcsb_pdb_4HRT.fasta", "fasta"):
    print(sequence.seq)

