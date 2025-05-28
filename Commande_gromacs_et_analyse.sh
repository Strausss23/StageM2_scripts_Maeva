gmx make_ndx -f maeva.gro -o index.ndx
###
1 | 13
name 18 SOLU

14
name 19 MEMB

17 | 15 | 16
name 20 SOLV

18 | 19

q

[ r_68_&_SG ]
1092
[ r_192_&_NE2 ]
3089
[ CU241 ]
3885
[ CU242 ]
3886
[ r_188_&_SG ]
3034
[ r_72_&_NE2 ]
1147

###
rm -f \#*\
#gmx trjconv -s nvt.tpr -f nvt.xtc -o clean_nvt.gro -dump 100
####

###Step 1###

gmx grompp -f step6.0_minimization.mdp -c maeva.gro -r maeva.gro -p topol.top -o em_maeva.tpr
gmx mdrun -v -deffnm em_maeva
#&
gmx grompp -f step6.0_minimization.mdp -c step5_input.gro -r step5_input.gro -p topol.top -o em_step5.tpr
gmx mdrun -v -deffnm em_step5

###Step 2###
gmx grompp -f step6.1_equilibration.mdp -c em_maeva.gro -r em_maeva.gro -n index.ndx -p topol.top -o nvt_maeva.tpr
gmx mdrun -v -deffnm nvt_maeva
#&
gmx grompp -f step6.1_equilibration.mdp -c em_step5.gro -r em_step5.gro -n index.ndx -p topol.top -o nvt_step5.tpr
gmx mdrun -v -deffnm nvt_step5

###Step 3###
gmx grompp -f step6.2_equilibration.mdp -c nvt_maeva.gro -r nvt_maeva.gro -n index.ndx -p topol.top -o npt1_maeva.tpr
gmx mdrun -v -deffnm npt1_maeva
#&
gmx grompp -f step6.2_equilibration.mdp -c nvt_step5.gro -r nvt_step5.gro -n index.ndx -p topol.top -o npt1_step5.tpr
gmx mdrun -v -deffnm npt1_step5

###Step 4### 

gmx grompp -f step6.3_equilibration.mdp -c npt1_maeva.gro -r npt1_maeva.gro -n index.ndx -p topol.top -o npt2_maeva.tpr
gmx mdrun -v -deffnm npt2_maeva

### Step 5###
gmx grompp -f step6.0_minimization.mdp -c npt2_maeva.gro -r npt2_maeva.gro -p topol.top -o em_npt2.tpr
gmx mdrun -deffnm em_npt2

gmx grompp -f step6.4_equilibration.mdp -c npt2_maeva.gro -r npt2_maeva.gro -n index.ndx -p topol.top -o npt3_maeva.tpr
gmx mdrun -v -deffnm npt3_maeva
#

###
gmx grompp -f step6.5_equilibration.mdp -c npt3.gro -r npt3.gro -n index.ndx -p topol.top -o npt4.tpr
gmx mdrun -v -deffnm npt4
#

gmx grompp -f step6.6_equilibration.mdp -c npt4.gro -r npt4.gro -n index.ndx -p topol.top -o npt5.tpr
gmx mdrun -v -deffnm npt5
#

#gmx grompp -f step7.1pre_production.mdp -c npt5.gro -r npt5.gro -n index.ndx -p topol.top -o md.tpr -maxwarn 1
#gmx mdrun -v -deffnm md
#

gmx grompp -f step7.2_production.mdp -c npt5.gro -r npt5.gro -n index.ndx -p topol.top -o md_finale.tpr -maxwarn 1
gmx mdrun -v -deffnm md_finale




gmx grompp -f step7_production.mdp -c npt2_maeva.gro -r npt2_maeva.gro -n index.ndx -p topol.top -o md.tpr

gmx grompp -f step7_production.mdp -c npt2_maeva.gro -r npt2_maeva.gro -n index.ndx -p topol.top -o md.tpr


#############
##### ETHE
#############
gmx grompp -f minimization/step6.0_minimization.mdp -c ETR2_ETHE.gro -r ETR2_ETHE.gro -p topol.top -o minimization/em_ETHE1
gmx mdrun -v -deffnm minimization/em_ETHE1

gmx grompp -f equil1/step6.1_equilibration.mdp -c minimization/em_ETHE1.gro -r minimization/em_ETHE1.gro -p topol.top -n index.ndx -o equil1/eq1_ETHE1
gmx mdrun -v -deffnm equil1/eq1_ETHE1
xmgrace -nxy equil/eq1_ETHE1_pullx.xvg gmx grompp -f equil1/step6.1_equilibration.mdp -c minimization/em_ETHE1.gro -r minimization/em_ETHE1.gro -p topol.top -n index.ndx -o equil1/eq1_ETHE1
gmx mdrun -v -deffnm equil1/eq1_ETHE1
xmgrace -nxy equil/eq1_ETHE1_pullx.xvg 

