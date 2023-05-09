"""
Programme qui permet de convertir la minute, l'heure, le jour ou la semaine en secondes
"""

liste = ["a. Minutes - Secondes", "b. Heures - Secondes", "c. Jours - Secondes", "d. Semaines - Secondes", "5. Quitter"]

def minutes_secondes():
    seconde = 1 #On initialise la seconde à 1
    a = input("Entrer le nombre de minutes que vous voulez convertir en seconde \n>") #on affecte la valeur envoyer par l'utilisateur dans la variable a
    minute = 60 * seconde #minute egale à 60 secondes
    try: #on verifie la valeur qui sera rentrée par l'utilisateur s'il n'ya pas d'exception
        a = int(a) #On convertit la valeur entrée (en chaine de caractere) en entier
        minute_f = a * minute #On recupere la valeur qui sera entrer par l'utilisateur
        assert a > 0
        if a == 1: #si la valeur entree est 1 
            print(f"{a} minute = {minute_f} secondes") #afficher au singulier la minute
        elif a > 1: #si la valeur entree est superieure à 1
            print(f"{a} minutes = {minute_f} secondes") #afficher au pluriel les minutes
        else: #sinon (juste pour prevenir et eviter les erreurs dans la console)
             print("Un petit soucis") #affiche ceci dans la console
    except AssertionError: #On verifie si l'utilisateur envoie une chaine de caractère au lieu d'un nombre
        print("La valeur doit etre superieur 0") #On affiche.........
    except ValueError: #si la valeur entree a une exception
        print("Le programme n'accepte pas les lettres") #affiche ceci



def heures_secondes():
    seconde = 1
    a = input("Entrer l'heure que voulez convertir en secondes \n>")
    minute = 60 * seconde
    heure = 60 * minute
    try: #on verifie la valeur qui sera rentrée par l'utilisateur s'il n'ya pas d'exception
        a = int(a) #On convertit la valeur entrée (en chaine de caractere) en entier
        heure_f = a * heure #On recupere la valeur qui sera entrer par l'utilisateur
        assert a > 0
        if a == 1: #si la valeur entree est 1 
            print(f"{a} heure = {heure_f} secondes") #afficher au singulier l'heure
        elif a > 1: #si la valeur entree est superieure à 1
            print(f"{a} heures = {heure_f} secondes") #afficher au pluriel les heures
        else: #sinon (juste pour prevenir et eviter les erreurs dans la console)
             print("Un petit soucis") #affiche ceci dans la console
    except AssertionError: #On verifie si l'utilisateur envoie une chaine de caractère au lieu d'un nombre
        print("La valeur doit etre superieur 0") #On affiche.........
    except ValueError: #si la valeur entree a une exception
        print("Le programme n'accepte pas les lettres") #affiche ceci


def jour_secondes():
    seconde = 1
    minute = 60 * seconde
    heure = 60 * minute
    jour = 24 * heure
    a = input("Entrer le nombre de jour(s) que voulez convertir en secondes \n>")
    try: #on verifie la valeur qui sera rentrée par l'utilisateur s'il n'ya pas d'exception
        a = int(a) #On convertit la valeur entrée (en chaine de caractere) en entier
        jour_f = a * jour #On recupere la valeur qui sera entrer par l'utilisateur
        assert a > 0
        if a == 1: #si la valeur entree est 1 
            print(f"{a} jour = {jour_f} secondes") #afficher au singulier le jour
        elif a > 1: #si la valeur entree est superieure à 1
            print(f"{a} jours = {jour_f} secondes") #afficher au pluriel les jours
        else: #sinon (juste pour prevenir et eviter les erreurs dans la console)
             print("Un petit soucis") #affiche ceci dans la console
    except AssertionError: #On verifie si l'utilisateur envoie une chaine de caractère au lieu d'un nombre
        print("La valeur doit etre superieur 0") #On affiche.........
    except ValueError: #si la valeur entree a une exception
        print("Le programme n'accepte pas les lettres") #affiche ceci


def semaine_secondes():
    seconde = 1
    minute = 60 * seconde
    heure = 60 * minute
    jour = 24 * heure
    semaine = 7 * jour
    a = input("Entrer le nombre de semaine(s) que voulez convertir en secondes \n>")
    try: #on verifie la valeur qui sera rentrée par l'utilisateur s'il n'ya pas d'exception
        a = int(a) #On convertit la valeur entrée (en chaine de caractere) en entier
        semaine_f = a * semaine #On recupere la valeur qui sera entrer par l'utilisateur
        assert a > 0
        if a == 1: #si la valeur entree est 1 
            print(f"{a} semaine = {semaine_f} secondes") #afficher au singulier la semaine
        elif a > 1: #si la valeur entree est superieure à 1
            print(f"{a} semaines = {semaine_f} secondes") #afficher au pluriel les semaines
        else: #sinon (juste pour prevenir et eviter les erreurs dans la console)
             print("Un petit soucis") #affiche ceci dans la console
    except AssertionError: #On verifie si l'utilisateur envoie une chaine de caractère au lieu d'un nombre
        print("La valeur doit etre superieur 0") #On affiche.........
    except ValueError: #si la valeur entree a une exception
        print("Le programme n'accepte pas les lettres") #affiche ceci



# On crée une foànctionne qui va afficher la conversion a chaque appelle
def choix_conversion():
    choix = True
    while choix:
        print("\nChoisir votre conversion")
        for i in liste:
            print(i)
        joueur = input(">")

        if joueur == "a" or joueur == "A":
            print("Minutes - Secondes")
            minutes_secondes()
            continue
        elif joueur == "b" or joueur == "B":
            print("Heures - Secondes")
            heures_secondes()
            continue
        elif joueur == "c" or joueur == "C":
            print("Jours - Secondes")
            jour_secondes()
            continue
        elif joueur == "d" or joueur == "D":
            print("Semaines - Secondes")
            semaine_secondes()
            continue
        elif joueur == "5":
            print("Vous avez quitté le Jeu, a très bientot !")
            break
        else:
            print("Entrer une lettre de a à b comme affichée pour choisir le jeu")
            continue


choix_conversion()