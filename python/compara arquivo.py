# Leitura do conteúdo dos arquivos de texto
with open('canais.txt', 'r') as arquivo1:
    linhas_txt1 = set(arquivo1.read().splitlines())

with open('nomes_pastas.txt', 'r') as arquivo2:
    linhas_txt2 = set(arquivo2.read().splitlines())

# Encontra os nomes que estão em txt1, mas não em txt2
nomes_que_faltam = linhas_txt1 - linhas_txt2

# Escreve os nomes em txt3.txt
with open('txt3.txt', 'w') as arquivo3:
    for nome in nomes_que_faltam:
        arquivo3.write(nome + '\n')

print("Nomes que estão em txt1, mas não em txt2, foram gravados em txt3.txt.")
