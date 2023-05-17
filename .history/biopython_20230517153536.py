from Bio.Seq import Seq 
dna = Seq("ATGCAGTAGACGTGATAG")
print(dna)
print(dna.complement())
print(dna.reverse_complement())

from Bio import SeqIo

