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

    def insere_mostra_pessoas(self, pessoa):

        self.lista_pessoas.append(pessoa)

        return print(self.lista_pessoas)

        
pessoa = Pessoa("Josh", "Henry", "09/08/1978", "henry_j@gmail.com", "hj67889")
objeto_pessoa = dict(nome = pessoa.nome, sobrenome=pessoa.sobrenome, data_nascimento=pessoa.data_nascimento, email=pessoa.email, senha=pessoa.senha)

pprint(objeto_pessoa)