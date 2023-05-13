# PIERRE, PAPIER, CISEAU

from random import * #La librairie random pour recuperer les valeurs aleatoirement de la partie l'ordinateur

print("Choisissez entre pierre, papier et ciseau")
jeu = True
pointsPlayer = 0
pointsOrdi = 0

while jeu:
    player = input(">")
    list = ["pierre", "papier", "ciseau"]
    ordi = choice(list)

    if player == ordi:
        print("Vous[{}] : [{}]Ordinateur: Egalité, choisissez une nouvelle fois  ! ou ecriver quitter pour sortir du jeu".format(player, ordi))
        continue
    elif (player == "pierre" and ordi == "ciseau") or (player == "ciseau" and ordi == "papier") or (player == "papier" and ordi == "pierre"):
        print("Vous[{}] : [{}]Ordinateur: Vous avez remporter la manche, choisissez une nouvelle fois ! ou ecriver quitter pour sortir du jeu".format(player, ordi))
        pointsPlayer += 1
        continue
    elif (player == "pierre" and ordi == "papier") or (player == "ciseau" and ordi == "pierre") or (player == "papier" and ordi == "ciseau"):
        print("Vous[{}] : [{}]Ordinateur: Vous avez perdu la manche, choisissez une nouvelle fois ! ou ecriver quitter pour sortir du jeu".format(player, ordi))
        pointsOrdi += 1
        continue
    elif player == "quitter":
        if pointsPlayer < pointsOrdi:
            print("score finale\nVous[{}] : [{}]Ordinateur \nVous avez perdu la partie".format(pointsPlayer, pointsOrdi))
        elif pointsPlayer > pointsOrdi:
            print("score finale\nVous[{}] : [{}]Ordinateur \nVous avez gagné la partie, FELICITATION !".format(pointsPlayer, pointsOrdi))
        else:
            print("Il y'a une erreur quelque part")
        break
    else:
        print("Oupps ! Il y'a eu un petit souci avec la machine, vous n'avez pas saisie la valeur attendue, choisissez une nouvelle fois entre pierre, papier et ciseau ! ou ecriver quitter pour sortir du jeu")
        
