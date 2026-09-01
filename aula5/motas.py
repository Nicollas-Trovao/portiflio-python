import os
import re

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class aluno:
    nome = ""
    nota = 0.0

def registrar_aluno(nome: str, nota: float):
    while True:
        limpar_console()
        print ("O que deseja fazer?")
        print ("1 - Registrar aluno")
        print ("2 - Acessar arquivo de alunos")
        print ("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            limpar_console()
            nomePadrao = r'^[A-Za-zÀ-ÿ\s]+$'
            nome = input("Digite o nome do aluno: ")
            if not re.match(nomePadrao, nome):
                print("Nome inválido. Por favor, digite um nome válido.")
                input()
                continue
            aluno.nome = nome

            #Loop para garantir que a nota seja válida
            while True:
                notaPadrao = r'^[0-9]+(\.[0-9]+)?$'
                nota = input("Digite a nota do aluno: ")
                aluno.nota = float(nota)

                if not re.match(notaPadrao, str(nota)) or float(nota) < 0 or float(nota) > 10:
                    print("Nota inválida. Por favor, digite uma nota entre 0 e 10.")
                    input()
                    limpar_console()
                    continue

            print("Salvando aluno em um arquivo...")
            try:
                arquivo = open("alunos.txt", "a")
                arquivo.write(f"{aluno.nome},{aluno.nota}\n")
                arquivo.close()
            except Exception as e:
                print(f"Erro ao abrir o arquivo: {e}")
                input()
                continue

            if arquivo.closed:
                print(f"Aluno registrado: {aluno.nome}, Nota: {aluno.nota}")
                input()


        if opcao == "2":
            try:
                limpar_console()
                print("Acessando arquivo de alunos...")
                print()
                arquivo = open("alunos.txt", "r")
                linhas = arquivo.readlines()
                for linha in linhas:
                    nome, nota = linha.strip().split(",")
                    print(f"Aluno: {nome}, Nota: {nota}")
                input()
                arquivo.close()
            except FileNotFoundError:
                print("Arquivos de alunos não encontrado.")
            
            finally:
                arquivo.close()

        if opcao == "0":
            print("Saindo do programa...")
            break

if __name__ == "__main__":
    registrar_aluno("", 0.0)

