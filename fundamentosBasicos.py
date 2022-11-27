print("Hello world!")

nome= "João"
idade=22
profissão = "Desenvolvedor Web"

print(nome)


num1 = 20
num2= 30

print(num1 + num2)

textoMúltiplasLinhas = '''texto de mutiplas linhas
linha 1
linha 2
linha 3'''

print(textoMúltiplasLinhas)

print("O nome é: %s" %(nome))
print("A idade é: {}" .format(idade))

'''além de não ser muito elegante concatenar dessa maneira, 
se a tentativa for de concatenar uma string ao um dado do 
tipo número, ocorrerá um erro:TypeError: can only concatenate 
str (not "int") to str'''

# print("Idade: " + idade)

print("Nome: " + nome)


# Variáveis
"""Os tipos são definidos de maneira implícita pelo python"""
_numero = 1
Numero = 1
numero = 1
numero123 = 1
texto ="""Um grande texto com grande...
...
...
..."""

# Tipos primirtivos
"""string, booleano, inteiro, float"""
string = "string"
booleano = True
booleano2 = False
int = 10
float = 1.5
print(string, booleano, booleano2, int, float)

"""É possível reatribuir a variável com diferentes tipos:"""
string = 10
int = booleano
print(string, int)

# padrao de nomenclatura

# - CamelCase = SaldoBancario
# - pascalCase = saldoBancario
# - snack_case = saldo_bancario

#  Formatação de texto
# %s - texto
# %d - inteiro
# %f - float
# %f3/4/5/6/qualquer numero = formata um float adicionando a quantidade de casas decimais 

# %s, %d, %f -> local onde o dado deve aparecer formatado
# %() -> local inde a variável/dado deve ser inserido

mes = "Dezembro"
dia = 25
eNatal = True
temperatura = 25.5456

print("O mes é: %s O dia é: %d Este dia representa o natal: %s A temperatura está prevista para: %.f2" %(mes, dia, eNatal, temperatura))


# 1

dia = 4
mes = 5
ano = 1999

print("O joão nasceu em %d/%d/%d" %(dia, mes, ano))

# 2 
hora = 18
min = 43

print("Agora são %d horas e %d minutos" %(hora, min))


# 3

pi = 3.4567892345

print("O PI é: %.5f" %(pi))


# Operadores AND e OR

# AND - Todos os valores envolvidos precisam resultar verdadeiro
# OR - qualuqer um dos valores envolvidos pode ser verdadeiro e retornará True
# NOT - Inverte o valor 

resultado1 = True and False;
print(resultado1)

resultado2 = True and True
print(resultado2)


resultado3 = True

resultado4 = False
print(resultado3 or resultado4)

resultado5 = False

print(not(resultado5))

# 1 

falta_comida = False

e_sabado = False

precisa_ir_no_mercado = False

if not(falta_comida) or not(e_sabado) : 
    print("Precisa ir no mercado: %s" %(not(precisa_ir_no_mercado)))


# 2

pode_atravessar_rua = True
sinal_vermelho = False
nenhum_carro_passando = False

if not(sinal_vermelho) and not(nenhum_carro_passando) :
    print("Pode atravessar? {}" .format(pode_atravessar_rua) )
    

# 3

if not(sinal_vermelho) or not(nenhum_carro_passando) :
    print("Pode atravessar? {}" .format(pode_atravessar_rua) )


# type casting

# funcao type e transformar dados

texto = "texto"
num1 = 0
num2 = 4
boolean = True
print(type(texto))
print(type(num1))
print(type(num2))
print(type(boolean))



