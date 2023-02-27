import random
lista1 = []
tam=100
i=0
while i < tam:
 lista1.append(random.randint(0,1000))
i = i + 1
i=0
conta=0
while i < len(lista1):
 if lista1[i]%2 == 0:
  conta=conta+1
  i=i+1
  print ("Quantidade de números pares %d " % conta)
