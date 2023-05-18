from Bio.Seq import Seq 
dna = Seq("ATGCAGTAGACGTGATAG")
print(dna)
print(dna.complement())
print(dna.reverse_complement())

from Bio import SeqIO
for sequence in SeqIO.parse("./content/rcsb_pdb_4HRT.fasta", "fasta"):
    print("Id of a sequence is: " ,sequence.id)
    print("Sequence itself: ", sequence.seq)
    print("Length of a sequence: ", len(sequence))

