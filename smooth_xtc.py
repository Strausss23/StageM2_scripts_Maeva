#Me sert à obtenir un fichier xtc avec les trajectoires smoothés pour faire des rmsd avec après.

#################
#### Library ####
#################

import mdtraj as md
import numpy as np

###################
#### fonctions ####
###################

def smooth(x, window_len=11, window='hanning'):
    if x.ndim != 1:
        raise ValueError("smooth only accepts 1 dimension arrays.")
    if x.size < window_len:
        raise ValueError("Input vector needs to be bigger than window size.")
    if window_len < 3:
        return x
    if window not in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
        raise ValueError("Window must be one of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'")

    s = np.r_[2*x[0] - x[window_len-1::-1], x, 2*x[-1] - x[-1:-window_len:-1]]
    if window == 'flat':
        w = np.ones(window_len)
    else:
        w = getattr(np, window)(window_len)
    y = np.convolve(w / w.sum(), s, mode='same')
    return y[window_len:-window_len+1]


# Lissage des coordonnées d'une trajectoire mdtraj
def smooth_trajectory(traj, window_len=11, window='hanning'):
    smoothed = np.zeros_like(traj.xyz)
    for atom in range(traj.n_atoms):
        for coord in range(3):  # x, y, z
            smoothed[:, atom, coord] = smooth(traj.xyz[:, atom, coord], window_len, window)
    traj.xyz = smoothed
    return traj

###############
#### Code ####
##############

traj = md.load('/home/mabadielim/Desktop/production_supercalculateur/SIMU_COMPLETE/alone/md_VvETR2_1us_final.xtc', top='/home/mabadielim/Desktop/production_supercalculateur/SIMU_COMPLETE/alone/md_VvETR2_1us.gro')  # ou .gro/.prmtop/.psf selon ton système
traj_smooth = smooth_trajectory(traj, window_len=11, window='hanning')

traj_smooth.save_xtc('/home/mabadielim/Desktop/production_supercalculateur/SIMU_COMPLETE/alone/alone_smooth.xtc')
