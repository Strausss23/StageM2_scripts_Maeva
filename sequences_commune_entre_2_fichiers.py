#je regarde les séquences communes dans deux fichiers différents (les msa et un de mes jeux de données ETR)

#################
#### Library ####
#################

from Bio import SeqIO


##############
#### Code ####
##############


file1_path = "/home/mabadielim/Desktop/python_prod/msa/msa_af2.a3m"
file2_path = "/home/mabadielim/Desktop/python_prod/fa et fasta/ETR_700.fasta"

# Lire les identifiants des séquences dans le fichier .a3m
identifiers_file1 = set()
with open(file1_path, "r") as file1:
    for record in SeqIO.parse(file1, "fasta"):
        identifiers_file1.add(record.id)

# Lire les identifiants des séquences dans le fichier .fasta
identifiers_file2 = set()
with open(file2_path, "r") as file2:
    for record in SeqIO.parse(file2, "fasta"):
        identifiers_file2.add(record.id)

# Trouver les identifiants communs
common_identifiers = identifiers_file1.intersection(identifiers_file2)

# Nombre de séquences en commun
num_common_sequences = len(common_identifiers)
num_common_sequences
