# 6 - Escolha 3 objetos e crie uma lista para eles, armazenando o objeto e sua funcao.
# Recebea por input o nome de um objeto, se ele existir na lista imprima sua funca
# se nao, informe ao usuário que nao existe


objetos = {
    'Cadeira': 'Sentar',
    'Monitor': 'Assistir',
    'Caneta': 'Escrever'
}

solicitacao_usuario = input("Digite o nome de um objeto: ")

if solicitacao_usuario in objetos:

    print(objetos[solicitacao_usuario])
else:
    print("Não existe este objeto na lista!")

