grelha = [["-","-","H","-"],["-","H","-","H"],["-","-","-","-"],["-","-","-","-"]]
for coluna in range(len(grelha)):
 for linha in range(len(grelha[coluna])):
  print("%s " % grelha[linha][coluna], end="")
  print("")