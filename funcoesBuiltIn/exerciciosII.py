#  6 - Crie uma função que receba uma string e uma letra do alfabeto e retorne a quantidade de vezes que essa letra tem na string.
# Caso não ocorra nenhuma vez, retorne 0.

def qtdVezesLetra(string, letra):

    string_minuscula = string.lower()

    if string_minuscula.count(letra.lower()) > 0:

        print(string_minuscula.count(letra.lower()))
    
    else:

        print(0)

# qtdVezesLetra("Amanhã faz sol!!!", "A")