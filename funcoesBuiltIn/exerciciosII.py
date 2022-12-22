#  6 - Crie uma função que receba uma string e uma letra do alfabeto e retorne a quantidade de vezes que essa letra tem na string.
# Caso não ocorra nenhuma vez, retorne 0.

def qtdVezesLetra(string, letra):

    string_minuscula = string.lower()

    if string_minuscula.count(letra.lower()) > 0:

        print(string_minuscula.count(letra.lower()))
    
    else:

        print(0)

# qtdVezesLetra("Amanhã faz sol!!!", "A")

#  7 (DESAFIO) Crie um função que receba uma string e uma letra do alfabeto. Retorne uma lista
# contendo o índice de onde todas as ocorrencia aparecem.
def indicesOcorrencias(string, letra):
    
   indices = []
   indice = 0

   string_minuscula = string.lower()

   for i in string_minuscula:

    if  i == letra.lower():

        indices.append(indice)
        # manda so os indices iguais a letra

    indice += 1
    # incrementa p/ cada index da string
    
    print(indices)

#    for i in range(0, qtd_vezes_letra):

#     if letra.lower() in string_minuscula:

#         print(string_minuscula[i])
  
# indicesOcorrencias("hoje foi um dia bom!!!", "o")

#  8 - Crie uma função que receba o que foi digitado pelo usuário no chat e tambem uma lista
# contendo todas as palavras nao permitidas a serem digitadas. Essa funcao entao retornara o que foi digitado pelo usuário
# mas no lugar das palavras nao permitidas retorna o caractere '*'

def escondePalavroes(chat, palavras):

    for i in palavras:

        if i in chat:

            chat = chat.replace(i, '*')

    print(chat)

escondePalavroes("puta vc é um viado, lazarento", ['puta', 'viado', 'lazarento'])