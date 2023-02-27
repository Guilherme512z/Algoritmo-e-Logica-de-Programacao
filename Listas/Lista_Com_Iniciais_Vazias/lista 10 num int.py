num = []
tam = 10
soma = 0.0
conta = 0.0
i=0
while i<tam:
 num.append(int(input("Digite o %d número: " % (i+1))))
i=i+1
i=0
while i<len(num):
 if num[i]%2==1:
  soma = soma + num[i]
  conta = conta + 1
  i=i+1
  media = soma / conta
  print ("A média dos números ímpares é %.1f" % media)
