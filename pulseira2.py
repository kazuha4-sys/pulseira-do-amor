import socket

# Configurações do servidor
host = '127.0.0.1'  # Escuta em todas as interfaces de rede
port = 12345  # Porta para conexão

# Criação do socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa o socket ao host e à porta
server_socket.bind((host, port))

# Coloca o servidor para ouvir por conexões
server_socket.listen(1)

print(f"Servidor ouvindo em {host}:{port}")

# Aceita a conexão quando um cliente se conecta
client_socket, client_address = server_socket.accept()

print(f"Conexão de {client_address}")

# Recebe os dados do cliente
data = client_socket.recv(1024)
print(f"Mensagem recebida: {data.decode()}")

# Fecha a conexão com o cliente
client_socket.close()

# Fecha o socket do servidor
server_socket.close()
