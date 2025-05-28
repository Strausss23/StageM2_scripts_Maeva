#Programme pour faire un csv contenant le temps que passe chaque ligand dans les différentes parties avec membrane et ecart type

#################
#### Library ####
#################

import pandas as pd
import os
import glob
from io import StringIO

##############
#### CODE ####
##############


input_folder = "/home/mabadielim/Desktop/production_supercalculateur/SIMU_COMPLETE/both/trajetZ"
output_csv = "/home/mabadielim/Desktop/production_supercalculateur/SIMU_COMPLETE/both/resume_temps_ethanol_membrane_proteine.csv"

# Limites Z de la membrane (nm)
z_min_membrane = 4.1
z_max_membrane = 7.9

# Limites XY de la protéine 
x_min_prot, x_max_prot = 1.9, 4.7
y_min_prot, y_max_prot = 1.9, 4.6


xvg_files = sorted(glob.glob(os.path.join(input_folder, "ethanol_*.xvg")))  #on récupère tous les xvg qui ont un nom de ce format là
summary_list = []

#boucle pour chaque fichier xvg
for filepath in xvg_files:
    filename = os.path.basename(filepath)
    ethanol_id = filename.replace("ethanol_", "").replace(".xvg", "")

    with open(filepath, 'r') as f:
        lines = [line for line in f if not line.startswith(('@', '#'))]
    data = pd.read_csv(StringIO(''.join(lines)), sep=r'\s+', header=None)

    # extraction des colonnes
    time_ps = data.iloc[:, 0]
    x = data.iloc[:, 1]
    y = data.iloc[:, 2]
    z = data.iloc[:, 3]

    time_ns = time_ps / 1000  # conversion ps en ns
    delta_t_ns = time_ns.diff().fillna(0)

    #on regarde si c'est dans la membrane ou dans la protéine
    in_membrane = (z >= z_min_membrane) & (z <= z_max_membrane)
    in_protein = (x >= x_min_prot) & (x <= x_max_prot) & (y >= y_min_prot) & (y <= y_max_prot) & (z >= z_min_membrane) & (z <= z_max_membrane)
    

    #on calcule chaque durée
    time_in_protein = delta_t_ns[in_protein].sum()
    time_in_lipid = delta_t_ns[in_membrane].sum() - time_in_protein #on deduit bien le temps passé dans la protéine sinon c'est faux
    time_out_membrane = delta_t_ns[~in_membrane].sum()
    time_total = delta_t_ns.sum()

    # on ajoute ça au summary
    summary_list.append({
        "Fichier": filename,
        "ethanol_ID": ethanol_id,
        "Temps_dans_proteine_ns": round(time_in_protein, 3),
        "Temps_dans_lipide_ns": round(time_in_lipid, 3),
        "Temps_hors_membrane_ns": round(time_out_membrane, 3),
        "Temps_total_ns": round(time_total, 3)
    })



#on transforme le summary en dataframe
df = pd.DataFrame(summary_list)
num = df.select_dtypes(include="number")
mean_val = num.mean().round(3)
std_val  = num.std().round(3)

#je veux aussi moyenn et ecart type à la fin 

stats_df = pd.DataFrame([
    {
        "Fichier":               "",
        "ethanol_ID":           "Moyenne",
        "Temps_dans_proteine_ns": mean_val["Temps_dans_proteine_ns"],
        "Temps_dans_lipide_ns":   mean_val["Temps_dans_lipide_ns"],
        "Temps_hors_membrane_ns": mean_val["Temps_hors_membrane_ns"],
        "Temps_total_ns":         mean_val["Temps_total_ns"],
    },
    {
        "Fichier":               "",
        "ethanol_ID":           "Écart-type",
        "Temps_dans_proteine_ns": std_val["Temps_dans_proteine_ns"],
        "Temps_dans_lipide_ns":   std_val["Temps_dans_lipide_ns"],
        "Temps_hors_membrane_ns": std_val["Temps_hors_membrane_ns"],
        "Temps_total_ns":         std_val["Temps_total_ns"],
    }
])

# j'ajoute la moyenne et l'ecart type dans le df
df = pd.concat([df, stats_df], ignore_index=True)


df.to_csv(( output_csv), index=False)

print(df)

print(f"\n Sauvegardé dans : {output_csv}") #pour être sur d'être dans le bon fichier


