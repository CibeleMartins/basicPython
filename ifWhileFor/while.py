
contador = 0
soma = 0

while contador < 5:

    contador += 1

    num_lido = input("Digite um número: ")
    num_float = float(num_lido)
    soma += num_float

media = soma / 5

print(f"A média aritmética é: {media}")

