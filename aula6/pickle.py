import pickle

dados = {"nome": "João", "idade": 25, "cidade": "São Paulo"}

try:
    with open("dados.bin", "wb") as salvar_binario:
        pickle.dump(dados, salvar_binario)
    print("Dados salvos com sucesso em 'data.pkl'.")
except Exception as e:
    print(f"Erro ao salvar os dados: {e}")

try:
    with open("dados.bin", "rb") as file:
        dados_carregados = pickle.load(file)
    print("Dados carregados com sucesso:", dados_carregados)
except Exception as e:
    print(f"Erro ao carregar os dados: {e}")