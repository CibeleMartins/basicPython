saldo, debito = map(float, input("Digite o seu saldo e quanto voce deve: ").split(" "))

if saldo > debito :
    print("O seu saldo está positivo!")
else:
    print("O seu saldo está negativo!")