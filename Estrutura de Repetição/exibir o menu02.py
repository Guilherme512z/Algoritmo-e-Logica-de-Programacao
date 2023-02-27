n=1
c=0
s=0
while n >= 1 and n<= 4:
 n=int(input('1 – Ler e somar valor\n2 –Somatória\n3 – Quantidade de números\n4 -Média\n5 - Sair'))
if n==1:
 a=int(input('Valor 1? ')) 
 s=s+a
 c=c+1
elif n==2:
 print ('Somatória %d' % s)
elif n==3:
 print ('Quantidade de números %d' % c)
elif n==4:
 m=s/c
print ('Média %f' % m)