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

                if not re.match(notaPadrao, str(nota)) or float(nota) < 0 or float(nota) > 10:
                    print("Nota inválida. Por favor, digite uma nota entre 0 e 10.")
                    input()
                    limpar_console()
                    continue
                else:
                    aluno.nota = float(nota)
                    break

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
                print()
                print("O que gostaria de fazer?")
                print("2 - Modificar nome de um aluno")
                print("1 - Modificar nota de um aluno")
                print("0 - Voltar")
                print()
                opcao = input("Escolha uma opção: ")
                if opcao == "1":
                    nome_aluno = input("Digite o nome do aluno que deseja modificar a nota: ")
                    aluno_encontrado = False
                    for i, linha in enumerate(linhas):
                        nome, nota = linha.strip().split(",")
                        if nome == nome_aluno:
                            aluno_encontrado = True
                            nova_nota = input(f"Digite a nova nota para {nome}: ")
                            if not re.match(r'^[0-9]+(\.[0-9]+)?$', str(nova_nota)) or float(nova_nota) < 0 or float(nova_nota) > 10:
                                print("Nota inválida. Por favor, digite uma nota entre 0 e 10.")
                                input()
                                break
                            linhas[i] = f"{nome},{nova_nota}\n"
                            print(f"Nota de {nome} atualizada para {nova_nota}.")
                            input()
                            break
                    if not aluno_encontrado:
                        print(f"Aluno {nome_aluno} não encontrado.")

                if opcao == "2":
                    nome_aluno = input("Digite o nome do aluno que deseja modificar: ")
                    aluno_encontrado = False
                    for i, linha in enumerate(linhas):
                        nome, nota = linha.strip().split(",")
                        if nome == nome_aluno:
                            aluno_encontrado = True
                            novo_nome = input(f"Digite o novo nome para {nome}: ")
                            if not re.match(r'^[A-Za-zÀ-ÿ\s]+$', novo_nome):
                                print("Nome inválido. Por favor, digite um nome válido.")
                                input()
                                break
                            linhas[i] = f"{novo_nome},{nota}\n"
                            print(f"Nome de {nome} atualizado para {novo_nome}.")
                            input()
                            break
                    if not aluno_encontrado:
                        print(f"Aluno {nome_aluno} não encontrado.")

                if opcao == "0":
                    continue
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

