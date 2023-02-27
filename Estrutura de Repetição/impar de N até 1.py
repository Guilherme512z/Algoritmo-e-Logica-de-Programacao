n = int(input("Valor? "))
if n>1:
 conta = 2
while conta <= n:
 print("%d" % conta)
 conta = conta + 2
else:
 n = n + (-(n % 2) + 1)
while n <= 1:
 print("%d" % n)
 n = n + 2