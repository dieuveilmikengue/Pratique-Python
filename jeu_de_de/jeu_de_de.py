# JEU DE LUDO
"""
Choisir votre joueur et tourner le premier à arriver à 30 points gagne la partie
si le joueur choisi une valeur superieur a l'autre, il sera incrementer de la valeur 
trouver tandisque la valeur de l'autre joueur restera constante
"""
from random import *
from time import *

print("Le jeu commence\n")
#On initialise le score a 0 - 0
joueur1 = 0
joueur2 = 0

# on affiche
print(f"Joueur1 [{joueur1}] : [{joueur2}] Joueur1")

# On initialise la machine à True (en fonctionnement)
machine = True

while machine: #Tant que le machine fonctionne
    j1 = randint(1, 6) #On affecte une valeur aleatoire au joueur1
    j2 = randint(1, 6) #On affecte une valeur aleatoire au joueur2
    sleep(1)
    if j1 > j2: #si le nombre envoyé par le joueur1 est superieur a celui du joueur2
        joueur1 += j1 #Augmenter le score du joueur1 du nombre envoyer
        print(f"\nj1[{j1}] : [{j2}]J2 \nScore \nj1[{joueur1}] : [{joueur2}]J2")
        if joueur1 >= 30: #et si le le score du joueur atteint 30, le jeu se termine en affichant
            print(f"\nLe joueur 1 remporte la partie avec 30")
            break #on arrete le jeu
        else: #sinon
            continue #On continue
    elif j1 < j2:
        joueur2 += j2
        print(f"\nj1[{j1}] : [{j2}]J2 \nScore \nj1[{joueur1}] : [{joueur2}]J2")
        if joueur2 >= 30:
            print(f"\nLe joueur 2 remporte la partie avec 30")
            break
        else:
            continue
    elif j1 == j2:
        print(f"\nj1[{j1}] : [{j2}]J2 \nScore j1[{joueur1}] : [{joueur2}]J2")
    else:
        break

