#CE code est fait pour voir le mouvement en Z n fonction du temps avec tous les XVG fusionnés por regrouper les données sur un seul plot.

#################
#### Library ####
#################

import numpy as np
import matplotlib.pyplot as plt
import glob
import os

###############
#### Code ####
##############

input_folder = "/home/mabadielim/Desktop/production_supercalculateur/SIMU_COMPLETE/both/trajetZ"

xvg_files = sorted(glob.glob(os.path.join(input_folder, "ethylene_z*.xvg")))

output_folder = "/home/mabadielim/Desktop/production_supercalculateur/SIMU_COMPLETE/both/ethylene/ethylene_plots_Z"
os.makedirs(output_folder, exist_ok=True)
output_file = os.path.join(output_folder, f"Z_all_ethylene.png")

#paremetre mb 
z_min_membrane = 4.1
z_max_membrane = 7.9
z_mid_membrane = (z_max_membrane + z_min_membrane) / 2


plt.figure(figsize=(15, 8)) 
plt.axhline(z_max_membrane - z_mid_membrane, color='red', linestyle='--', label="Limite membrane")
plt.axhline(z_min_membrane-z_mid_membrane, color='red', linestyle='--')
plt.fill_between([-10, 1100],z_max_membrane - z_mid_membrane,z_min_membrane-z_mid_membrane, color='gray', alpha=0.5, label="Zone membrane")

# Tracer chaque fichier .xvg
for i, file in enumerate(sorted(xvg_files)):
    data = np.loadtxt(file, comments=('@', '#'))
    time = data[:, 0] / 1000  # ns
    z = data[:, 3]
    deltaZ = z - z_mid_membrane
    basename = os.path.basename(file)
    resnum = ''.join(filter(str.isdigit, basename)) 
    label = os.path.basename(file).replace(".xvg", "")
    plt.scatter(time, deltaZ, label=label, marker= "." )

plt.xlabel("Temps (ns)")
plt.ylim(-7, 7)
plt.xlim(0,1000)
plt.ylabel("ΔZ (nm)")
plt.title("Distance Z des molécules d'ethylene au centre de la membrane")
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
plt.grid(True)
plt.tight_layout()
plt.savefig(output_file, dpi=600)
plt.show()
