idades = {'ana': 10, 'maria': 30, 'joao': 34, 'fernando': 'indefinido'}

print(idades)

nome_numeros = {7.1:"sete vírgula um", 5.0: "cinco virgula zero"}

print(nome_numeros)

print(idades['ana'])
print(idades.get('ana'))
ana_update = idades['ana'] = 30

joao_update = idades.update({'joao': 50})
idades.pop('fernando')
idades.popitem()
print(idades)