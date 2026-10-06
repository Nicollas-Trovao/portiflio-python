import os

diretorio_arquivo = os.path.dirname(os.path.abspath(__file__))
conta_path= os.path.join(diretorio_arquivo, "contato.txt")


class Contato:
    nome = "";
    sobrenome = "";
    email = ""
    telefone = ""


    def __init__(self, nome, sobrenome, email, telefone):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.telefone = telefone

def adicionar(contato):
    with open (conta_path, 'w', encoding= "utf-8") as arquivo:
        while True:
            
            nome = input("Adicione o nome do contato")
            
            sobrenome = input("Adicione o sobrenome do contato")
            
            email = input("Adicione o email do contato")
            
            telefone = input("Adicione o telefone do contato")

            tratar(nome, sobrenome, email, telefone)

            if tratar() == True:
                break
        

        contato.nome = nome
        contato.sobrenome = sobrenome
        contato.email = email
        contato.telefone = telefone

def tratar(nome: str, sobrenome: str, email: str, telefone: int):
    with open (conta_path, 'r', encoding= "utf-8"):
        #Tratar os dados
        if nome.type == str and sobrenome.type == str and email.type == str and telefone.type == int:
            return True
        else:
            return False

if __name__ == "__main__":
    adicionar(conta_path)