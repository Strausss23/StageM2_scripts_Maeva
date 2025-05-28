#################
#### Library ####
#################

import mdtraj as md

##############
#### CODE ####
##############

pdb = md.load_pdb("/home/mabadielim/Desktop/00.pdb")

rg = md.compute_rg(pdb)[0]*10

perimetre = rg *3.14 *2

print(f"Rayon de giration : {rg:.5f} Å, perimetre = {perimetre: .3f}")
