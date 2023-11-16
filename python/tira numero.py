import os

diretorio = 'C:/Users/vinicius/Desktop/logos'  # Substitua pelo caminho do seu diretório
extensao = '.png'  # Substitua pela extensão dos seus arquivos

for arquivo in os.listdir(diretorio):
    if arquivo.endswith(extensao):
        novo_nome = arquivo.replace('_1_', '')
        antigo_caminho = os.path.join(diretorio, arquivo)
        novo_caminho = os.path.join(diretorio, novo_nome)
        os.rename(antigo_caminho, novo_caminho)

for arquivo in os.listdir(diretorio):
    if arquivo.endswith(extensao):
        novo_nome = arquivo.replace('_2_', '')
        antigo_caminho = os.path.join(diretorio, arquivo)
        novo_caminho = os.path.join(diretorio, novo_nome)
        os.rename(antigo_caminho, novo_caminho)

for arquivo in os.listdir(diretorio):
    if arquivo.endswith(extensao):
        novo_nome = arquivo.replace('_3_', '')
        antigo_caminho = os.path.join(diretorio, arquivo)
        novo_caminho = os.path.join(diretorio, novo_nome)
        os.rename(antigo_caminho, novo_caminho)

for arquivo in os.listdir(diretorio):
    if arquivo.endswith(extensao):
        novo_nome = arquivo.replace('_4_', '')
        antigo_caminho = os.path.join(diretorio, arquivo)
        novo_caminho = os.path.join(diretorio, novo_nome)
        os.rename(antigo_caminho, novo_caminho)

print("Renomeação concluída!")
