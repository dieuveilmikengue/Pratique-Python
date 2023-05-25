from verbecc import Conjugator

cg = Conjugator(lang='fr')

verbe = input("Entrer un verbe à l'infinitif: ")
print("\n")
conjugation = cg.conjugate(verbe)
futur_simple = conjugation['moods']['indicatif']

#Les modes
# print(conjugation['moods'].keys())

#Les élements de l'indicatif
# conjugation['moods']['indicatif'].keys()

# les elements du subjonctif
# print(conjugation['moods']['indicatif'].keys())




for k, v in futur_simple.items(): #Tant que y'a des element dans la variable dict
    print(f"{k}") #Affiches les clés
    for g in v: #On crée une variable g qui va parcourir chaque valeur(v) qui sont des listes pour la clé k
        print(f"{g}")
    print("\n")