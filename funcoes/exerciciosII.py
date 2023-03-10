# 6 - Crie uma funcao que receba uma lista de elementos e um valor qualquer. Em seguida retorne um booleano
# dixendo se o valor foi encontradoou nao na lista

def foiEncontrado(listaElementos, valorQualquer):

    if valorQualquer in listaElementos:

        return print(True)
    else:

        return print(False)

# foiEncontrado(['mercado', 1, 2, 3], 'mercado')
# foiEncontrado(['mercado', 1, 2, 3], 'sorvete')

# 7 - Crie uma funcao que receba uma lista de elementos e um valor qualquer. Em seguida, retorne um booleano
# dizendo se o valor foi encontrado ou nao e tambem a posicao onde foi encontrado

def foiEncontradoIndex(listaElementos, valorQualquer):

    if valorQualquer in listaElementos:

        index_valor = listaElementos.index(valorQualquer)

        return print(f"{True} no indice {index_valor}")
    else:

        return print(False)

foiEncontradoIndex(['mercado', 1, 2, 3], 'mercado')
foiEncontradoIndex(['mercado', 1, 2, 3], 'sorvete')

#  8 - Crie uma funcao que recebe um numero arbitrario de parametros. Em seguida diga qual o tipo de cada parametro
def qualOTipo(*parametros):

    for i in range(0, len(parametros)):

        parametro = parametros[i]

        tipo = type(parametro)

        print(tipo)

qualOTipo('sdgs', 90, 'sfgs', 9)

# 9 - Crie uma funcao que receba uma string, mas que possua um decorator para transforma-la em uma citacao, ou seja,
# voce deve retornar a string entre aspas duplas, alem disso, transformar os carateres para minuscula usando a funcao lower()


def decoratorCitacao(func):

    def fazCitacao(string):

        citacao = '"' + func(string).lower() + '"'

        return citacao


    return fazCitacao
    
@decoratorCitacao

def transformaString(string):

    return string

citacao = transformaString("E quando eu estiver triste Simplesmente me abrace Quando eu estiver louco")
print(citacao)

#  10 - Cria uma funcao recursiva que itere os numeros de 0 ate 10 e print o resultado de sua divisao inteira com o número 3.

def divisaoPorTres(num):

    if num == 11:

        return

    print(num // 3)
    
    divisaoPorTres(num + 1)

divisaoPorTres(0)