## R 2)
#  recebe um número do usuário
num = int(input("Digite um número: "))

# calcular a sequência de Fibonacci
fb1, fb2 = 0, 1
while fb2 < num:
    fb1, fb2 = fb2, fb1 + fb2

# verifica se o número fornecido pertence a sequência de Fibonacci
if fb2 == num:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
