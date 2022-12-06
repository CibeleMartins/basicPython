# Crie uma lista contendo o nome de todos os meses do ano. em seguida,
# receba por input o mes (número) em que voce nasceu e mostre qual o nome do mes que voce nasceu.

listaMeses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

mesNascimento = int(input("Insira o mes que voce nasceu: "))


print(listaMeses[mesNascimento - 1])