#Ce code sert à mesurer le nombre de diffusion de l'éthylène à travers la membrane et de calculer la moyenne de la durée d'une diffusion et l'ecart type ssocié.

#################
#### Library ####
#################

import os, glob
import numpy as np
import pandas as pd

###################
#### fonctions ####
###################
# Bornes de la membrane (en nm)
z_min = 4.1
z_max = 7.9

def get_transit_times(time, z, zmin=z_min, zmax=z_max):
   #On veut garder que ceux qui entrent d'un coté pour sortir de l'autre coté.
    inside = (z >= zmin) & (z <= zmax)
    crossings = []
    i = 0
    n = len(z)

    while i < n:
        if inside[i]:
            #on commence à l'indice i
            start = i
            # on cherche où on sort de la membrane
            while i < n and inside[i]:
                i += 1
            end = i - 1  # dernier point à l'intérieur

            # indices avant/après
            if start > 0 and end < n-1:
                z_before = z[start-1]
                z_after  = z[end+1]
                # je test si c'est bien allé du bas vers le haut
                if z_before < zmin and z_after > zmax:
                    crossings.append(time[end+1] - time[start-1])
                # ou du haut vers le bas
                elif z_before > zmax and z_after < zmin:
                    crossings.append(time[end+1] - time[start-1])
        else:
            i += 1

    return crossings

##############
#### CODE ####
##############



input_folder  = "/home/mabadielim/Desktop/production_supercalculateur/SIMU_COMPLETE/ethylene"
output_folder = "/home/mabadielim/Desktop/production_supercalculateur/SIMU_COMPLETE/ethylene/plots_Z"
os.makedirs(output_folder, exist_ok=True)


# on ouvre tous les fichiers qui ont ce format
pattern = os.path.join(input_folder, "ethylene_z*.xvg")
files = sorted(glob.glob(pattern))
if not files:
    raise FileNotFoundError(f"Aucun fichier trouvé pour {pattern}")

# Extraction des coordonnées. 
records = []
for f in files:
    mol = os.path.splitext(os.path.basename(f))[0]
    data = np.loadtxt(f, comments=('@','#'))
    time = data[:,0] / 1000   # ps → ns
    z    = data[:,3]

    for dur in get_transit_times(time, z):
        records.append({'molecule': mol, 'duration': dur})

# moyenne et ecart type

df = pd.DataFrame(records, columns=['molecule','duration'])

mean_val = df['duration'].mean()
std_val  = df['duration'].std()

df.loc[len(df)] = ['Moyenne', df['duration'].mean()]
df.loc[len(df)] = ['Ecart-type', std_val]

# on sauvegarde
out = os.path.join(output_folder, "temps_diffusion_ethylene.csv")
df.to_csv(out, index=False, float_format="%.4f")

print(df)
print(f"\nCSV → {out}")


