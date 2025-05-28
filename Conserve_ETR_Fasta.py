#faire en sorte que seule des séquences possédant ETR ou une appelation similaire soit conserver.
#################
#### Library ####
#################
import os 

##############
#### CODE ####
##############

working_directory = "/home/mabadielim/Desktop/Sequences/alignement multiple/"  
os.chdir(working_directory)

# Nom des fichiers d'entrée et sortie
input_file = input("sequences.fasta :")  
output_file = input("sequences_uniques.fasta :")

# Mot à chercher
keyword = "ethylene receptor"

output_lines = []
keep_sequence = False
count_selected = 0
count_total = 0


with open(input_file, "r") as f: #ouvre le fasta
    for line in f:
        if line.startswith(">"):  #lire chaque séquences du fasta quand une ligne commence par >
            count_total += 1
            if keyword.lower() in line.lower():  #On regade si la séquence a le mot qu'on cherche
                keep_sequence = True
                count_selected += 1
                output_lines.append(line)  
            else:
                keep_sequence = False
        elif keep_sequence:
            output_lines.append(line)  

with open(output_file, "w") as f: #on écrit dans un nouveau fasta les séquences qu'on garde pour la suite
    f.writelines(output_lines)

# infos
print(f"Séquences analysées : {count_total}")
print(f"Séquences retenues (ethylene receptor) : {count_selected}")
print(f"Fichier généré : {output_file}")
