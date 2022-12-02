"""1. Crie um programa que receba 5 números e retorne a média aritmética entre esses números"""

contador = 0
soma = 0

# while contador < 5:

#     contador += 1

#     num_lido = input("Digite um número: ")
#     num_float = float(num_lido)
#     soma += num_float

# media = soma / 5

# print(f"A média aritmética é: {media}")

""" 2. Crie um programa que receba 5 números, realiza a soma destes números, 
mas caso um destes números seja negativo não considere ele na soma"""

# while contador < 5:

#     contador += 1

#     num__recebido = float(input("Digite um número: "))
    
#     if num__recebido < 0:

#         soma -= num__recebido
#     else :
#         soma += num__recebido

# print(f"O resultado é: {soma}")

"""Crie um programa que receba como input uma string.
Em seguida percorra a string e diga quantos espaços em branco essa string tem."""

string = input("Digite uma palavra ou frase: ")
quantidade_espaco = 0

while (contador < len(string)):

    if (string[contador] == " "):
        quantidade_espaco += 1
    contador += 1

print(f"O número de espaços é de: {quantidade_espaco}")
