texto = "Nossa aula manipulando String"

def exibir_string(texto):
    for i in range(len(texto)):
        print(texto[i])

def tamanho_string(texto):
    tamanho = len(texto)
    return tamanho

def contar_a(texto):
    contador = texto.count("a", 0, len(texto))
    return contador

def retornar_valores(texto):
    aula = texto.find("aula")
    return aula

    if aula == -1:
        print("a palavra aula nao foi encontrada")
    else:
        print("a palavra aula foi encontrada na posiçao: ", aula)

def substituir_string(texto):
    nova_txt = texto.replace("Aula", "Bunda")
    return nova_txt
    bunda = texto.find("Bunda")
    return bunda

def variacoes(texto):
    print(texto.upper())
    print(texto.lower())
    print(texto.title())
    print(texto.capitalize())
    print(texto.swapcase())

def strip ():
    nome = str(input("Digite seu nome: "))
    print("Olá, ", nome, "!")
    print("Olá, ", nome.lstrip(), "!")
    print("Olá, ", nome.rstrip(), "!")
    print("Olá, ", nome.strip(), "!")

def split():
    texto = str(input("Escreva um texto: "))
    print("Numero de palavras:", len(texto.split()))

def join():
    lista = ["Python", "é", "uma", "linguagem", "de", "programação"]
    texto = " ".join(lista)
    print(texto)


        
#--------------------------------------------------------------------

def main():
    exibir_string(texto)
    tamanho_string(texto)
    contar_a(texto)
    retornar_valores(texto)
    substituir_string(texto)
    variacoes(texto)
