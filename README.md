# Ferramenta para extrair e baixar logos
Este projeto tem o intuito de otimizar o tempo gasto em serviços manuais e repetitivos, verificando cadastros sem imagens e gerando um arquivo de texto. Um script em Python é utilizado para baixar e transformar as imagens em um formato e dimensão padrão, enviando-as para o servidor. Junto com esse sistema, vêm algumas ferramentas de verificação para garantir que todos os nomes da lista tenham sido baixados.

# Pasta Enxtensao logos e Extensao logos 2.0
Esta extensão do Chrome extrai informações de uma página da web e cria um arquivo de texto com os nomes extraídos. Quando o usuário clica no botão "Extrair Dados" no popup, o script popup.js envia uma mensagem para content.js, que extrai os nomes da página e os envia para background.js. Neste último arquivo, os nomes são convertidos em um arquivo de texto e disponibilizados para download. O manifesto (manifest.json) define as permissões e configurações da extensão.
a diferenca de uma versao para outra eque sao usados em sistemas diferentes

# Atualização para a Versão 3.0:

A nova versão da extensão "Extensao logos" apresenta melhorias notáveis. Agora, além de extrair nomes, a extensão coleta URLs de imagens associadas a esses nomes. A manipulação avançada de dados, incluindo filtragem, resulta em resultados mais refinados. Focada na extração de logos, a versão 3.0 otimiza o processo de verificação de cadastros sem imagens. Essas mudanças refletem uma abordagem mais abrangente e eficaz.

# Pasta python
Abra Main.py 
Explicação: O botão "Baixar Imagens" tem a função de recuperar imagens de todos os canais cujos nomes estão listados no arquivo "canais.txt". Estas imagens são então armazenadas em pastas individuais correspondentes a cada canal, dentro do diretório denominado "imagens".

Posteriormente, ao clicar no botão "Remover Números", o sistema processa as imagens previamente salvas em "C:/Users/vinicius/Desktop/logos", removendo números de seus nomes e mantendo os arquivos na mesma localização.

Após essa etapa, ao selecionar "Enviar Arquivos", o sistema coleta todas as imagens presentes em "C:/Users/vinicius/Desktop/logos" e as envia para a pasta "logos" no servidor.

Em seguida, as funções de verificação entram em cena. Uma delas consiste em gerar uma lista de nomes de pastas, que é salva no arquivo "nomes_pastas.txt". Além disso, há a função de comparar arquivos, na qual o sistema compara os nomes presentes nos arquivos "canais.txt" e "nomes_pastas.txt", salvando os nomes ausentes em "txt3.txt".

Por fim, a função "Transformar 250x250" atua sobre as imagens baixadas, localizadas em "C:/Users/vinicius/Desktop/logos". Esta função redimensiona essas imagens para 250x250 pixels e as armazena no diretório "C:/Users/vinicius/Desktop/logos convertidas". Recomenda-se registrar o nome do canal antes de efetuar o download para otimizar o processo.

