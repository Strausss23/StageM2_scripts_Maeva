#Renome tous les PDB dans un dossier dans l'ordre numérique.

#################
#### Library ####
#################

import os

###################
#### fonctions ####
###################
def rename_pdb_files(directory, prefix="B"):
    

    files = [f for f in os.listdir(directory) if f.endswith(".pdb")]
     
    # Trier les fichiers pour une numérotation ordonnée
    files.sort()

    print(f"Fichiers trouvés : {files}")
    
    for index, file in enumerate(files, start=1):
        old_path = os.path.join(directory, file)
        new_name = f"{prefix}{index:03d}.pdb"  # Format : fichier_001.pdb
        new_path = os.path.join(directory, new_name)

        try:
            os.rename(old_path, new_path)
            print(f"Renommé: {file} -> {new_name}")
        except Exception as e:
            print(f"Erreur lors du renommage de {file}: {e}")


##############
#### CODE ####
##############

path = "/home/mabadielim/Desktop/Pour FreSA/Preparation 8/B/output/"
print(os.listdir(path))
rename_pdb_files(path)
