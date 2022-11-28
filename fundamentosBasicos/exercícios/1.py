
def receiveBalance (string):

    print(string)
    transformBalanceInNumber = int(string)
    
    result = transformBalanceInNumber - 1000

    print(f"Seu saldo atual é: {result}")


receiveBalance("1500")