gmx grompp -f equil2/step6.2_equilibration.mdp -c equil1/eq1_ETHE1.gro -r equil1/eq1_ETHE1.gro -p topol.top -n index.ndx -o equil2/eq2_ETHE1
gmx mdrun -v -deffnm equil2/eq2_ETHE1
xmgrace -nxy equil2/eq2_ETHE1_pullx.xvg 

gmx grompp -f equil3/step6.3_equilibration.mdp -c equil2/eq2_ETHE1.gro -r equil2/eq2_ETHE1.gro -p topol.top -n index.ndx -o equil3/eq3_ETHE1
gmx mdrun -v -deffnm equil3/eq3_ETHE1
xmgrace -nxy equil3/eq3_ETHE1_pullx.xvg 

gmx grompp -f equil4/step6.4_equilibration.mdp -c equil3/eq3_ETHE1.gro -r equil3/eq3_ETHE1.gro -p topol.top -n index.ndx -o equil4/eq4_ETHE1
gmx mdrun -v -deffnm equil4/eq4_ETHE1
xmgrace -nxy equil4/eq4_ETHE1_pullx.xvg 

gmx grompp -f prod_test/step7_production.mdp -c equil3/eq3_ETHE1.gro -r equil3/eq3_ETHE1.gro -n index.ndx -p topol.top -o prod_test/md_ETHE.tpr
gmx mdrun -v -deffnm prod_test/md_ETHE
xmgrace -nxy prod_test/md_ETHE_pullx.xvg 

gmx grompp -f prod_1us/step7_production.mdp -c equil3/eq3_ETHE1.gro -r equil3/eq3_ETHE1.gro -n index.ndx -p topol.top -o prod_1us/md_ETHE_1us.tpr


#############
##### ETOH
#############
gmx grompp -f minimization/step6.0_minimization.mdp -c ETR2_ETOH.gro -r ETR2_ETOH.gro -p topol.top -o minimization/em_ETOH
gmx mdrun -v -deffnm minimization/em_ETOH

gmx grompp -f equil1/step6.1_equilibration.mdp -c minimization/em_ETOH.gro -r minimization/em_ETOH.gro -p topol.top -n index.ndx -o equil1/eq1_ETOH
gmx mdrun -v -deffnm equil1/eq1_ETOH
xmgrace -nxy equil1/eq1_ETOH_pullx.xvg 

gmx grompp -f equil2/step6.2_equilibration.mdp -c equil1/eq1_ETOH.gro -r equil1/eq1_ETOH.gro -p topol.top -n index.ndx -o equil2/eq2_ETOH
gmx mdrun -v -deffnm equil2/eq2_ETOH
xmgrace -nxy equil2/eq2_ETOH_pullx.xvg 

gmx grompp -f equil3/step6.3_equilibration.mdp -c equil2/eq2_ETOH.gro -r equil2/eq2_ETOH.gro -p topol.top -n index.ndx -o equil3/eq3_ETOH
gmx mdrun -v -deffnm equil3/eq3_ETOH
xmgrace -nxy equil3/eq3_ETOH_pullx.xvg 

gmx grompp -f prod_test/step7_production.mdp -c equil3/eq3_ETOH.gro -r equil3/eq3_ETOH.gro -n index.ndx -p topol.top -o prod_test/md_ETOH.tpr
gmx mdrun -v -deffnm prod_test/md_ETOH
xmgrace -nxy prod_test/md_ETOH_pullx.xvg 

gmx grompp -f prod_1us/step7_production.mdp -c equil3/eq3_ETOH.gro -r equil3/eq3_ETOH.gro -n index.ndx -p topol.top -o prod_1us/md_ETOH_1us.tpr


####################
#### ETHE & ETOH
####################
gmx grompp -f minimization/step6.0_minimization.mdp -c ETR2_ETHE_ETOH.gro -r ETR2_ETHE_ETOH.gro -p topol.top -o minimization/em__ETHE_ETOH
gmx mdrun -v -deffnm minimization/em_ETHE_ETOH

gmx grompp -f equil1/step6.1_equilibration.mdp -c minimization/em_ETHE_ETOH.gro -r minimization/em_ETHE_ETOH.gro -p topol.top -n index.ndx -o equil1/eq1_ETHE_ETOH
gmx mdrun -v -deffnm equil1/eq1_ETHE_ETOH
xmgrace -nxy equil1/eq1_ETHE_ETOH_pullx.xvg 

gmx grompp -f equil2/step6.2_equilibration.mdp -c equil1/eq1_ETHE_ETOH.gro -r equil1/eq1_ETHE_ETOH.gro -p topol.top -n index.ndx -o equil2/eq2_ETHE_ETOH
gmx mdrun -v -deffnm equil2/eq2_ETHE_ETOH
xmgrace -nxy equil2/eq2_ETHE_ETOH_pullx.xvg 

gmx grompp -f equil3/step6.3_equilibration.mdp -c equil2/eq2_ETHE_ETOH.gro -r equil2/eq2_ETHE_ETOH.gro -p topol.top -n index.ndx -o equil3/eq3_ETHE_ETOH
gmx mdrun -v -deffnm equil3/eq3_ETHE_ETOH
xmgrace -nxy equil3/eq3_ETHE_ETOH_pullx.xvg 

