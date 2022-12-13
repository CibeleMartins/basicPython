# 10 -  Percorra os números de 0 a 20 e crie um array, onde caso o número 
# terminar em 0 o valor deve ser '0', caso contrario deve ser '-'.

lista = ['0' if str(numero)[-1] == '0' else '-' for numero in range(0,21)]

print(lista)