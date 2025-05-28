#Observe quelles séquences MSA aide à la construction des modèles. 

nb_lignes = 0
ETR = 0 
histidine_kinase = 0
ETR_organism = ""
HK_organism = ""
input_file = "/home/mabadielim/Desktop/msa_result"
output_file = "/home/mabadielim/Desktop/msa_onlyHK"

with open(input_file, "r") as fichier:
    for ligne in fichier:  
        a = ligne.lower()
        nb_lignes += 1
        if "ethylene receptor" in a :
            ETR_organism += a + "\n"
            ETR += 1
        elif "histidine kinase" in a :
            histidine_kinase += 1
            HK_organism += a + "\n"
    
percentETR = ETR/nb_lignes *100
percentHK = histidine_kinase/nb_lignes *100
percentAutre = (nb_lignes-ETR-histidine_kinase)/nb_lignes *100
S = percentAutre + percentETR + percentHK

with open(output_file,"w") as f :
    f.write(HK_organism) 

print(f'Le pourcentage de ETR qui ont servi à AF2 est de {percentETR}% Il y en a {ETR}. \nLe pourcentage de HK est de {percentHK} %  Il y en a {histidine_kinase}. \nLe pourcentage du reste est de {percentAutre}.')