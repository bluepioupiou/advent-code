import re

file = open('1.txt', 'r')
lignes = file.readlines()

total = 0
liste_gauche = []
liste_droite = []
for ligne in lignes:
    #print(ligne)
    ligne = re.sub(" +", " ", ligne)
    ligne = ligne.replace("\n", "")
    gauche, droite = [int(x) for x in ligne.split(" ")]
    liste_gauche.append(gauche)
    liste_droite.append(droite)

for number in liste_gauche:
    total += number * liste_droite.count(number)
print(total)
