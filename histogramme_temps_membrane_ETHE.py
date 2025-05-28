#histogramme du temps que passe les molécules d'ethylene dans la membrane

#################
#### Library ####
#################

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

##############
#### CODE ####
##############

df = pd.read_csv("/home/mabadielim/Desktop/production_supercalculateur/SIMU_COMPLETE/both/resume_temps_ethylene_membrane_proteine.csv")

df['Temps_dans_proteine_ns'] = df['Temps_dans_proteine_ns'].astype(float)
df['Temps_dans_membrane_ns'] = df['Temps_dans_lipide_ns'].astype(float)
df['Temps_hors_membrane_ns'] = df['Temps_hors_membrane_ns'].astype(float)

ethylene_ids = df['Ethylene_ID'].astype(str)
x = np.arange(len(ethylene_ids))
width = 0.25

# FIGURE 1 : Histogramme groupé
plt.figure(figsize=(14, 6))
plt.bar(x - width, df['Temps_dans_proteine_ns'], width, label='Dans la protéine')
plt.bar(x, df['Temps_dans_membrane_ns'], width, label='Dans la membrane')
plt.bar(x + width, df['Temps_hors_membrane_ns'], width, label='Hors de la membrane')

plt.xlabel("ID Ethylene")
plt.ylabel("Temps (ns)")
plt.title("Temps par région – Histogramme groupé")
plt.xticks(x, ethylene_ids, rotation=45, ha='right')
plt.legend()
plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("/home/mabadielim/Desktop/production_supercalculateur/SIMU_COMPLETE/both/histogramme_groupé_ethylene.png", dpi=300)
plt.show()

#FIGURE 2 : Histogramme empilé
plt.figure(figsize=(14, 6))
plt.bar(x, df['Temps_dans_proteine_ns'], width, label='Dans la protéine')
plt.bar(x, df['Temps_dans_membrane_ns'], width, bottom=df['Temps_dans_proteine_ns'], label='Dans la membrane')
plt.bar(x, df['Temps_hors_membrane_ns'], width, 
        bottom=df['Temps_dans_proteine_ns'] + df['Temps_dans_membrane_ns'], label='Hors de la membrane')

plt.xlabel("ID Éthanol")
plt.ylabel("Temps cumulé (ns)")
plt.title("Temps par région – Histogramme empilé")
plt.xticks(x, ethylene_ids, rotation=45, ha='right')
plt.legend()
plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("/home/mabadielim/Desktop/production_supercalculateur/SIMU_COMPLETE/both/histogramme_empilé_ethylene.png", dpi=300)
plt.show()