import random
#matriu exemple

m = []
sep = "\n-------------\n"

print(sep)
# com crear una matriu de 10x5 utilitzant un bucle for
for i in range(10):
    fila = []
    for j in range(5):
        n = random.randint(0,99)
        fila.append(n)
    m.append(fila)

# Imprimeix tots els elements d'una llista de dues dimensions.
for fila in m:
    print(*fila)

print(sep)
for fila in m:
    for n in fila:
        espais = "  " if n<10 else " "
        print(f"{espais}{n}",end="")
    print()