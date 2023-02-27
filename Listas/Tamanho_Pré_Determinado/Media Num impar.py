num = [0.0]*10
soma = 0.0
conta = 0.0
i=0
while i<len(num):
 num[i] = int(input("Digite a nota do %d o. aluno: " % (i+1)))
 i=i+1
 i=0
while i<len(num):
 if num[i] %2==1:
  soma = soma + num[i]
  conta = conta + 1
  i=i+1
  media = soma / conta
  print ("A média dos números ímpares é %.1f" % media)