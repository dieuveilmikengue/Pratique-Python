

# PIERRE , PAPIER, JUSTE AVEC LES CONDITIONS

player = "pierre"
list = ["pierre", "papier", "ciseau"]
ordi = choice(list)

if player == ordi:
    print("Vous avez tous choisis {} - {}: Egalité, Reesayer encore ! ou ecriver quitter pour sortir du jeu".format(player, ordi))
elif player == "pierre" and ordi == "ciseau":
    print("Vous[{}] : [{}]Ordinateur: Vous avez remporter la manche".format(player, ordi))
elif player == "pierre" and ordi == "papier":
    print("Vous[{}] : [{}]Ordinateur: Vous avez perdu la manche".format(player, ordi))
else:
    print("Oupps ! Il y'a eu un petit souci avec la machine")