gmx grompp -f prod_test/step7_production.mdp -c equil3/eq3_ETHE_ETOH.gro -r equil3/eq3_ETHE_ETOH.gro -n index.ndx -p topol.top -o prod_test/md_ETHE_ETOH.tpr
gmx mdrun -v -deffnm prod_test/md_ETHE_ETOH
xmgrace -nxy prod_test/md_ETHE_ETOH_pullx.xvg 

gmx grompp -f prod_1us/step7_production.mdp -c equil3/eq3_ETHE_ETOH.gro -r equil3/eq3_ETHE_ETOH.gro -n index.ndx -p topol.top -o prod_1us/md_ETHE_ETOH_1us.tpr



#############################################
#### Supression conditions périodiques
#############################################
#L'idée principale est de "corriger" les trajectoires pour que les molécules ou les complexes 
#ne soient pas artificiellement séparés à cause des bords de la boîte périodique.

# 1. Corriger les sauts d'abord
echo -e "0" | gmx trjconv -s alone/md_VvETR2_1us.tpr -f alone/md_VvETR2_1us.xtc -o alone/md_VvETR2_1us_nojump.xtc -pbc nojump
echo -e "0" | gmx trjconv -s ethylene/md_ETHE_1us.tpr -f ethylene/md_ETHE_1us.xtc -o ethylene/md_ETHE_1us_nojump.xtc -pbc nojump
echo -e "0" | gmx trjconv -s ethanol/md_ETOH_1us.tpr -f ethanol/md_ETOH_1us.xtc -o ethanol/md_ETOH_1us_nojump.xtc -pbc nojump
echo -e "0" | gmx trjconv -s both/md_ETHE_ETOH_1us.tpr -f both/md_ETHE_ETOH_1us.xtc -o both/md_ETHE_ETOH_1us_nojump.xtc -pbc nojump
# systeme

# 2. Centrer la protéine (très important AVANT le reemboîtage)
echo -e " 1" "0" | gmx trjconv -s alone/md_VvETR2_1us.tpr -f alone/md_VvETR2_1us_nojump.xtc -o alone/md_VvETR2_1us_center.xtc -center
echo -e " 1" "0" | gmx trjconv -s ethylene/md_ETHE_1us.tpr -f ethylene/md_ETHE_1us_nojump.xtc -o ethylene/md_ETHE_1us_center.xtc -center
echo -e " 1" "0" | gmx trjconv -s ethanol/md_ETOH_1us.tpr -f ethanol/md_ETOH_1us_nojump.xtc -o ethanol/md_ETOH_1us_center.xtc -center
echo -e " 1" "0" | gmx trjconv -s  both/md_ETHE_ETOH_1us.tpr -f both/md_ETHE_ETOH_1us_nojump.xtc -o both/md_ETHE_ETOH_1us_center.xtc -center


# 3. Réemboîter membrane + protéine
echo -e "0" | gmx trjconv -s alone/md_VvETR2_1us.tpr -f alone/md_VvETR2_1us_center.xtc -o alone/md_VvETR2_1us_final.xtc -pbc mol -ur compact
echo -e "0" | gmx trjconv -s ethylene/md_ETHE_1us.tpr -f ethylene/md_ETHE_1us_center.xtc -o ethylene/md_ETHE_1us_final.xtc -pbc mol -ur compact
echo -e "0" | gmx trjconv -s ethanol/md_ETOH_1us.tpr -f ethanol/md_ETOH_1us_center.xtc -o ethanol/md_ETOH_1us_final.xtc -pbc mol -ur compact
echo -e "0" | gmx trjconv -s both/md_ETHE_ETOH_1us.tpr -f both/md_ETHE_ETOH_1us_center.xtc -o both/md_ETHE_ETOH_1us_final.xtc -pbc mol -ur compact
#systeme

### TOUT TESTER ###
vmd alone/md_VvETR2_1us.gro alone/md_VvETR2_1us_final.xtc
vmd ethylene/md_ETHE_1us.gro ethylene/md_ETHE_1us_final.xtc
vmd ethanol/md_ETOH_1us.gro ethanol/md_ETOH_1us_final.xtc
vmd both/md_ETHE_ETOH_1us.gro both/md_ETHE_ETOH_1us_final.xtc

###############
#### RMSD
###############
gmx make_ndx -f  alone/md_VvETR2_1us.tpr -o alone/helices.ndx
gmx make_ndx -f  ethylene/md_ETHE_1us.tpr -o ethylene/helices.ndx
gmx make_ndx -f  ethanol/md_ETOH_1us.tpr -o ethanol/helices.ndx
gmx make_ndx -f  both/md_ETHE_ETOH_1us.tpr -o both/helices.ndx
r 18-49 | r 55-77 | r 84-118
name 19 HELICES
q

