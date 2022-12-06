# Crie uma lista contendo todos os dias (número) do mes em que voce nasceu. Em seguida,
# receba por input o dia que vc nasceu e remova desta lista. Ao final mostre o conteudo da lista.

lista = []

for i in range(0, 31):

    lista.append(i)

diaNascimento = int(input("Digite o dia que voce nasceu: "))

lista.remove(diaNascimento)

print(lista)