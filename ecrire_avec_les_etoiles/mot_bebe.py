"""
referez vous au code source de la lettre_b
"""

l = 7

for i in range(1, l+1):
    for j in range(1, 30):
        if (j==1) or ((j==5) and (i!=1 and i!=(l+1)//2 and i!=l)) or (j==7) or (j==13) or ((j==17) and (i!=1 and i!=(l+1)//2 and i!=l)) or (j==19):
            print("* ", end="")
        elif (i==1 or i == (l+1)//2 or i==l) and (j>1 and j!=5 and j!=6 and j!=12 and j!=17 and j!=18 and j<=23):
            print("* ", end="")
        else:
            print("  ", end="")
    print()