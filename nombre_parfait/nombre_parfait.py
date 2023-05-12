
v = 0
n = input("Entrer un nombre: ")
n = int(n)
for i in range(1, n):
    if n % i == 0:
        v += i

if n == v:
    print(f"{n} est un nombre parfait")
else:
    print("Faux et faux")