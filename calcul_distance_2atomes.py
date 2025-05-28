#Ce code permet de calculer la distance entre 2 atomes

#################
#### Library ####
#################

import numpy as np
from Bio.PDB import PDBParser

###################
#### fonctions ####
###################

def recuperationcoordonnees(pdb,namechaine,positionresidu): 
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure("protein", pdb) #lire la structure proteine dans le pdb
    coord = next(
    (atom.coord 
    for model in structure 
    for chain in model if chain.id == namechaine #Pour chaque chaine parce qu'on a un homodimere
    for residue in chain if residue.get_resname() == "CYM" and residue.id[1] == positionresidu
    for atom in residue if atom.get_name() == "SG"), 
    None)
    return coord

folder_path = "/home/mabadielim/Desktop/DisulfideBridge/881010.pdb" 

##############
#### CODE ####
##############

coordA = recuperationcoordonnees(folder_path,"A",8)
coordB = recuperationcoordonnees(folder_path,"B",8)
distance = abs(np.linalg.norm(np.array(coordA) - np.array(coordB)))

print(distance)