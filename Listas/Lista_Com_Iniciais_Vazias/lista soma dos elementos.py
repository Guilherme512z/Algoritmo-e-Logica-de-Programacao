import random
lista1 = []
lista2 = []
lista3 = []
tam = 100
i = 0
while i < tam:
    lista1.append(random.randint(-100, 100))
    lista2.append(random.randint(-100, 100))
    i = i + 1
    print("Lista 1 ", lista1)
    print("Lista 2 ", lista2)
    i = 0
    conta = 0
while i < len(lista1):
    lista3.append(lista1[i]+lista2[i])
    i = i+1
    print("Lista 3 ", lista3)
