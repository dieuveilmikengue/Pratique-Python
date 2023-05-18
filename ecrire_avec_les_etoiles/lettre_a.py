l = 7 #On affecte le nombre des lignes dans la variable l

for i in range(1, l+1): #i va parcourir les lignes de 1 à l+1
    for j in range(1, 5): #j va parcourir les colonnes de 1 a 5
        if (j==1 or j==5) and (i!=1): #au niveau de la colonne 1 et 5 de toutes lignes sauf la ligne 1
            print("* ", end="") #remplie cela des etoiles et le reste(end) laisse ca vide
        elif (i==1 or i == (l+1)//2) and (j>1 and j<5): #au niveau de la ligne 1, (l+1)//2 des colonnes comprises entre 1 et 5
            print("* ", end="") #remplie cela des etoiles et le reste(end) laisse ca vide
        else: #Pour les lignes et les colonnes qu'on a pas parler 
            print("  ", end="") #Mets les espaces comme dans le print et le reste tu le laisse vide
    print()