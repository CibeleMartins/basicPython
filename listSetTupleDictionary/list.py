from pprint import pprint

array = []
array = list()

array_numeros = [1,2,3,4,5,6,7,8,9,10]
array_nomes = list(["Cibele"])

print(array_nomes)

#1. Crie uma funcao que recebe um valor e o insere ao final de uma lista
def finalLista(valor):

    list = ['Node', 'React', 'Angular', 'Python', 'JavaScript']
    list.append(valor)

    pprint(f"O valor inserido ao final da lista foi: {valor}")


finalLista("TypeScript")

# 2. Crie uma funcao que recebe um valor numerico e uma string. 
# Após isso, insere a string no indice de uma lista representado pelo 
# valor numerico recebido.
def numeroString(numero, string):

    list = [34, 56, 78]
    list.insert(numero, string)
    print(f"O valor {string} foi inserido no índice, {numero}. A lista está assim agora: {list}")

numeroString(2, "String")

# 3. Crie uma funcao que recebe um array e um numero. 
# Após isso, remove um item do array com base no número recebido.
def removeItemArray(array, numero):

    array.pop(numero)

    print(f"O item no índice: {numero} foi removido. A lista agora está assim: {array}")

removeItemArray([1,2,3,4,5,6,7,8,9,10,34,56,78], 6)


# 4. Crie uma funcao que recebe um valor e, se esse valor existir em uma lista
# será removido e mostrará uma mensagem de sucesso, caso contrário mostrará uma mensagem de erro.
def removeValorExistente(valor):

    list = ['Arroz', 'Feijão', 'Salada', 'Sorvete', 'Chocolate', 'Maçã']

    if(valor in list):
        list.remove(valor)
        print(f"O valor {valor} existia na lista, então foi removido.")
    else:
        list.append(valor)
        print(f"O valor não existia na lista, então foi adicionado.")

removeValorExistente("Arroz")
removeValorExistente("João")

# 5. Crie uma funcao que recebe um array, um numero e uma string.
# Após isso, insere a string no array em um indice representado pelo numero recebido.
def insereStringIndex(array, numero, string):

    array.insert(numero, string)

    print(f"O valor inserido foi {string} no index {numero}. O array agora está assim: {array}")

insereStringIndex([4, 5, 6, 7, 8], 2, "Texto")

# 6. Crie uma funcao que recebe um valor e verifica quantas vezes esse valor tem em uma lista
# E mostra uma mensagem de sucesso ou de falha com base na ocorrencia do valor dentro da lista.

def quantasVezesValorLista(valor):

    lista = list(['chocolate', 'sorvete', 'banana', 'maçã', 'chocolate', 'sorvete', 'banana', 'maçã', 'João'])

    quantidade_vezes = lista.count(valor)

    if (valor in lista):
        print(f"Esse valor aparece na lista {quantidade_vezes} vezes e é {valor}")
    else:
        print(f"O {valor} não aparece nenhuma vez na lista.")

quantasVezesValorLista('chocolate')
quantasVezesValorLista('João')

