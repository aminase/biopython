from Bio.Seq import Seq 
dna = Seq("ATGCAGTAGACGTGATAG")
print(dna)
print(dna.complement())
print(dna.reverse_complement())

from Bio import SeqIO
for sequence in SeqIO.parse("rcsb_pdb_4HRT", "fasta"):
    print(sequence.id)

