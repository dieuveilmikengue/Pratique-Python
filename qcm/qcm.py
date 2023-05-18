
print("QUESTIONS A CHOIX MULTIPLE \n")

points = 0 #On initialise le nombre des points à 0

question1 = "La Première Querre Mondiale a commencée en quelle année ?" #La question
print(f"Question 1: {question1}")
suggestion1 = ["1913", "1914", "1917", "1918"] #Les reponses suggerees

for x, y in enumerate(suggestion1): #x et y vont parcourir la liste des suggestions et
    print(f"{x}. {y}") #Afficher respectivement l'indice et la valeur

reponse1 = input(">") #On affecte la reponse de l'utilisateur dans la variable reponse
reponse1 = int(reponse1) #On convertir cela en entier pour notre indice x
juste1 = "1914" #On stock la reponse qui est juste dans la variable juste


for i, j in enumerate(suggestion1): #i et j vont parcourir la liste des suggestions
    if i == reponse1: #si i qui est l'indice correspond a la reponse de l'utilisateur
        if j == juste1: #et que j qui est la valeur de l'indice i correspond à la variable juste
            points += 1 #Augmente la variable points de 1
            print(f"Bonne reponse {points} points") #Et affiche aussi ceci
        else: #Sinon
            print("Mauvaise reponse") #Affiche ceci

print("\n")

# LA MEME STRUCTURE QUE LA QUESTION 1 EN CHANGEANT JUSTE LES VARIABLES QUI SONT DANS LA BOUCLE FOR POUR EVITER LES CONFUSIONS DANS LA CONSOLE

question2 = "La Deuxième Guerre Mondiale a commencée en quelle année ?"
print(f"Question 2: {question2}")
suggestion2 = ["1997", "1929", "1939", "1945"]
for x, y in enumerate(suggestion2):
    print(f"{x}. {y}")


reponse2 = input(">")
reponse2 = int(reponse2)
juste2 = "1939"

for a, b in enumerate(suggestion2):
    if a == reponse2:
        if b == juste2:
            points += 1
            print(f"Bonne reponse {points} points")
        else:
            print("Mauvaise reponse")

print(f"Score: {points} points")
