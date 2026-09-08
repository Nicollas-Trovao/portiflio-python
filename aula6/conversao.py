import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

imagem_entrada_nome = os.path.join(diretorio_atual, "imagem_original.jpg")
imagem_saida_nome = os.path.join(diretorio_atual, "imagem_copiada.jpg")

if os.path.exists(imagem_entrada_nome):
    try:
        with open(imagem_entrada_nome, "rb") as imagem_entrada:
            imagem_dados = imagem_entrada.read()

        with open(imagem_saida_nome, "wb") as imagem_saida:
            imagem_saida.write(imagem_dados)

        print(f"Imagem copiada com sucesso para '{imagem_saida_nome}'")
    except Exception as e:
        print(f"Erro ao copiar a imagem: {e}")

dados_binarios_nome = os.path.join(diretorio_atual, "dados_puros.bin")

frase = "Raphael"
dados_binarios = frase.encode('utf-8')

try:
    with open(dados_binarios_nome, "wb") as salvar_binario:
        salvar_binario.write(dados_binarios)
    print("Dados binários salvos com sucesso.")

except Exception as e:
    print(f"Erro ao salvar os dados binários: {e}")

if os.path.exists(dados_binarios_nome):
    try:
        with open(dados_binarios_nome, "rb") as ler_binario:
            dados_lidos = ler_binario.read()

        #1. texto decodificado
        dados_lidos_texto = dados_lidos.decode('utf-8')

        #2. converter os bytes para uma string de zeros e uns separados por espaço
        binario_real = ' '.join(format(byte, '08b') for byte in dados_lidos)

        print(f"Dados carregado com sucesso")
        print(f"{binario_real} -> {dados_lidos_texto}")

    except Exception as e:
        print(f"Erro ao ler os dados binários: {e}")