n=int(input("Termo da série de Fibonacci: "))
if n==1 or n==2:
 print ("Termo %d = %d" % (n,1))
else:
 u=1
 p=1
 c=3
 novo=0
while c<=n:
 novo=p+u
 p=u
 u=novo
 c=c+1
 print ("Termo %d = %d" % (n,novo))