"""Crie um programa que receba o seu saldo bancário e o quanto voce deve. 
Em seguida o programa deve dizer se voce tem saldo positivo ou negativo."""

# saldo, debito = map(float, input("Digite o seu saldo e quanto voce deve: ").split(" "))

# if saldo > debito :
#     print("O seu saldo está positivo!")
# else:
#     print("O seu saldo está negativo!")

"""Crie um programa que possui uma variável que guarde seu CPF e que guarde uma senha de sua escolha.
Em seguida receba por input uma senha do usuário. Caso a senha recebida seja a correta mostre o CPF, caso não,
diga que a senha está incorreta"""

# cpf = "05567789956"
# senha = 123567

# senhaUsuario = input("Digite sua senha: ")

# if int(senhaUsuario) == senha:
#     print(f"O seu CPF é: {cpf}")
# else :
#     print("Senha incorreta.")

"""Crie um programa que fale sobre sua idade. As regras sao as seguintes: vc deve receber por input a idade, se vc tiver
ate 3 anos printe que vc 'um bebe, ate 13 anos uma crianca, ate 18 anos adolescente, ate 65 adulto. Em nenhum destes casos é
um idoso."""

idade = int(input("Digite sua idade: "))

if idade <= 3:
    print("Um bebe!")
elif idade <= 13:
    print("É uma criança!")
elif idade <= 18:
    print("É um adolescente!")
elif idade <= 65:
    print("É um adulto!")
else:
    print("É um idoso")
