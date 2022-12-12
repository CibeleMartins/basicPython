# 9 - Crie uma lista contendo todos os numeros de 0 a 100, mas filtre mantendo apenas os numeros que terminam com 0

listaNumeros = []
for i in range(0, 101):
    listaNumeros.append(str(i))
print(listaNumeros)

listaNumeroTerminaZero = [numero for numero in listaNumeros if numero[-1] == '0']

print(listaNumeroTerminaZero)