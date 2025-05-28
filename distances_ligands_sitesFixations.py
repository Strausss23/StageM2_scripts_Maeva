#ce code est fait pour mesurer la distances entre l'ethanol et ou l'ethylene avec le site de fixation à l'ethanol

#################
#### Library ####
#################
import matplotlib.pyplot as plt
import pandas as pd
import re
from io import StringIO


##############
#### CODE ####
##############

fichier = "~/Desktop/production_supercalculateur/vvETR2/ethylene/distances_ethylenes_siteB.xvg"

with open(fichier, 'r') as f:
    lines = [line for line in f if not re.match(r'^[@#]', line)]


data = pd.read_csv(StringIO(''.join(lines)), sep=r'\s+')
data = data.dropna(axis=1, how='all')  # au cas ou

# on récupère le temps + distances
time_ps = data.iloc[:, 0]
distances_nm = data.iloc[:, 1:]
distances_angstrom = distances_nm * 10

plt.figure(figsize=(10, 6))
for i in range(distances_angstrom.shape[1]):
    plt.plot(time_ps, distances_angstrom.iloc[:, i], label=f'Éthylène {i+1}')

plt.axhline(y=5.0, color='black', linestyle='--', linewidth=2, label='Seuil 5 Å') # j'ajoute une ligne à 5 Å
plt.xlabel('Temps (ps)')
plt.ylabel('Distance (Å)')
plt.title('Distances des éthylene au site de fixation B')
plt.legend(loc='upper right', fontsize='small', ncol=2)
plt.grid(True)
plt.tight_layout()
plt.savefig("distances_ethanol_siteA.png", dpi=300)
plt.show()
