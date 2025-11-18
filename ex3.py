import random
#matriu exemple

m = []
sep = "\n-------------\n"


# com crear una matriu de 10x5 utilitzant un bucle for
for i in range(10):
    fila = []
    for j in range(5):
        n = random.randint(0,99)
        fila.append(n)
    m.append(fila)

total = 0 
for fila in m:         # Per a cada fila de la matriu 'm'
    for numero in fila: 
        if numero > total: # Mirem quin es mes gran
            total = numero 

print(sep)
for fila in m:
    for n in fila:
        espais = "  " if n<10 else " "
        print(f"{espais}{n}",end="")
    print()
print(sep)
print(f"El numero mes gran de la llista es: {total}")