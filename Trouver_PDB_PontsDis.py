#Ce PDB a pour but de sélectioner les PDB où un pont disulfulre est possible

#################
#### Library ####
#################
import os
import numpy as np
from Bio.PDB import PDBParser


#################
### Fonctions ###
#################

#Recuperation des coordonnées du SG d'une CYS
def recuperationcoordonnees(pdb,namechaine,positionresidu): 
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure("protein", pdb)
    coord = next(
    (atom.coord 
    for model in structure
    for chain in model if chain.id == namechaine
    for residue in chain if residue.get_resname() == "CYS" and residue.id[1] == positionresidu
    for atom in residue if atom.get_name() == "SG"), 
    None)
    return coord


#Calcul des distances
def calculsdistances(coordA8, coordA10, coordB8, coordB10) : 
    pontA8B8 = abs(np.linalg.norm(np.array(coordB8) - np.array(coordA8)))
    pontA10B10 = abs(np.linalg.norm(np.array(coordA10) - np.array(coordB10)))
    pontA8B10 = abs(np.linalg.norm(np.array(coordA8) - np.array(coordB10)))
    pontA10B8 = abs(np.linalg.norm(np.array(coordB8) - np.array(coordA10)))              
    return(pontA8B8, pontA10B10,pontA8B10,pontA10B8)


###############
#### Code ####
##############

compteur = 0
nb_resultats = 0
resultats = ""
folder_path = "/home/mabadielim/Desktop/bridge/881010/" #là où il y a tous les pdb générés par FResA
#output_path = "/home/mabadielim/Desktop/test_pdb/resultats.txt"

#parcourir tous les pdb
for file in os.listdir(folder_path) : 
    if file.endswith(".pdb") :
        pdb_path = os.path.join(folder_path, file)
        compteur += 1 #pour signaler à quel pdb on en est quand on lance le programme
        coordA8 = recuperationcoordonnees(pdb_path,"A",8)
        coordA10 = recuperationcoordonnees(pdb_path,"A",10)
        coordB8 = recuperationcoordonnees(pdb_path,"B",8)
        coordB10 = recuperationcoordonnees(pdb_path,"B",10)
        pontA8B8, pontA10B10,pontA8B10,pontA10B8 = calculsdistances(coordA8, coordA10, coordB8, coordB10)
        if pontA8B8 < 2 or pontA10B10 < 2 or pontA10B8 < 2 or pontA8B10 < 2 : 
            nb_resultats += 1
            resultats += (file) + " Distance entre les SG 8 des deux chaines : " + str(pontA8B8) + " Distance entre les SG 10 des deux chaines : " + str(pontA10B10) + "\n" + "Du GC Cys A8 et B10 : " + str(pontA8B10) + " Et des SG Cys A10 et B8 : " + str(pontA10B8) + "\n"
        print(f'{file} : pdb trouvé :  {pontA8B8}')
        #time.sleep(0.5) 
        
#print(resultats)
#with open(output_path, "w") as f:
#    f.write(resultats)



