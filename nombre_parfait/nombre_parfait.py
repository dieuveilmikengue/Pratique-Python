
n = input("Entrer un nombre: ") #On affecte la valeur entrée par l'utilisateur dans la variable n
n = int(n) #On récupère la valeur entrée et on convertit cela en integer
v = 0
for i in range(1, n): #On appel une variable i qui va parcourir les valeur de 1 à n
    if n % i == 0: #On verifie le cas ppour n modulo i == 0 car ces valeurs sont des diviseurs de n
        v += i #v qui etait initialiser à 0 est incrementer par les diviseurs de n
#on sort de la boucle for et on verifie
if n == v: #si n == v alors n est un nombre parfait
    print(f"{n} est un nombre parfait")  #alors n est un nombre parfait
else: #sinon
    print(f"{n} n'est pas un nombre parfait") #n n'est pas un nombre parfait