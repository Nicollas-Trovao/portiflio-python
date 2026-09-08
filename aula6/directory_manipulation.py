import os

def criar_diretorio(nome_diretorio: str)->None:
    try: 
        os.makedirs(nome_diretorio)
        print(f"O diretório '{nome_diretorio}' doi criado com sucesso")
    except FileExistsError:
        print(f"O diretório '{nome_diretorio}' já existe")
    except PermissionError:
        print(f"Permissão negada para criar o diretorio '{nome_diretorio}'.")
    except Exception as e:
        print(f"Ocorreu um erro o criar o diretorio '{nome_diretorio}':")

def criar_arquivo(arquivo_nome: str, conteudo: str)->None:
    try:
        with open(arquivo_nome, 'w') as file:
            file.write(conteudo)
        print(f"O arquivo '{arquivo_nome}' foi criado com sucesso.")
    except PermissionError:
        print(f"Permissão negada para criar o arquivo '{arquivo_nome}'.")
    except Exception as e:
        print(f"Ocorreu um erro ao criar o arquivo '{arquivo_nome}':")

def main()->None:
    diretorio_atual = os.getcwd()
    print(f'Caminho com os.getcd(): {diretorio_atual}')
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    print(f'Caminho com os path: {diretorio_atual}')
    arquivo_nome = os.path.join(diretorio_atual, "arquivo_aula.txt")
    nome_diretorio = os.path.join(diretorio_atual, "direto_aula.txt")
    conteudo = "Conteudo de Exemplo"

    try:
        criar_diretorio(nome_diretorio)
        criar_arquivo(arquivo_nome, conteudo)
    except FileNotFoundError:
        print(f"O caminho especificado não foi encontrado.")
    except PermissionError:
        print(f"Permissão negada para acessar o caminho especificado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

    if __name__ == "__main__":
        main()