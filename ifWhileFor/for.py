"""1. Crie um programa que receba uma string por input e conte
quantos caracteres ela tem, nao leve em conta caracteres de espaço."""

string = input("Digite uma palavra ou frase: ")
soma = 0
for caractere in string:

  if (caractere != " "):
    soma += 1

print(f"A palavra tem {soma} caracteres!")



"""2. Crie um programa que faça o calculo do fatorial de um número. O fatorial a ser calculado deve ser recebido por input"""


"""3. Crie um programa que leia uma quantidade arbitraria de textos e concatene eles numa string única."""


"""4. Crie um programa que printe a tabuada da divisão de um número lido por input."""

"""5. Crie um programa que percorra os números de 3 até 30 e diga se o número é primo ou não."""