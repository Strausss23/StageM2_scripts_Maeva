#Sert à fusionner tous les pdb contenants la chaine A avec tous les pdb contenant la chaine B dans toutes les configurations possibles 
#généré par MomaFResA pour faciliter l'analyse

#################
#### Library ####
#################

import os

###################
#### fonctions ####
###################
def combine_pdb_files(dir_a, dir_b, output_dir):
    # Vérifier si les dossiers existent
    if not os.path.exists(dir_a) or not os.path.exists(dir_b):
        print("le dossier n'existe pas.")
        return
    
    # Créer le dossier de sortie s'il n'existe pas
    os.makedirs(output_dir, exist_ok=True)
    
    # Lister les fichiers dans chaque dossier
    files_a = [f for f in os.listdir(dir_a) if f.endswith(".pdb")]
    files_b = [f for f in os.listdir(dir_b) if f.endswith(".pdb")]
    
    if not files_a or not files_b:
        print("Aucun fichier .pdb ")
        return
    
    # Générer toutes les combinaisons possibles
    for file_a in files_a:
        for file_b in files_b:
            path_a = os.path.join(dir_a, file_a)
            path_b = os.path.join(dir_b, file_b)
            
            # Créer un nouveau fichier dans le dossier de sortie
            combined_filename = f"{file_a.replace('.pdb', '')}_{file_b.replace('.pdb', '')}.pdb"
            output_path = os.path.join(output_dir, combined_filename)
            
            # Fusionner les deux fichiers
            with open(output_path, "w") as out_file:
                with open(path_a, "r") as a_file:
                    out_file.writelines(a_file.readlines())
                with open(path_b, "r") as b_file:
                    out_file.writelines(b_file.readlines())
            
            print(f"Fichier créé : {combined_filename}")

###############
#### Code ####
##############

dir_a = "/home/mabadielim/Desktop/FreSA/Preparation 8/A/output/"
dir_b = "/home/mabadielim/Desktop/FreSA/Preparation 8/B/output/"
output_dir = "/home/mabadielim/Desktop/FreSA/Preparation 8/all_combinaison"

combine_pdb_files(dir_a, dir_b, output_dir)
