#Ce code sert à faire une figure RMSF avec la chaine A audessu et B en dessous. Dedans j'annote aussi les positions des résidus qui m'interesse et je marque en rose les zones de linker et N-ter.

#################
#### Library ####
#################

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

###################
#### fonctions ####
###################
def load_xvg(filename):
    data = []
    with open(filename) as f:
        for line in f:
            if not line.startswith(('@', '#')):
                data.append([float(x) for x in line.split()])
    return np.array(data)

##############
#### CODE ####
##############

# Fichiers, labels, couleurs
files = [
    ("/home/mabadielim/Desktop/production_supercalculateur/SIMU_COMPLETE/alone/rmsf_VvETR2_Ca.xvg",   "VvETR2",     "black"),
    ("/home/mabadielim/Desktop/production_supercalculateur/SIMU_COMPLETE/ethylene/rmsf_ETHE_Ca.xvg","Ethylene","red"),
    ("/home/mabadielim/Desktop/production_supercalculateur/SIMU_COMPLETE/ethanol/rmsf_ETOH_Ca.xvg", "Ethanol",  "green"),
    ("/home/mabadielim/Desktop/production_supercalculateur/SIMU_COMPLETE/both/rmsf_both_Ca.xvg",     "Ethylene + Ethanol",     "blue")
]


# linker et n-ter
highlight_ranges = [
    (1, 17-1),   
    (49, 54-49),
    (78, 83-78), 
    (119, 120-119)
]

highlights = [8,10,29, 36, 68, 72, 94] #résidus important

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

for path, label, color in files:
    data = load_xvg(path)
    residus = data[:, 0]
    rmsf    = data[:, 1] * 10

    # Chaîne A
    res_a,  rmsf_a = residus[:120], rmsf[:120]
    # Chaîne B
    res_b,  rmsf_b = residus[120:] - 120, rmsf[120:]

    ax1.plot(res_a, rmsf_a, label=label, color=color)
    ax2.plot(res_b, rmsf_b, label=label, color=color)

# Calcul de la hauteur de barre 
for ax in (ax1, ax2):
    ymax = 10
    bar_h = 0.03 * ymax
    ax.set_ylim(0, ymax)
    # Dessine les barres roses
    ax.broken_barh(highlight_ranges,
                   (0, bar_h),
                   facecolors='pink')

#marque en orange les résidus importants    
for x in highlights:
    ax1.axvline(x, color='orange', linestyle='--', linewidth=1)
    ax2.axvline(x, color='orange', linestyle='--', linewidth=1)

base_ticks = sorted(set(list(ax2.get_xticks()) + highlights))

# On applique aux deux axes
for ax in (ax1, ax2):
    ax.set_xticks(base_ticks)
    ax.tick_params(axis='x', which='both', labelbottom=True)


# Légende
pink_patch = mpatches.Patch(facecolor='pink', edgecolor='none', label='Linker')
handles, labels = ax1.get_legend_handles_labels()
handles.append(pink_patch)
labels.append('Linker')
ax1.legend(handles=handles, labels=labels, ncol=2, fontsize="small", loc="upper right")
ax1.set_title("Chain A")
ax2.set_title("Chain B")
ax1.set_ylabel("RMSF (Å)")
ax2.set_ylabel("RMSF (Å)")
ax2.set_xlabel("Residues")
ax1.set_xlim(1, 120)
ax2.set_xlim(1, 120)
ax1.set_ylim(0, 10)
ax2.set_ylim(0, 10)
fig.suptitle("RMSF of C-alpha atoms of residues of VvETR2 across different experimental conditions", fontsize=13, y=0.98)
plt.tight_layout()
plt.show()