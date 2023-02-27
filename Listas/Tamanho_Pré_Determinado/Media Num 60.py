num = [0.0]*10
soma = 0.0
conta = 0.0
i=0
while i<len(num):
 num[i] = float(input("Digite o %d o. numero: " % (i+1)))
i=i+1
i=0
while i<len(num):
 if num[i] >= 60:
  soma = soma + num[i]
  conta = conta + 1
  i=i+1
  media = soma / conta
  print ("A média dos números digitados a partir do valor 60 é %.1f" % media)