#protein
echo -e "1" "1" | gmx rms -s alone/md_VvETR2_1us.tpr -f alone/md_VvETR2_1us_final.xtc -o alone/rmsd_VvETR2.xvg
echo -e "1" "1" | gmx rms -s ethylene/md_ETHE_1us.tpr -f ethylene/md_ETHE_1us_final.xtc -o ethylene/rmsd_ETHE.xvg
echo -e "1" "1" | gmx rms -s ethanol/md_ETOH_1us.tpr -f ethanol/md_ETOH_1us_final.xtc -o ethanol/rmsd_ETOH.xvg
echo -e "1" "1" | gmx rms -s both/md_ETHE_ETOH_1us.tpr -f both/md_ETHE_ETOH_1us_final.xtc -o both/rmsd_both.xvg


echo -e "3" "3" | gmx rms -s alone/md_VvETR2_1us.tpr -f alone/md_VvETR2_1us_final.xtc -n alone/helices.ndx -o alone/rmsd_ETR2Calpha.xvg
echo -e "3" "3" | gmx rms -s ethylene/md_ETHE_1us.tpr -f ethylene/md_ETHE_1us_final.xtc -n ethylene/helices.ndx -o ethylene/rmsd_ETHECalpha.xvg
echo -e "3" "3" | gmx rms -s ethanol/md_ETOH_1us.tpr -f ethanol/md_ETOH_1us_final.xtc -n ethanol/helices.ndx -o ethanol/rmsd_ETOHCalpha.xvg
echo -e "3" "3" | gmx rms -s both/md_ETHE_ETOH_1us.tpr -f both/md_ETHE_ETOH_1us_final.xtc -n both/helices.ndx -o both/rmsd_bothCalpha.xvg


echo -e "18" "18"| gmx rms -s alone/md_VvETR2_1us.tpr -f alone/md_VvETR2_1us_final.xtc -n alone/helices.ndx -o alone/rmsd_ETR2_helices.xvg
echo -e "19" "19"| gmx rms -s ethylene/md_ETHE_1us.tpr -f ethylene/md_ETHE_1us_final.xtc -n ethylene/helices.ndx -o ethylene/rmsd_ETHE_helices.xvg
echo -e "19" "19"| gmx rms -s ethanol/md_ETOH_1us.tpr -f ethanol/md_ETOH_1us_final.xtc -n ethanol/helices.ndx -o ethanol/rmsd_ETOH_helices.xvg
echo -e "20" "20"| gmx rms -s both/md_ETHE_ETOH_1us.tpr -f both/md_ETHE_ETOH_1us_final.xtc -n both/helices.ndx -o both/rmsd_both_helices.xvg

#!/bin/bash

for file in alone/rmsd_VvETR2.xvg ethylene/rmsd_ETHE.xvg ethanol/rmsd_ETOH.xvg both/rmsd_both.xvg alone/rmsd_ETR2Calpha.xvg ethylene/rmsd_ETHECalpha.xvg ethanol/rmsd_ETOHCalpha.xvg both/rmsd_bothCalpha.xvg alone/rmsd_ETR2_helices.xvg ethylene/rmsd_ETHE_helices.xvg ethanol/rmsd_ETOH_helices.xvg both/rmsd_both_helices.xvg; do
    out="${file%.xvg}_ns.xvg"
    awk '$1 ~ /^@/ || $1 ~ /^#/ {print} $1 !~ /^[@#]/ {printf "%.6f %s\n", $1/1000, $2}' "$file" > "$out"
    echo "✔ Fichier converti : $out"
done

xmgrace alone/rmsd_VvETR2_ns.xvg ethylene/rmsd_ETHE_ns.xvg ethanol/rmsd_ETOH_ns.xvg both/rmsd_both_ns.xvg
#RMSD evolution of all protein atoms of protein VvETR2 under different experimental conditions

xmgrace alone/rmsd_ETR2Calpha_ns.xvg ethylene/rmsd_ETHECalpha_ns.xvg ethanol/rmsd_ETOHCalpha_ns.xvg both/rmsd_bothCalpha_ns.xvg
#RMSD evolution of C-alpha atoms of protein VvETR2 across different experimental conditions 

xmgrace alone/rmsd_ETR2_helices_ns.xvg ethylene/rmsd_ETHE_helices_ns.xvg ethanol/rmsd_ETOH_helices_ns.xvg both/rmsd_both_helices_ns.xvg
#RMSD evolution of atoms in the helical region of protein VvETR2 under different experimental conditions


#####################
#### RMSD SMOOTH #### 
#####################
echo -e "3" "3" | gmx rms -s alone/md_VvETR2_1us.tpr -f alone/alone_smooth.xtc -n alone/helices.ndx -o alone/rmsd_ETR2Calpha_smooth.xvg
echo -e "3" "3" | gmx rms -s ethylene/md_ETHE_1us.tpr -f ethylene/ETHE_smooth.xtc -n ethylene/helices.ndx -o ethylene/rmsd_ETHECalpha_smooth.xvg
echo -e "3" "3" | gmx rms -s ethanol/md_ETOH_1us.tpr -f ethanol/ETOH_smooth.xtc -n ethanol/helices.ndx -o ethanol/rmsd_ETOHCalpha_smooth.xvg
echo -e "3" "3" | gmx rms -s both/md_ETHE_ETOH_1us.tpr -f both/BOTH_smooth.xtc -n both/helices.ndx -o both/rmsd_bothCalpha_smooth.xvg

