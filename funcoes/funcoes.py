import functools
# 1 - Crie uma funcao chamada "e_negativo" que receba um numero e retorne um booleano True se o numero for
# negativo, caso contrario retorne False

def e_negativo(numero):

    if numero < 0:
        print(True)
    else:
        print(False)

e_negativo(10)
e_negativo(-60)

# 2 - Crie uma funcao que receba um array de numeros (int ou float)
# e retorne sua soma

def somaNumerosArray(array_numeros):

    soma = functools.reduce(lambda a, p: a + p, array_numeros)

    return soma

print(somaNumerosArray([2,3,4]))
print(somaNumerosArray([2,3,4,90,80,900]))
    

#  3 - Crie uma funcao que receba uma string e que conte e retorne o numero de vogais desta string

#  4 - Crie uma funcao que retorne o ultimo caractere de uma string recebida

#  5 = Crie uma funcao que receba dois numeros e uam string dizendo se deve realizar a soma ou a subtracao dos numeros