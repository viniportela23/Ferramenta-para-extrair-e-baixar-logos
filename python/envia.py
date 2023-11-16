import paramiko
import os
import glob

host = 'ip'
port = 22
username = 'user'
password = 'senha'  # Ou utilize autenticação por chave, se preferir

# Diretório local contendo as imagens PNG
diretorio_local = 'C:/Users/vinicius/Desktop/logos/'

# Diretório remoto no servidor onde as imagens serão enviadas
diretorio_remoto = '/var/www/html/logos/'

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Inicializa a conexão SSH
ssh_client.connect(host, port, username, password)

# Lista os arquivos PNG na pasta local
arquivos_png = glob.glob(os.path.join(diretorio_local, '*.png'))

# Envia os arquivos PNG para o servidor remoto
for arquivo_local in arquivos_png:
    arquivo_remoto = os.path.join(diretorio_remoto, os.path.basename(arquivo_local))
    sftp = ssh_client.open_sftp()
    sftp.put(arquivo_local, arquivo_remoto)
    sftp.close()
    print(f"Enviado: {arquivo_local} para {arquivo_remoto}")

# Fecha a conexão SSH
ssh_client.close()
