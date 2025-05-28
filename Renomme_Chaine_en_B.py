#Sert à changer le nom de la chaine en B

#################
#### Library ####
#################
import os

###################
#### fonctions ####
###################

def modify_pdb_chain(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".pdb"):
            file_path = os.path.join(directory, filename)

            with open(file_path, "r") as file:
                lines = file.readlines()

            modified_lines = []
            for line in lines:
                if line.startswith(("ATOM", "HETATM")):  # Vérifier si c'est une ligne d'atome
                    modified_line = line[:21] + "B" + line[22:]  # Modifier la colonne de la chaîne
                else:
                    modified_line = line  # Ne pas modifier les autres lignes
                modified_lines.append(modified_line)

            # Écraser le fichier original
            with open(file_path, "w") as file:
                file.writelines(modified_lines)

            print(f" Modifié : {filename}")

##############
#### CODE ####
##############

dossier_pdb = "/home/mabadielim/Desktop/FreSA/Preparation 8/B/output/"
modify_pdb_chain(dossier_pdb)
