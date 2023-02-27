import random
listaA = []
listaB = []
tam = 100
i = 0
while i < tam:
    listaA.append(random.randint(-100, 100))
    i = i + 1
    print("Lista A ", listaA)
    i = 0
    ult = (len(listaA)-1)
while i < (tam/2):
    if (i != (ult-i)):
        listaB.append(listaA[i] + listaA[ult-i])
else:
    listaB.append(listaA[i])
    i = i+1
    print("Lista B ", listaB)
