
def receiveBalance (string):

    print(string)
    transformBalanceInNumber = int(string)

    if (transformBalanceInNumber <= 0) :
        print("Seu saldo está zerado.")
    else :
        result = transformBalanceInNumber - 1000

        print(f"Seu saldo atual é: {result}")



receiveBalance("500")



