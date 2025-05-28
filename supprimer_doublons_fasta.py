#Supprime les séquences fasta en double dans un fichier

#################
#### Library ####
#################

import os

###############
#### Code ####
##############

working_directory = "/home/mabadielim/Desktop"  
os.chdir(working_directory)

# Charger le fichier FASTA et enlever les doublons 
input_file = input("Nom du fichier FASTA en entrée : ")
output_file = input("Nom du fichier FASTA en sortie : ")

# Lire et stocker les séquences uniques
sequences_seen = {}
total_sequences = 0  # Compteur de séquences en entrée
unique_sequences = 0  # Compteur de séquences en sortie

with open(input_file, "r") as f:
    lines = f.readlines()

output_lines = []
current_header = None
current_sequence_lines = []

for line in lines:
    line = line.rstrip()  # Supprimer les espaces en fin de ligne
    if line.startswith(">"):  # nouvelle séquence
        if current_header and current_sequence_lines:
            sequence = "".join(current_sequence_lines)  # Reconstruire
            total_sequences += 1 
            if sequence not in sequences_seen:
                sequences_seen[sequence] = current_header
                output_lines.append(current_header)
                output_lines.extend(current_sequence_lines)  # Conserver les lignes originales
                unique_sequences += 1
        current_header = line
        current_sequence_lines = []
    else:
        current_sequence_lines.append(line)  # Conserver chaque ligne sans les modifier



# Ajouter un retour à la ligne entre les séquences
output_text = "\n".join(output_lines) + "\n" 

# Sauvegarder le fichier 
with open(output_file, "w") as f:
    f.write(output_text)

# Affichage du nombre de séquences en entrée et en sortie
print(f"  Séquences en entrée  : {total_sequences}")
print(f"  Séquences uniques    : {unique_sequences}")
print(f"  Fichier nettoyé enregistré : {output_file}\n")
