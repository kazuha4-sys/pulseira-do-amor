import socket

# Configurações do cliente
host = '192.168.15.6'  # Endereço IP do servidor, ou 'localhost' se estiver na mesma máquina
porta = 12345  # Porta usada pelo servidor

# Criação do socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Conecta ao servidor
    client_socket.connect((host, porta))

    # Envia uma mensagem para o servidor
    mensagem = "Olá, servidor!"
    client_socket.send(mensagem.encode())

    # Fecha a conexão com o servidor
    client_socket.close()
except OSError as e:
    print(f"Erro ao conectar ao servidor: {e}")

