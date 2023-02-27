idade = int(input("Idade "))
if (idade <= 12):
 print("Criança")
else:
 if (idade <= 17):
  print("Adolescente")
 else:
  if (idade <= 59):
    print("Adulto")
  else:
   print("Idoso")