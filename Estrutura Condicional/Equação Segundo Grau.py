a = float(input("Coeficiente a "))
b = float(input("Coeficiente b "))
c = float(input("Coeficiente c "))
d = b*b - 4*a*c
if a != 0:
    print("Delta = %f" % d)
if d < 0:
    print("Impossivel calcular - Não possui raízes reais")
else:
    x1 = (-b + d**0.5) / (2*a)
print("R1 = %.5f" % x1)
if d > 0:
 x2 = (-b - d**0.5) / (2*a)
 print("R2 = %.5f" % x2)
else:
 print("Impossivel calcular")
