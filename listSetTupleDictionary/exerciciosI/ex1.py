# 1. Crie uma lista com os seguintes números 1,10,6,7,8,10. Em seguida printe a soma destes números.
from functools import reduce

lista = [1, 10, 6, 7, 8, 10]

soma = reduce(lambda atual, somador: atual + somador, lista)

print(soma)