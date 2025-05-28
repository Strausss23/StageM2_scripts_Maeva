#Ce script prend les MSA de AF2 et cherche les organismes qui sompose ce MSA

#################
#### Library ####
#################

import re
import requests
import time

###################
#### fonctions ####
###################
def extract_uniprot_ids(msa_file):
    with open(msa_file, "r") as file:
        content = file.read()
    
    # Trouver les identifiants UniProt (UniRef100 et UPI)
    uniprot_ids = set(re.findall(r'UniRef100_[A-Z0-9]+|UPI[0-9A-Z]+', content))
    return list(uniprot_ids)

def fetch_info(uniprot_id):
    base_url = "https://rest.uniprot.org/uniref/"
    response = requests.get(f"{base_url}{uniprot_id}", headers={"Accept": "application/json"})
    
    if response.status_code == 200:
        data = response.json()
        organism_name = data.get("representativeMember", {}).get("organismName", "Organisme inconnu")
        protein_name = data.get("representativeMember", {}).get("proteinName", "Protéine inconnue")
        return organism_name, protein_name
    return "Organisme inconnu", "Protéine inconnue"

def main(msa_file):
    uniprot_ids = extract_uniprot_ids(msa_file)
    print(f"{len(uniprot_ids)} identifiants UniProt trouvés. Récupération des noms d'organismes...")
    n = 0
    output_text = ""
    output_file = "/home/mabadielim/Desktop/msa_result"

    for uniprot_id in uniprot_ids:
        organism_name, protein_name = fetch_info(uniprot_id)
        n = n +1
        print(n,' : ', organism_name, ' : ', protein_name)
        output_text += (organism_name) + "  :  " + (protein_name) + "\n" 
        time.sleep(0.5)  
    
    with open(output_file, "w") as f:
        f.write(output_text)

##############
#### CODE ####
##############

if __name__ == "__main__":
    msa_file = "/home/mabadielim/Desktop/msa_af2.a3m"  
    main(msa_file)



