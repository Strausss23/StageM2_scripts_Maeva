#Je fais des plots pour suivre de deltaZ disance de la membrane de l'ethylene

#################
#### Library ####
#################

import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
import os
import glob
import numpy as np

###################
#### fonctions ####
###################

def smooth(x,window_len=11,window='hanning'):
        if x.ndim != 1:
                raise ValueError("smooth only accepts 1 dimension arrays.")
        if x.size < window_len:
                raise ValueError("Input vector needs to be bigger than window size.")
        if window_len<3:
                return x
        if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
                raise ValueError("Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'")
        s=np.r_[2*x[0]-x[window_len-1::-1],x,2*x[-1]-x[-1:-window_len:-1]]
        if window == 'flat': #moving average
                w=np.ones(window_len,'d')
        else:
                w=eval('np.'+window+'(window_len)')
        y=np.convolve(w/w.sum(),s,mode='same')
        return y[window_len:-window_len+1]

###############
#### Code ####
##############

# Paramètres membrane
z_min_membrane = 4.1
z_max_membrane = 7.9
z_mid_membrane = (z_max_membrane + z_min_membrane) / 2

input_folder = "/home/mabadielim/Desktop/production_supercalculateur/SIMU_COMPLETE/ethylene"

xvg_files = sorted(glob.glob(os.path.join(input_folder, "ethylene_z*.xvg")))

output_folder = "/home/mabadielim/Desktop/production_supercalculateur/SIMU_COMPLETE/ethylene/plots_Z"
os.makedirs(output_folder, exist_ok=True)

# Boucle sur chaque fichier
for file_path in xvg_files:
    filename = os.path.basename(file_path)
    ethylene_id = filename.replace("ethylene_z", "").replace(".xvg", "")

    # Lecture du fichier
    with open(file_path, 'r') as f:
        lines = [line for line in f if not line.startswith(('@', '#'))]
    data = pd.read_csv(StringIO(''.join(lines)), sep=r'\s+', header=None)

    # Extraction du temps et coordonnée Z
    time = data.iloc[:, 0] / 1000  # ns
    z = data.iloc[:, 3]            # nm
    deltaZ = z - z_mid_membrane

    # Tracé
    plt.figure(figsize=(15, 8))
    plt.scatter(time, deltaZ, label="ΔZ distance au centre membrane", marker= "." )
    plt.axhline(z_max_membrane -z_mid_membrane, color='red', linestyle='--', label="Limite membrane")
    plt.axhline(z_min_membrane -z_mid_membrane, color='red', linestyle='--')
    plt.fill_between(time,z_min_membrane -z_mid_membrane ,z_max_membrane -z_mid_membrane , color='gray', alpha=0.2, label="Zone membrane")
    plt.xlabel("Temps (ns)")
    plt.ylabel("ΔZ (nm)")
    plt.ylim(-7, 7)
    plt.title(f"ethylene {ethylene_id} — Distance au centre membrane")
    plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1))
    plt.grid(True)
    plt.tight_layout()

    # Sauvegarde
    output_file = os.path.join(output_folder, f"format_1_ethylene_z{ethylene_id}_DeltaZ_.png")
    plt.savefig(output_file, dpi=300)
    plt.close()

print(f"Enregistrés dans : {output_folder}")
