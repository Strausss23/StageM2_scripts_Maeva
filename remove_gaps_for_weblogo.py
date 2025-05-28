#Ce code sert à supprimer les indels des weblogos pour les rendre + lisible

#################
#### Library ####
#################

from Bio import AlignIO

##############
#### CODE ####
##############
input_file = "/home/mabadielim/Desktop/Sequences/alignement multiple/BlastP_transmb/Selection_ETR/alignement_ETR/clustalo-I20250324-154102-0930-5546551-p1m.aln-clustal_num"
output_file = "/home/mabadielim/Desktop/Sequences/alignement multiple/BlastP_transmb/Selection_ETR/alignement_ETR/gaps_removed.fasta" 
gap_threshold = 0.7  # Seuil max de gaps 

alignment = AlignIO.read(input_file, "clustal")
columns_to_keep = []

# colonnes à garder 
for i in range(alignment.get_alignment_length()):
    gap_count = sum(1 for record in alignment if record.seq[i] == '-')
    if gap_count / len(alignment) < gap_threshold:
        columns_to_keep.append(i)

# création de nouvelles séquences avce les colonnes qu'on a gardé.
with open(output_file, "w") as out:
    for record in alignment:
        filtered_seq = ''.join(record.seq[i] for i in columns_to_keep)
        out.write(f">{record.id}\n{filtered_seq}\n")

print("Alignement filtré enregistré dans", output_file)
