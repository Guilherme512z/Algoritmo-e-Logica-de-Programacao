def tabuada(n):
  s=""
  for i in range(11):
    res = n * i
    s=s+str(n) + " x " + str(i) + " = " + str(res) + "\n"
  return s