echo -e "18" "18"| gmx rms -s alone/md_VvETR2_1us.tpr -f alone/alone_smooth.xtc -n alone/helices.ndx -o alone/rmsd_ETR2_helices_smooth.xvg
echo -e "19" "19"| gmx rms -s ethylene/md_ETHE_1us.tpr -f ethylene/ETHE_smooth.xtc -n ethylene/helices.ndx -o ethylene/rmsd_ETHE_helices_smooth.xvg
echo -e "19" "19"| gmx rms -s ethanol/md_ETOH_1us.tpr -f ethanol/ETOH_smooth.xtc -n ethanol/helices.ndx -o ethanol/rmsd_ETOH_helices_smooth.xvg
echo -e "20" "20"| gmx rms -s both/md_ETHE_ETOH_1us.tpr -f both/BOTH_smooth.xtc -n both/helices.ndx -o both/rmsd_both_helices_smooth.xvg

### METTRE EN ns
for file in alone/rmsd_ETR2Calpha_smooth.xvg ethylene/rmsd_ETHECalpha_smooth.xvg ethanol/rmsd_ETOHCalpha_smooth.xvg both/rmsd_bothCalpha_smooth.xvg alone/rmsd_ETR2_helices_smooth.xvg ethylene/rmsd_ETHE_helices_smooth.xvg ethanol/rmsd_ETOH_helices_smooth.xvg both/rmsd_both_helices_smooth.xvg; do
    out="${file%.xvg}_ns.xvg"
    awk '$1 ~ /^@/ || $1 ~ /^#/ {print} $1 !~ /^[@#]/ {printf "%.6f %s\n", $1/1000, $2}' "$file" > "$out"
    echo "✔ Fichier converti : $out"
done

xmgrace alone/rmsd_ETR2Calpha_smooth_ns.xvg ethylene/rmsd_ETHECalpha_smooth_ns.xvg ethanol/rmsd_ETOHCalpha_smooth_ns.xvg both/rmsd_bothCalpha_smooth_ns.xvg
#RMSD evolution of C-alpha atoms of protein VvETR2 across different experimental conditions, from smoothed trajectories

xmgrace alone/rmsd_ETR2_helices_smooth_ns.xvg ethylene/rmsd_ETHE_helices_smooth_ns.xvg ethanol/rmsd_ETOH_helices_smooth_ns.xvg both/rmsd_both_helices_smooth_ns.xvg
#RMSD evolution of atoms in the helical region of protein VvETR2 under different experimental conditions, from smoothed trajectories

###############
#### RMSF
###############
#carbone alpha
echo -e "3" "3" | gmx rmsf -s alone/md_VvE

#prot
echo -e "1" "1" | gmx rmsf -s alone/md_VvETR2_1us.tpr -f alone/md_VvETR2_1us_final.xtc -o alone/rmsf_VvETR2_prot.xvg -res
echo -e "1" "1" | gmx rmsf -s ethylene/md_ETHE_1us.tpr -f ethylene/md_ETHE_1us_final.xtc -o ethylene/rmsf_ETHE_prot.xvg -res
echo -e "1" "1" | gmx rmsf -s ethanol/md_ETOH_1us.tpr -f ethanol/md_ETOH_1us_final.xtc -o ethanol/rmsf_ETOH_prot.xvg -res
echo -e "1" "1" | gmx rmsf -s both/md_ETHE_ETOH_1us.tpr -f both/md_ETHE_ETOH_1us_final.xtc -o both/rmsf_both_prot.xvg -res

xmgrace alone/rmsf_VvETR2_prot.xvg ethylene/rmsf_ETHE_prot.xvg ethanol/rmsf_ETOH_prot.xvg both/rmsf_both_prot.xvg
#RMSF of all protein atoms of VvETR2 across different experimental conditions

#helices 
echo -e "18" "18" | gmx rmsf -s alone/md_VvETR2_1us.tpr -f alone/md_VvETR2_1us_final.xtc -n alone/helices.ndx -o alone/rmsf_VvETR2_helix.xvg -res
echo -e "19" "19" | gmx rmsf -s ethylene/md_ETHE_1us.tpr -f ethylene/md_ETHE_1us_final.xtc -n ethylene/helices.ndx -o ethylene/rmsf_ETHE_helix.xvg -res
echo -e "19" "19" | gmx rmsf -s ethanol/md_ETOH_1us.tpr -f ethanol/md_ETOH_1us_final.xtc -n ethanol/helices.ndx -o ethanol/rmsf_ETOH_helix.xvg -res
echo -e "20" "20" | gmx rmsf -s both/md_ETHE_ETOH_1us.tpr -f both/md_ETHE_ETOH_1us_final.xtc -n both/helices.ndx -o both/rmsf_both_helix.xvg -res

