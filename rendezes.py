import random

lista = [random.randint(0, 50) for _ in range(10)]
print(f'Alap lista: {lista}\n')


for index in range(1, len(lista)):
    seged = index-1
    while seged >= 0 and lista[seged] > lista[seged+1]:
        lista[seged], lista[seged+1] = lista[seged+1], lista[seged]
        seged -= 1
    print(f'Lista {index} cserélés után: {lista}')

print(f'\nLista rendezve: {lista}')

###############################################################################################

for index in range(1, len(lista)):
    seged = index-1
    szam = lista[index]
    while seged >= 0 and lista[seged] > szam:
        lista[seged+1] = lista[seged]
        seged -= 1
    lista[seged+1] = szam
    print(f'Lista {index} cserélés után: {lista}')

print(f'\nLista rendezve: {lista}')