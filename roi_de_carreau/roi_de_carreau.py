"""
choix de 0 - 100
moyenne * 0,8
valeur proche du rsultat gagne
les perdant auront -1 sur leurs vies jusqu'a -10
le joueur restant agagne
"""

import numpy as np

# JEU ROI DE CARREAU DANS ALICE IN BORDLANDS
j1 = 33
j2 = 40
j3 = 29
j4 = 30
j5 = 32

# On affiche les valeurs choisies par les joueurs dans une liste
list_j = [j1, j2, j3, j4, j5]
print(list_j)

# On calcule la moyenne qu'on appellera moyen
moyen = np.mean([j1, j2, j3, j4, j5])

# On calcule la moyenne multiplié par 0.8 qu'on appellera resultat
resultat = moyen*0.8

# On affiche la moyen et le resultat
print(moyen)
print(moyen, " x 0,8 = " ,resultat, "\n")

# On calcule la valeur absolu de la soustration entre le resultat et chaque joueur car la valeur la plus 
# proche sera consideré comme la valeur la plus proche du resultat
r1 = abs(resultat - j1)
r2 = abs(resultat - j2)
r3 = abs(resultat - j3)
r4 = abs(resultat - j4)
r5 = abs(resultat - j5)

# On recupère ces valeurs dans une liste qu'on appellera list
list = [r1, r2, r3, r4, r5]

# on recupère la plus petite valeur de notre list dans une variable qu'on appelera winner
winner = min(list)

# Juste pour connaitre l'indice de notre valeur min
l = list.index(winner)
print(l)

# On fait appel à la boucle for pour parcourrir la list et recuperer l'indice de notre plus petite valeur
for i, j in enumerate(list):
    if j == winner:
        print("Le joueur {} remporte la partie ".format(i+1)) #vu que notre liste commence par l'indice 0, on najoute +1 pour initialiser notre list à 1
    
