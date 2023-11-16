import os

# Diretório que você deseja listar
diretorio = 'C:/Users/vinicius/PycharmProjects/script-logo/imagens'  # Substitua pelo caminho do seu diretório

# Verifica se o diretório existe
if os.path.exists(diretorio) and os.path.isdir(diretorio):
    # Lista os nomes das pastas no diretório
    nomes_pastas = [nome for nome in os.listdir(diretorio) if os.path.isdir(os.path.join(diretorio, nome))]

    # Caminho para o arquivo de texto onde você deseja escrever os nomes das pastas
    arquivo_txt = 'nomes_pastas.txt'

    # Escreve os nomes das pastas no arquivo de texto
    with open(arquivo_txt, 'w') as arquivo:
        for nome_pasta in nomes_pastas:
            arquivo.write(nome_pasta + '\n')

    print(f'Nomes das pastas foram gravados em {arquivo_txt}')
else:
    print(f'O diretório {diretorio} não existe.')

