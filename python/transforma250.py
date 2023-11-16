from PIL import Image
import os

# Pasta de entrada com as imagens originais
pasta_entrada = 'C:/Users/vinicius/Desktop/logos baixadas'

# Pasta de saída para as imagens redimensionadas
pasta_saida = 'C:/Users/vinicius/Desktop/logos convertidas'

# Garante que a pasta de saída exista
if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

# Lista todos os arquivos na pasta de entrada
arquivos = os.listdir(pasta_entrada)

# Loop através de cada arquivo na pasta de entrada
for arquivo in arquivos:
    caminho_arquivo = os.path.join(pasta_entrada, arquivo)

    # Verifica se é um arquivo de imagem
    if os.path.isfile(caminho_arquivo) and arquivo.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
        # Abre a imagem
        imagem = Image.open(caminho_arquivo)

        # Redimensiona a imagem para 250x250 pixels
        imagem_redimensionada = imagem.resize((250, 250))

        # Define o nome do arquivo de saída com a extensão PNG
        nome_arquivo_saida = os.path.splitext(arquivo)[0] + '.png'

        # Salva a imagem redimensionada na pasta de saída
        caminho_arquivo_saida = os.path.join(pasta_saida, nome_arquivo_saida)
        imagem_redimensionada.save(caminho_arquivo_saida, 'PNG')

print("Todas as imagens foram redimensionadas e salvas em PNG.")
