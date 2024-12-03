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

liste_gauche.sort()
liste_droite.sort()
print("liste gauche", liste_gauche)
print("liste droite", liste_droite)

while len(liste_gauche):
    minimum_gauche = liste_gauche.pop(0)
    minimum_droite = liste_droite.pop(0)
    difference = abs(minimum_gauche - minimum_droite)
    total += difference
print(total)
