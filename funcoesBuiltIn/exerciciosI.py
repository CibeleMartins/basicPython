# 1 - Crie uma função que retorne a subtração de dois elementos, mas que considere o valor absoluto destes valores.

def valorAbsolutoSubtracao(elemento1, elemento2):

    subtracao = abs(elemento1) - abs(elemento2)

    return print(subtracao)

# valorAbsolutoSubtracao(-10, 20)

# 2 -  Sem usar "if`s", crie uma função que receba dois números e retorne a soma dos mesmos, mas o valor retornado não pode passar 
# de 10000 e deve ser sempre maior que 0.

import math

def soma(num1, num2):

    soma = num1 + num2

    soma = min(10000, soma)
    soma = max(0, soma)

    return soma

print(soma(6000, 5000))

# 3 - (DESAFIO) Crie uma função que receba argumentos de tamanho arbitrário. Todos serão números.
# Em seguida retorne o menor número entre todos os recebidos.

def menorNumero(*args):

    return print(min(args))

menorNumero(1,3,4,5,6)
# 4 - Crie uma funão que calcule a formula de Bhaskara, encontrado o X. 
# Os coeficientes a, b e c devem ser lidos por input.

#  5 - Crie uma função que receba uma string, e para cada letra minúscula a transforme para maiúscula e vice e versa.
