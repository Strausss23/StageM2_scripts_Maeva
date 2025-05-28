#################
#### Library ####
#################

import os 

###############
#### Code ####
##############

working_directory = "/home/mabadielim/Desktop/Sequences/alignement multiple/BlastP_transmb/Selection_ETR/" 
os.chdir(working_directory)

input_file = input("sequences.fasta :") 
output_file = input("sequences_uniques.fasta :")

# Mot-clé à rechercher 
keyword = "ethylene receptor"

# Variables pour stocker les séquences filtrées
output_lines = []
keep_sequence = False
count_selected = 0
count_total = 0

# Lire le fichier FASTA et filtrer les séquences
with open(input_file, "r") as f:
    for line in f:
        if line.startswith(">"):  # Nouvelle séquence
            count_total += 1
            if keyword.lower() in line.lower():  # Vérifier si "ethylene receptor" est dans l'identifiant
                keep_sequence = True
                count_selected += 1
                output_lines.append(line) 
            else:
                keep_sequence = False
        elif keep_sequence:
            output_lines.append(line)  # Ajouter la séquence si elle correspond

# Sauvegarder le fichier filtré
with open(output_file, "w") as f:
    f.writelines(output_lines)

# Afficher un résumé
print(f"Séquences analysées : {count_total}")
print(f"Séquences retenues (ethylene receptor) : {count_selected}")
print(f"Fichier généré : {output_file}")
