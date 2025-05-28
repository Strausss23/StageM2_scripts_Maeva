#Mesurer la distance entre un atome de liaison de cuivre et le cuivre en fonction du temps. 

#################
#### Library ####
#################

import matplotlib.pyplot as plt

time = []
distance = []

with open("/home/mabadielim/Desktop/Charmm/Cu2p_dupc/charmm-gui-4302665021/gromacs/dist2_188.xvg") as f:
    for line in f:
        if line.startswith(("#", "@")):
            continue
        t, d = map(float, line.split())
        time.append(t)
        distance.append(d)

plt.plot(time, distance)
plt.xlabel("Time (ps)")
plt.ylabel("Distance (nm)")
plt.title("Distance CU242 – SG188 over time")
plt.grid(True)
plt.tight_layout()
plt.show()
