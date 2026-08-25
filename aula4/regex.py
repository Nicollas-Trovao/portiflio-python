import re
def verifica_regex(texto: str) -> None:
    padrao = r'\(\d{3}\)\d{3}-\d{4}'
    resultado = re.search(padrao, texto)
    if resultado:
        print("Numero de telefone encontrado:", resultado.group())
    else:
        print("Numero de telefone nao encontrado")

def pesquisar_email(texto: str, escondido: bool) -> None:
    padrao = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    resultado = re.search(padrao, texto)
    if resultado:
        if escondido:
            email = resultado.group()
            email_escondido = re.sub(r'(?<=.).(?=[^@]*?@)', '*', email)
            print("Email encontrado:", email_escondido)
        else:
            print("Email encontrado:", resultado.group())
    else:
        print("Email nao encontrado")

if __name__ == "__main__":
    verifica_regex("Meu numero de telefone é (123)456-7890")
    pesquisar_email("Meu email é john.doe@example.com", False)
