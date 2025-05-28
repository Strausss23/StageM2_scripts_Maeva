#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mda_MG.py
#  
#  Copyright 2020 Gueroult <gueroult@wasabi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# Code crée par MARC GUEROULT, sert à calculer les distances entre les ligands et les résidus.

import numpy as np
import MDAnalysis as mda
from MDAnalysis.analysis.base import AnalysisBase
import argparse, os


##### Function or object class to calculate distance between mass center#####

def dist(Sel1,Sel2, Box):
    """ calculate distance between 2 center of mass"""
    coord1 = Sel1.center_of_mass()
    coord2 = Sel2.center_of_mass()
    dist_sel = mda.lib.distances.distance_array(coord1, coord2, box=Box)
    return dist_sel[0][0]

class Distance_Com(AnalysisBase):
    def __init__(self, atomgroup1, atomgroup2, box=None, **kwargs):
        super(Distance_Com, self).__init__(atomgroup1.universe.trajectory,
                                           atomgroup2.universe.trajectory,         
                                           #dimensions.trajectory,
                                           **kwargs)
        self._ag1 = atomgroup1
        self._ag2 = atomgroup2
        self._box = box
    def _prepare(self):
        
        self.result = []

    def _single_frame(self):
        self.result.append(dist(self._ag1, self._ag2, self._box))
    
    def _conclude(self):
        self.data = np.array(self.result)
        self.mean = np.mean(self.result)
        self.sd = np.std(self.result)

##### Smoothing function ##################
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

####### Gestion des arguments ######
def valid(dir):
    if not os.path.exists(dir):
        raise argparse.ArgumentTypeError("%s is not a valid directory" % subdir)
    return dir

def isfile(path):
    """Check if path is an existing file. 
    If not, raise an error. Else, return the path."""
    if not os.path.isfile(path):
        if os.path.isdir(path):
            msg = "{0} is a directory".format(path)
        else:
            msg = "{0} does not exist.".format(path)
        raise argparse.ArgumentTypeError(msg)
    return path


def argt():
    """Define the script options."""
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-f", dest = "FilinXtc", \
                        help="xtc file",required = True, type = isfile)
    parser.add_argument("-s", dest = "FilinTpr", required = True, type = isfile,\
                        help =  "tpr file")
    parser.add_argument("--select1", dest = "sel1", required = True, type = str,\
                        help='selection 1')
    parser.add_argument("--select2", dest = "sel2", required = True, type = str,\
                        help='selection 2')
    args = parser.parse_args()

    return args



#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mda_MG.py
#  
#  Copyright 2020 Gueroult <gueroult@wasabi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# 

import numpy as np
import MDAnalysis as mda
import matplotlib.pyplot as plt
import argparse 

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

##### Function or object class to calculate distance between mass center#####

def dist(Sel1,Sel2, Box):
    """ calculate distance between 2 center of mass"""
    coord1 = Sel1.center_of_mass()
    coord2 = Sel2.center_of_mass()
    dist_sel = mda.lib.distances.distance_array(coord1, coord2, box=Box)
    return dist_sel[0][0]

class Distance_Com(AnalysisBase):
    def __init__(self, atomgroup1, atomgroup2, box=None, **kwargs):
        super(Distance_Com, self).__init__(atomgroup1.universe.trajectory,
                                           atomgroup2.universe.trajectory,         
                                           #dimensions.trajectory,
                                           **kwargs)
        self._ag1 = atomgroup1
        self._ag2 = atomgroup2
        self._box = box
    def _prepare(self):
        
        self.result = []

    def _single_frame(self):
        self.result.append(dist(self._ag1, self._ag2, self._box))
    
    def _conclude(self):
        self.data = np.array(self.result)
        self.mean = np.mean(self.result)
        self.sd = np.std(self.result)


####### Gestion des arguments ######
def valid(dir):
    if not os.path.exists(dir):
        raise argparse.ArgumentTypeError("%s is not a valid directory" % subdir)
    return dir

def isfile(path):
    """Check if path is an existing file. 
    If not, raise an error. Else, return the path."""
    if not os.path.isfile(path):
        if os.path.isdir(path):
            msg = "{0} is a directory".format(path)
        else:
            msg = "{0} does not exist.".format(path)
        raise argparse.ArgumentTypeError(msg)
    return path


def argt():
    """Define the script options."""
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-f", dest = "FilinXtc", \
                        help="xtc file",required = True, type = isfile)
    parser.add_argument("-s", dest = "FilinGro", required = True, type = isfile,\
                        help = "tpr file")
    parser.add_argument("--select1", dest = "sel1", required = True, type = str,\
                        help='selection 1')
    parser.add_argument("--select2", dest = "sel2", required = True, type = str,\
                        help='selection 2')
    parser.add_argument("-o", dest = "out", type = str, default = "figure.svg",\
                        help='image Name')
    args = parser.parse_args()

    return args

def main():
    """traitement des arguments d'entrée"""
    args = argt()
    filinGro = args.FilinGro
    filinXtc = args.FilinXtc
    Sel1 = args.sel1
    Sel2 = args.sel2
    FigName = args.out

    md = mda.Universe(filinGro, filinXtc)
    ligd = md.select_atoms(Sel1)
    prot = md.select_atoms(Sel2)

    resligd = []
    for resId in ligd.resids:
        if not resId in resligd:
           resligd.append(resId)

    dist_all = []
    for molid in resligd:
        lig_tmp = md.select_atoms("resid "+str(molid))
        dist_tmp = Distance_Com(lig_tmp, prot, box= md.dimensions ).run()
        dist_all.append(dist_tmp)

##### ploting part #####
    plt.figure()
    for i in range(len(resligd)):
        plt.plot(dist_all[i].times/1000, smooth(np.array(dist_all[i].data)), label = "ligand_"+str(resligd[i]))
    plt.legend()
    
    plt.xlabel("time (ns)")
    plt.ylabel(r"distance ($\AA$)")
    plt.ylim(0, 10)
    plt.savefig(FigName, format= "svg", dpi = 600)
if __name__ == '__main__':
        main()



