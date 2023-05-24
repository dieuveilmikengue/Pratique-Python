print("LES FORMULES PHYSIQUES")

def r_vitesse():
    try: 
        distance = input("distance: ")
        distance = int(distance)
        temps = input("temps: ")
        temps = int(temps)
        vitesse = distance / temps
        print(f"V = {vitesse} m/s")
    except ZeroDivisionError:
        print("Non non")
    except:
        print("Entrer un nombre")

def v_rotation():
    try: 
        tours = input("nombres des tours: ")
        tours = int(tours)
        temps = input("temps: ")
        temps = int(temps)
        vitesse = tours / temps
        print(f"N = {vitesse} tours/s")
    except ZeroDivisionError:
        print("Non non")
    except:
        print("Entrer un nombre")

print("Choisissez le calcul a effectuer")
liste = ["1. Vitesse Lineaire", "2. Vitesse de rotation"]

for element in liste:
    print(element)

def main():
    choix = input(">")

    if choix == "1":
        r_vitesse()
    elif choix == "2":
        v_rotation()
    else:
        print("Une erreur c'est produite")


main()