xmgrace alone/rmsf_VvETR2_helix.xvg ethylene/rmsf_ETHE_helix.xvg ethanol/rmsf_ETOH_helix.xvg both/rmsf_both_helix.xvg

#### HOLE ####
#echo -e "1" | gmx trjconv -s ethanol/md_ETOH_1us.tpr -f ethanol/md_ETOH_1us_final.xtc -o hole/frame_.pdb -sep -skip 20


#####################
#### DIFFUSION MB 
#####################

### Def boite proteine
# Sélection de la protéine
set sel [atomselect top "protein"]
set minmax [measure minmax $sel]
set min [lindex $minmax 0]
set max [lindex $minmax 1]

# Extraire les coordonnées
set xmin [lindex $min 0]
set ymin [lindex $min 1]
set zmin [lindex $min 2]
set xmax [lindex $max 0]
set ymax [lindex $max 1]
set zmax [lindex $max 2]

# Définir les coins de la boîte
set p1 [list $xmin $ymin $zmin]
set p2 [list $xmax $ymin $zmin]
set p3 [list $xmin $ymax $zmin]
set p4 [list $xmax $ymax $zmin]
set p5 [list $xmin $ymin $zmax]
set p6 [list $xmax $ymin $zmax]
set p7 [list $xmin $ymax $zmax]
set p8 [list $xmax $ymax $zmax]

# Couleur rouge
draw color red

# Dessiner les 12 arêtes
draw line $p1 $p2
draw line $p1 $p3
draw line $p1 $p5

draw line $p2 $p4
draw line $p2 $p6

draw line $p3 $p4
draw line $p3 $p7

draw line $p4 $p8

draw line $p5 $p6
draw line $p5 $p7

draw line $p6 $p8
draw line $p7 $p8

##On réduit
# Sélection de la protéine
set sel [atomselect top "protein"]
set minmax [measure minmax $sel]
set min [lindex $minmax 0]
set max [lindex $minmax 1]

# Extraire les coordonnées
set xmin [lindex $min 0]
set ymin [lindex $min 1]
set zmin [lindex $min 2]
set xmax [lindex $max 0]
set ymax [lindex $max 1]
set zmax [lindex $max 2]

# Réduction : plus grand padding = boîte plus serrée
set padding 12.0

set xmin [expr $xmin + $padding]
set ymin [expr $ymin + $padding]
set zmin [expr $zmin + $padding]
set xmax [expr $xmax - $padding]
set ymax [expr $ymax - $padding]
set zmax [expr $zmax - $padding]

# Coins de la boîte
set p1 [list $xmin $ymin $zmin]
set p2 [list $xmax $ymin $zmin]
set p3 [list $xmin $ymax $zmin]
set p4 [list $xmax $ymax $zmin]
set p5 [list $xmin $ymin $zmax]
set p6 [list $xmax $ymin $zmax]
set p7 [list $xmin $ymax $zmax]
set p8 [list $xmax $ymax $zmax]

draw color pink

# Arêtes de la boîte
draw line $p1 $p2
draw line $p1 $p3
draw line $p1 $p5echo -e "0" | gmx trjconv -s ethanol/md_ETOH_1us.tpr -f ethanol/md_ETOH_1us_center.xtc -o ethanol/md_ETOH_1us_final.xtc -pbc mol -ur compact
echo -e "0" | gmx trjconv -s both/md_ETHE_ETOH_1us.tpr -f both/md_ETHE_ETOH_1us_center.xtc -o both/md_ETHE_ETOH_1us_final.xtc -pbc mol -ur compact


draw line $p2 $p4
draw line $p2 $p6

draw line $p3 $p4
draw line $p3 $p7

draw line $p4 $p8

draw line $p5 $p6
draw line $p5 $p7

draw line $p6 $p8
draw line $p7 $p8

####
X : de 18.58 à 60.36

Y : de 21.40 à 57.54

Z : de 20.68 à 92.10
####


#test ethanol 
gmx make_ndx -f ethanol/md_ETOH_1us.tpr -o ethanol/ethanol_only.ndx

