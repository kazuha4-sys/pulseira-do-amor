import socket

# Configurações do cliente
host = '127.0.0.1'  # Endereço IP do servidor
port = 12345  # Porta usada pelo servidor

# Criação do socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
client_socket.connect((host, port))

# Envia uma mensagem para o servidor
message = "Olá, servidor!"
client_socket.send(message.encode())

# Fecha a conexão com o servidor
client_socket.close()
