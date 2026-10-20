from datetime import datetime
from pessoa import Pessoa
from veiculo import veiculo
from marca import Marca

# Função principal do programa
def main():

    cpf = input("Digite o CPF do proprietário: ")
    nome = input("Digite o nome do proprietário: ")
    nascimento = input("Digite a data de nascimento (YYYY-MM-DD): ")
    
    pessoa1 = Pessoa(cpf=cpf, nome=nome, nascimento=datetime.strptime(nascimento, "%Y-%m-%d").date())
    
    marca1 = Marca(id=1, nome="Toyota", sigla="TYT")

    placa = input("Digite a placa do veículo: ")
    cor = input("Digite a cor do veículo: ")
    veiculo1 = veiculo(placa=placa, cor=cor, proprietario=pessoa1, marca=marca1)

    
    print(f"Veículo: {veiculo1.placa}, Cor: {veiculo1.cor}, Proprietário: {veiculo1.proprietario.nome}, Marca: {veiculo1.marca.nome}")