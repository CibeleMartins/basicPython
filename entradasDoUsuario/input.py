# O input server para receber entradas do usuário, 

receiveName = input("Digite o seu nome: ")
print(f"O nome inserido foi: {receiveName}")

num1, num2 = input("Digite dois números ").split()

result = int(num1) // int(num2)

print(f"O resultado da divisão dos números foi: {result}")
