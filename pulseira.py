import socket

# Configurações do cliente
host = 'endereco_ip_servidor'  # Endereço IP do servidor
porta = 12345  # Porta usada pelo servidor

# Criação do socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
client_socket.connect((host, porta))

# Envia uma mensagem para o servidor
mensagem = "Olá, servidor!"
client_socket.send(mensagem.encode())

# Fecha a conexão com o servidor
client_socket.close()

