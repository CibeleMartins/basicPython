"""1. Crie um programa que receba uma string por input e conte
quantos caracteres ela tem, nao leve em conta caracteres de espaço."""

# string = input("Digite uma palavra ou frase: ")
# soma = 0
# for caractere in string:

#   if (caractere != " "):
#     soma += 1

# print(f"A palavra tem {soma} caracteres!")


"""2. Crie um programa que faça o calculo do fatorial de um número. O fatorial a ser calculado deve ser recebido por input"""

# numero = input("Digite um número: ")
# numero_fatorial = int(numero)
# resultado = 1

# for i in range(1,numero_fatorial+1):

#     resultado *= i

# print(f"O fatorial de {numero} é {resultado}")


"""3. Crie um programa que leia uma quantidade arbitraria de textos e concatene eles numa string única."""

# quantidade_textos = int(input("Insira a quantidade de textos que vc quer concatenar: "))
# string_unica = ""

# for i in range(1,quantidade_textos+1):

#     texto = input("Digite uma palavra ou texto")

#     string_unica += texto

# print(string_unica)


"""4. Crie um programa que printe a tabuada da divisão de um número lido por input."""

# numero_recebido = input("Digite um número: ")
# numero_recebido_formatado = int(numero_recebido)

# for i in range(1, 11):

#     print(f"{numero_recebido} / {i} = {numero_recebido_formatado / i}")

"""5. Crie um programa que percorra os números de 3 até 30 e diga se o número é primo ou não."""

for i in range(3, 31):

    e_primo = True

    for num_teste in range(2, i):
        if (i % num_teste == 0):
            e_primo = False
            break

if e_primo:
    print(f"O número {i} é primo")
else:
    print(f'O número {i} não é primo')
