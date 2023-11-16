import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from PIL import Image, ImageOps
import os
import io


# Função para redimensionar e salvar a imagem em formato PNG com fundo branco
def save_image_as_png(image_url, save_path):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            with Image.open(io.BytesIO(response.content)) as img:
                img = img.convert("RGBA")
                img = img.resize((250, 250))

                # Crie uma nova imagem de fundo branco do mesmo tamanho
                white_background = Image.new("RGBA", img.size, (255, 255, 255, 255))

                # Cole a imagem original sobre o fundo branco
                new_img = Image.alpha_composite(white_background, img)

                # Salve a nova imagem como PNG
                new_img.save(save_path, format="PNG")
    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")


# Lê as palavras-chave do arquivo de texto
with open('canais.txt', 'r') as keyword_file:
    keywords = keyword_file.read().splitlines()

# Número máximo de imagens a serem baixadas por palavra-chave
max_images = 5

# Pasta principal para conter as pastas das palavras-chave
main_folder = "imagens"
os.makedirs(main_folder, exist_ok=True)

# Loop pelas palavras-chave
for keyword in keywords:
    # Cria uma pasta com o nome da palavra-chave dentro da pasta principal
    download_folder = os.path.join(main_folder, keyword)
    os.makedirs(download_folder, exist_ok=True)

    # URL do Google Imagens com a palavra-chave
    url = f"https://www.google.com.br/search?q=channel%20{keyword}%20television%20logo&tbm=isch"

    # Faz uma requisição à página de imagens do Google
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # URL da página atual para criar URLs completas
        base_url = response.url

        # Variável para controlar o número de imagens baixadas
        num_images_downloaded = 0

        # Encontra todas as tags 'img' na página
        img_tags = soup.find_all("img")

        # Itera sobre as tags de imagem e faz o download das imagens
        for img_tag in img_tags:
            if num_images_downloaded >= max_images:
                break  # Sai do loop quando o limite de imagens for alcançado

            img_url = img_tag.get("src")

            # Verifica se a URL é relativa e cria uma URL completa
            if img_url and not img_url.startswith(("data:", "javascript:")):
                img_url = urljoin(base_url, img_url)

                # Gere um nome de arquivo único com "250x250" no final
                image_filename = f"{keyword}_{num_images_downloaded}_.250x250.png"
                image_path = os.path.join(download_folder, image_filename)

                # Salve a imagem como PNG com fundo branco
                save_image_as_png(img_url, image_path)

                num_images_downloaded += 1

        print(f"Foram baixadas {num_images_downloaded} imagens na pasta {download_folder}")

    else:
        print(f"Falha ao acessar a página de imagens do Google para a palavra-chave: {keyword}")
