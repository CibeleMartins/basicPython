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
# Após isso, remove um item do array com base no número recebeido.

# 4. Crie uma funcao que recebe um valor e, se esse valor existir em uma lista
# será removido e mostrará uma mensagem de sucesso, caso contrário mostrará uma mensagem de erro.

# 5. Crie uma funcao que recebe um array, um numero e uma string.
# Após isso, insere a string no array em um indice representado pelo numero recebido.

# 6. Crie uma funcao que recebe um valor e verifica quantas vezes esse valor tem em uma lista
# E mostra uma mensagem de sucesso ou de falha com base na ocorrencia do valor dentro da lista.



