# O input serve para receber entradas do usuário,
# ou pode receber mais de uma entrada; nesse caso deve ser
# implementado em conjunto com o método split()

receiveName = input("Digite o seu nome: ")
print(f"O nome inserido foi: {receiveName}")

num1, num2 = input("Digite dois números ").split()

result = int(num1) // int(num2)

print(f"O resultado da divisão dos números foi: {result}")
