import random
lista1 = [0]*100
lista2 = [0]*len(lista1)
lista3 = [0]*(2*len(lista1))
i=0
while i < len(lista1):
 lista1[i]=random.randint(-100,100)
 lista2[i]=random.randint(-100,100)
i = i + 1
print("Lista 1 ",lista1)
print("Lista 2 ",lista2)
i=0
conta=0
while i < len(lista1):
 lista3[i]=lista1[i]
i=i+1
j=0
while j < len(lista2):
 lista3[i]=lista2[j]
i=i+1
j=j+1
print("Lista 3 ",lista3)
