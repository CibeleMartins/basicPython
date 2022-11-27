from pprint import pprint
from functools import reduce


def sum(num1, num2):
    print(num1 + num2)


sum(1, 4)


def printName(name):
    print("O nome é: %s" % (name))


printName("Josh")


def printVariosValores(*valores):
    print(valores)

    for i in valores:
        print(i)


printVariosValores(10, 5, 6, 7, 8, 9, 3)

produtos = [
    {'name': 'Caderno', 'price': 50},
    {'name': 'Caneta', 'price': 9},
    {'name': 'Pincel', 'price': 6},
    {'name': 'Mouse', 'price': 90},
    {'name': 'Notebook', 'price': 5000},
    {'name': 'Garrafinha de água', 'price': 2},
]

pprint(produtos)


precos = map(lambda p: p['price'], produtos)
print(next(precos))

print("Resultado do for: ")

for preco in precos:
    print(preco)


def showBiggerValues(*valores):

  biggerValues = filter(lambda v: v > 5, valores)

  for value in biggerValues:
    print(value)


showBiggerValues(90, 70, 8 ,5)

arrayNumbers = [5,5,3]

def sumNumbersArray(array):

    sum = reduce(lambda actual, somador: actual + somador, array)

    print("A soma é: %d " %(sum))
    # for listSum in sum:
    #     print(listSum)


sumNumbersArray(arrayNumbers)