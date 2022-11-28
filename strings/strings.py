# strings/slicing

# # 1
nameLastName = "Josh Halfmann"

name = nameLastName[0:4]

lastName = nameLastName[5:13]

print(name, lastName)

# # 2
toReadString = input("Insira uma string: ")

print(toReadString[: -1])


# 3 

receiveString = input("Digite uma palavra: ")

if ("a" in receiveString or "e" in receiveString or "i" in receiveString or "o" in receiveString or "u" in receiveString) :
    print("Nessa palavra tem vogal!")

else :
    print("Tem vogal não rapaz!")


# 4

receiveWord = input("Insira uma palavra: ")

insertABC = 'ABC' + receiveWord[0:]

print(insertABC)

