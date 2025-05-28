#coupe une séquence en fonction de la longueur souhaitée.

seq = input("Entrez une séquence :")
seq = list(seq)
nombre = int(input("Quelle taille pour votre séquence ? "))
sequence_nouvelle =""

for i in range(nombre) :
    aa = seq[i]
    sequence_nouvelle = sequence_nouvelle + aa

print('La nouvelle sequence est', sequence_nouvelle , ' Sa taille est de ', len(sequence_nouvelle))