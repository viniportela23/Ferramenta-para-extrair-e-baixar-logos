# Ferramenta para extrair e baixar logos
Este projeto tem o intuito de otimizar o tempo gasto fazendo servicos manuais e repetitivos verificando cadastros sem imagens baixando transformando em um formato e dimensao padrao e enviando para o servidor

# Pasta python
Abra Main.py 
Explicação: O botão "Baixar Imagens" tem a função de recuperar imagens de todos os canais cujos nomes estão listados no arquivo "canais.txt". Estas imagens são então armazenadas em pastas individuais correspondentes a cada canal, dentro do diretório denominado "imagens".

Posteriormente, ao clicar no botão "Remover Números", o sistema processa as imagens previamente salvas em "C:/Users/vinicius/Desktop/logos", removendo números de seus nomes e mantendo os arquivos na mesma localização.

Após essa etapa, ao selecionar "Enviar Arquivos", o sistema coleta todas as imagens presentes em "C:/Users/vinicius/Desktop/logos" e as envia para a pasta "logos" no servidor.

Em seguida, as funções de verificação entram em cena. Uma delas consiste em gerar uma lista de nomes de pastas, que é salva no arquivo "nomes_pastas.txt". Além disso, há a função de comparar arquivos, na qual o sistema compara os nomes presentes nos arquivos "canais.txt" e "nomes_pastas.txt", salvando os nomes ausentes em "txt3.txt".

Por fim, a função "Transformar 250x250" atua sobre as imagens baixadas, localizadas em "C:/Users/vinicius/Desktop/logos". Esta função redimensiona essas imagens para 250x250 pixels e as armazena no diretório "C:/Users/vinicius/Desktop/logos convertidas". Recomenda-se registrar o nome do canal antes de efetuar o download para otimizar o processo.

