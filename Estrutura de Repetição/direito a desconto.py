n=9
while n != 9999:
 n=int(input('Idade (para sair 9999): '))
if (n<6 or n>=60) and n!=9999:
 print ('Pessoas com %d anos tem direito a desconto' % n)
