import os





diretorio_arquivo = os.path.dirname(os.path.abspath(__file__))
caminho= '\\dados.txt'
def ler_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        for i, linha in enumerate(linha, start=1):
            print(f'linha {i}: {linha}')

#print(caminho_arquivo.ler_arquivo())
#========================================
def escrever_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding= "utf-8") as arquivo:
        arquivo.write("meu pintinho amarelinho")
        arquivo.writelines(["\ncabe aqui na minha mao",
                             "\nnaminha mao",
                             "\n quando quer comer bixinho",
                             "\ncom seu biquinho ",
                             "\nele sisca o chao"])
    
#========================================
def cuzin(caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding= "utf-8") as arquivo:
        arquivo.write('esta e a primeira linha.\n')
        arquivo.write('esta e a segunda linha do arquivo.\n')

        linhas=['esta e a primeira linha em uma lista.\n',
                 'esta e a segunda linha em uma lista.\n']
        arquivo.writelines(linhas)
#========================================
cuzin(caminho)

def test_sell_tell():
    with open ("exemplo.txt", "w", encoding= "utf-8") as d:
        d.write("exemplo de uso dos metodos seek() e tell() em PY")
    with open("exemplo.txt", "r", encoding="utf-8") as f:
        print("posicao inicial do cursor: ", f.ell())

        conteudo=f.read(10)
        print("conteudo lido: ", conteudo)
        print("posiçao do cursor apos ler 10 caracteres: ", f.tell())

        f.seek(0,0)
        print("posiçao do cursor apos seek(0,0): ", f.tell())

        f.seek(15,0)
        print("posiçao do cursor apos seek(15,0): ", f.tell())

        parte= f.read(5)
        print("conteudo lido apos seek(15,0)", parte)
        #retrocede 5 caracteres a partir da posiçao atual usando seek absoluto:
        pos_atual=f.tell()
        f.seek(pos_atual - 5, 0)
        print("posiçao atual do cursor apos retrpceder 5 caracteres: ", f.tell())
        parte2=f.read(5)
        print ("conteudo lido apos retroceder 5 caracteres: ", parte2)
        #move para o fim dp arquivo:
        f.seek(0,2)
        print("posiçao do cursor no fim do arquivo: ", f.tell())
