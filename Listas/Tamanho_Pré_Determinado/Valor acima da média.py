import random
num = [0.0]*100
soma = 0.0
conta = 0.0
i=0
while i<len(num):
 num[i] = random.random()*1000+1
 soma = soma + num[i]
 i=i+1
 i=0
 media = soma/len(num)
 print("Média dos valores sorteados %.2f" % media)
while i<len(num):
  if num[i]>media:
   print(num[i])
  i=i+1