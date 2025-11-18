import random
#matriu exemple

m = []
sep = "\n-------------\n"

print(sep)

# Crearem una matriu de 5x5
mida_matriu = 5 

for i in range(mida_matriu):  
    fila = []
    for j in range(mida_matriu):  
        n = random.randint(0,99)
        fila.append(n)
    m.append(fila)

print(sep)
for fila in m:
    for n in fila:
        espais = "  " if n<10 else " "
        print(f"{espais}{n}",end="")
    print()
print(sep)

total_diagonal = 0

for i in range(mida_matriu):
    # A la diagonal principal, l'índex de fila 'i'
    # és igual a l'índex de columna 'i'.
    total_diagonal += m[i][i]

print(f"El total de la suma de la diagonal és: {total_diagonal}")
print(sep)