echo -e "19" | gmx traj -s ethanol/md_ETOH_1us.tpr -f ethanol/md_ETOH_1us_final.xtc -n ethanol/ethanol_only.ndx -ox ethanol/ethanol_z1.xvg -com -ng 1
echo -e "20" | gmx traj -s ethanol/md_ETOH_1us.tpr -f ethanol/md_ETOH_1us_final.xtc -n ethanol/ethanol_only.ndx -ox ethanol/ethanol_z2.xvg -com -ng 1
echo -e "21" | gmx traj -s ethanol/md_ETOH_1us.tpr -f ethanol/md_ETOH_1us_final.xtc -n ethanol/ethanol_only.ndx -ox ethanol/ethanol_z3.xvg -com -ng 1
echo -e "22" | gmx traj -s ethanol/md_ETOH_1us.tpr -f ethanol/md_ETOH_1us_final.xtc -n ethanol/ethanol_only.ndx -ox ethanol/ethanol_z4.xvg -com -ng 1
echo -e "23" | gmx traj -s ethanol/md_ETOH_1us.tpr -f ethanol/md_ETOH_1us_final.xtc -n ethanol/ethanol_only.ndx -ox ethanol/ethanol_z5.xvg -com -ng 1
echo -e "24" | gmx traj -s ethanol/md_ETOH_1us.tpr -f ethanol/md_ETOH_1us_final.xtc -n ethanol/ethanol_only.ndx -ox ethanol/ethanol_z6.xvg -com -ng 1
echo -e "25" | gmx traj -s ethanol/md_ETOH_1us.tpr -f ethanol/md_ETOH_1us_final.xtc -n ethanol/ethanol_only.ndx -ox ethanol/ethanol_z7.xvg -com -ng 1
echo -e "26" | gmx traj -s ethanol/md_ETOH_1us.tpr -f ethanol/md_ETOH_1us_final.xtc -n ethanol/ethanol_only.ndx -ox ethanol/ethanol_z8.xvg -com -ng 1
echo -e "27" | gmx traj -s ethanol/md_ETOH_1us.tpr -f ethanol/md_ETOH_1us_final.xtc -n ethanol/ethanol_only.ndx -ox ethanol/ethanol_z9.xvg -com -ng 1
echo -e "28" | gmx traj -s ethanol/md_ETOH_1us.tpr -f ethanol/md_ETOH_1us_final.xtc -n ethanol/ethanol_only.ndx -ox ethanol/ethanol_z10.xvg -com -ng 1

#apres les trajectoires, on applique le code python Suivre DeltaZ

#pour ethylène : 
gmx make_ndx -f ethylene/md_ETHE_1us.tpr -o ethylene/ethylene_only.ndx

      0 System              : 72261 atoms
      1 Protein             :  3884 atoms
      2 Protein-H           :  1920 atoms
      3 C-alpha             :   240 atoms
      4 Backbone            :   720 atoms
      5 MainChain           :   958 atoms
      6 MainChain+Cb        :  1190 atoms
      7 MainChain+H         :  1184 atoms
      8 SideChain           :  2700 atoms
      9 SideChain-H         :   962 atoms
      10 Prot-Masses         :  3884 atoms
      11 non-Protein         : 68377 atoms
      12 Other               : 68377 atoms
      13 CU2P                :     2 atoms
      14 DOPC                : 22080 atoms
      15 POT                 :    29 atoms
      16 CLA                 :    27 atoms
      17 TIP3                : 46179 atoms
      18 ETHE                :    60 atoms
      19 r_15852             :     6 atoms
      20 r_15853             :     6 atoms
      21 r_15854             :     6 atoms
      22 r_15855             :     6 atoms
      23 r_15856             :     6 atoms
      24 r_15857             :     6 atoms
      25 r_15858             :     6 atoms
      26 r_15859             :     6 atoms
      27 r_15860             :     6 atoms
      28 r_15861             :     6 atoms


for i in {19..28}; do
  outfile="ethylene/ethylene_z$((i-18)).xvg"
  echo -e "$i" | gmx traj -s ethylene/md_ETHE_1us.tpr -f ethylene/md_ETHE_1us_final.xtc -n ethylene/ethylene_only.ndx -ox "$outfile" -com -ng 1
done

###Pour les deux : 
gmx make_ndx -f both/md_ETHE_ETOH_1us.tpr -o both/ethanol_only.ndx
gmx make_ndx -f both/md_ETHE_ETOH_1us.tpr -o both/ethylene_only.ndx

for i in {20..29}; do
  outfile="both/trajetZ/ethylene_z$((i-19)).xvg"
  echo -e "$i" | gmx traj -s  both/md_ETHE_ETOH_1us.tpr -f both/md_ETHE_ETOH_1us_final.xtc -n both/ethylene_only.ndx -ox "$outfile" -com -ng 1
done

for i in {20..29}; do
  outfile="both/trajetZ/ethanol_z$((i-19)).xvg"
  echo -e "$i" | gmx traj -s  both/md_ETHE_ETOH_1us.tpr -f both/md_ETHE_ETOH_1us_final.xtc -n both/ethanol_only.ndx -ox "$outfile" -com -ng 1
done


#####################
#### Distances
#####################

#!/bin/bash

# Fichiers d'entrée
XTC="ethanol/md_ETOH_1us_final.xtc"
TPR="ethanol/md_ETOH_1us.tpr"
SCRIPT="/home/mabadielim/Desktop/script/dist_Maeva.py"
OUTDIR="ethanol/all_distances"
mkdir -p "$OUTDIR"

# Boucle sur les résidus (de 1 à 240)
for resid in $(seq 1 2); do
    OUTFILE="${OUTDIR}/resid_${resid}_allethanol.svg"
    echo "Processing resid $resid..."
    python3 "$SCRIPT" -f "$XTC" -s "$TPR" --select1 "resname ETHE" --select2 "resid $resid" -o "$OUTFILE"
done

