import random
listaA = [0]*100
listaB = [0]*50
i=0
while i < len(listaA):
 listaA[i] = random.randint(-100,100)
i = i + 1
print("Lista A ", listaA)
i=0
while i < len(listaB):
 listaB[i] = listaA[i] + listaA[(len(listaA)-1)-i]
 i=i+1
 print("Lista B ", listaB)
