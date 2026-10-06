

import dataset

db = dataset.connect('sqlite:///CRUD.db')
table = db['aluno']

#Create
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
matricula = input("Digie sua matricula")

table.insert(dict(nome = nome, idade = idade, matricula = matricula))

#Read
table = db['aluno'].all()
matricula = input("Qual seu numero de Matricula? ")
aluno = table.find_one(matricula=matricula)

#Update
matricula = input("Qual seu numero de Matricula? ")

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
table.update(dict(nome = "Nicollas", idade = 67), [matricula])



