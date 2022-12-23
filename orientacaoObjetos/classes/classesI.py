from pprint import pprint
# 1
class Pessoa :

    def __init__(self, nome, sobrenome, data_nascimento, email, senha):

        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.email = email
        self.senha = senha
        self.lista_pessoas = []

    def cadastrar_website(self, url, nome):

        return print(f"{nome} acabou de criar uma conta em {url}")

    def insere_mostra_pessoas(self, *pessoas):

        for pessoa in pessoas:

            self.lista_pessoas.append(dict(nome = pessoa.nome, sobrenome=pessoa.sobrenome, data_nascimento=pessoa.data_nascimento, email=pessoa.email, senha=pessoa.senha))

        return pprint(self.lista_pessoas)

        
pessoa = Pessoa("Josh", "Henry", "09/08/1978", "henry_j@gmail.com", "hj67889")
pessoa1 = Pessoa("Mariano", "Silveira", "01/10/1979", "marianos@gmail.com", "ms999889")

pessoa.insere_mostra_pessoas(pessoa, pessoa1)
