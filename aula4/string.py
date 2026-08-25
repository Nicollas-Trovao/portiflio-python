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

print(tamanho_string(texto))
print(contar_a(texto))
print(retornar_valores(texto))
print(substituir_string(texto))