#ethylene
python3 ~/Desktop/script/dist_Maeva.py -f ethylene/md_ETHE_1us_final.xtc -s ethylene/md_ETHE_1us.tpr --select1 "resname ETHE" --select2 "resid 36" -o ethylene/SiteA36_allethylene.svg
python3 ~/Desktop/script/dist_Maeva.py -f ethylene/md_ETHE_1us_final.xtc -s ethylene/md_ETHE_1us.tpr --select1 "resname ETHE" --select2 "resid 156" -o ethylene/SiteB156_allethylene.svg

python3 ~/Desktop/script/dist_Maeva.py -f ethylene/md_ETHE_1us_final.xtc -s ethylene/md_ETHE_1us.tpr --select1 "resname ETHE" --select2 "resid 94" -o ethylene/K94_A_allethylene.svg
python3 ~/Desktop/script/dist_Maeva.py -f ethylene/md_ETHE_1us_final.xtc -s ethylene/md_ETHE_1us.tpr --select1 "resname ETHE" --select2 "resid 214" -o ethylene/K94_B_allethylene.svg

python3 ~/Desktop/script/dist_Maeva.py -f ethylene/md_ETHE_1us_final.xtc -s ethylene/md_ETHE_1us.tpr --select1 "resname ETHE" --select2 "resid 29" -o ethylene/D29_A_allethylene.svg
python3 ~/Desktop/script/dist_Maeva.py -f ethylene/md_ETHE_1us_final.xtc -s ethylene/md_ETHE_1us.tpr --select1 "resname ETHE" --select2 "resid 149" -o ethylene/D29_B_allethylene.svg

python3 ~/Desktop/script/dist_Maeva.py -f ethylene/md_ETHE_1us_final.xtc -s ethylene/md_ETHE_1us.tpr --select1 "resname ETHE" --select2 "resid 48" -o ethylene/S48_A_allethylene.svg
python3 ~/Desktop/script/dist_Maeva.py -f ethylene/md_ETHE_1us_final.xtc -s ethylene/md_ETHE_1us.tpr --select1 "resname ETHE" --select2 "resid 168" -o ethylene/S48_B_allethylene.svg

###J'ai fait les plus important à la main, mtn j'automatise#

#### ETHYLENE ####

# Fichiers d'entrée
XTC="ethylene/md_ETHE_1us_final.xtc"
TPR="ethylene/md_ETHE_1us.tpr"
SCRIPT="/home/mabadielim/Desktop/script/dist_Maeva.py"
OUTDIR="ethylene/Smooth_all_distances"
mkdir -p "$OUTDIR"

# Boucle sur les résidus (de 1 à 240)
for resid in $(seq 1 240); do
    OUTFILE="${OUTDIR}/resid_${resid}_allethylene.svg"
    echo "Processing resid $resid..."
    python3 "$SCRIPT" -f "$XTC" -s "$TPR" --select1 "resname ETHE" --select2 "resid $resid" -o "$OUTFILE"
done

#### ETHANOL ####

# Fichiers d'entrée
XTC="ethanol/md_ETOH_1us_final.xtc"
TPR="ethanol/md_ETOH_1us.tpr"
SCRIPT="/home/mabadielim/Desktop/script/dist_Maeva.py"
OUTDIR="ethanol/Smooth_all_distances"
mkdir -p "$OUTDIR"

# Boucle sur les résidus (de 1 à 240)
for resid in $(seq 1 240); do
    OUTFILE="${OUTDIR}/resid_${resid}_allethanol.svg"
    echo "Processing resid $resid..."
    python3 "$SCRIPT" -f "$XTC" -s "$TPR" --select1 "resname ETOH" --select2 "resid $resid" -o "$OUTFILE"
done

#### BOTH ####

XTC="both/md_ETHE_ETOH_1us_final.xtc"
TPR="both/md_ETHE_ETOH_1us.tpr"
SCRIPT="/home/mabadielim/Desktop/script/dist_Maeva.py"
OUTDIR="both/Smooth_ETHE_all_distances"
mkdir -p "$OUTDIR"

# Boucle sur les résidus (de 1 à 240)
for resid in $(seq 1 240); do
    OUTFILE="${OUTDIR}/resid_${resid}_allethylene.svg"
    echo "Processing resid $resid..."
    python3 "$SCRIPT" -f "$XTC" -s "$TPR" --select1 "resname ETHE" --select2 "resid $resid" -o "$OUTFILE"
done

XTC="both/md_ETHE_ETOH_1us_final.xtc"
TPR="both/md_ETHE_ETOH_1us.tpr"
SCRIPT="/home/mabadielim/Desktop/script/dist_Maeva.py"
OUTDIR="both/Smooth_ETOH_all_distances"
mkdir -p "$OUTDIR"

# Boucle sur les résidus (de 1 à 240)
for resid in $(seq 1 240); do
    OUTFILE="${OUTDIR}/resid_${resid}_allethanol.svg"
    echo "Processing resid $resid..."
    python3 "$SCRIPT" -f "$XTC" -s "$TPR" --select1 "resname ETOH" --select2 "resid $resid" -o "$OUTFILE"
done

#### MATRICE SMOOTH ###
