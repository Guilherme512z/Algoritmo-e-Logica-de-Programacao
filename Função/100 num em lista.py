def lerElementos(quant):
    lista=[]
    for i in range(quant):
       lista.append(int(input(" Digite um valor")))
    return lista
def somar (lista):
    soma = 0
    for i in range (len(lista)):
       soma = soma + lista[i]
    return soma
    import MinhasFuncoes
def main():
   v = MinhasFuncoes.lerElementos(6)
   print(v)
   s = MinhasFuncoes.somar(v)
   m = s / len(v)
   print (m)
     
   main()