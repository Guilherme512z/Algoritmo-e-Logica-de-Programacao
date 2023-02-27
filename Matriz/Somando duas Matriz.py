A = [0]*2
print("Matriz A")
for linha in range(len(A)):
 A[linha] = [0]*3
for coluna in range(len(A[linha])):
 A[linha][coluna] = int(input("Digite um valor "))
 B = [0]*2
 print("Matriz B")
for linha in range(len(B)):
 B[linha] = [0]*3
for coluna in range(len(B[linha])):
 B[linha][coluna] = int(input("Digite um valor "))
 C = [0]*2
 print("Matriz C")
for linha in range(len(C)):
 C[linha] = [0]*3
for coluna in range(len(C[linha])):
 C[linha][coluna] = A[linha][coluna] + B[linha][coluna]
 print(A)
 print(B)
 print(C)
