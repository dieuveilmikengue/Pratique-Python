def table():
    print("Entrer nombre de votre choix")
    choix = input(">") #La valeur entree par l'utilisateur est affectee dans la variable choix en str
    choix = int(choix) #On convertit la variable choix en int

    x = 0 #On initialise notre compteur à 0

    while x <= 12: #Tant que x est inferieure ou egale à 12
        print(f"{choix} x {x} = {choix*x}") #Imprime ceci
        x += 1 #et augmente la valeur de x de 1 a chaque fois

table()