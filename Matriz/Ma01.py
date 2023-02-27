grelha = [["-","-","H","-"],["-","H","-","H"],["-","-","-","-"],["-","-","-","-"]]
for linha in range(len(grelha)):
 for coluna in range(len(grelha[linha])):
  print("%s " % grelha[linha][coluna], end="")
  print("")
