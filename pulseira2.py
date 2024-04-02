import socket

def encontrar_porta_livre():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    porta = s.getsockname()[1]
    s.close()
    return porta

# Encontrar uma porta livre
porta = encontrar_porta_livre()
host = '0.0.0.0'  # Escuta em todas as interfaces de rede

# Criação do socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa o socket ao host e à porta
server_socket.bind((host, porta))

# Coloca o servidor para ouvir por conexões
server_socket.listen(1)

print(f"Servidor ouvindo em {host}:{porta}")

# Aceita a conexão quando um cliente se conecta
client_socket, client_address = server_socket.accept()

print(f"Conexao de {client_address}")

# Recebe os dados do cliente
data = client_socket.recv(1024)
print(f"Mensagem recebida: {data.decode()}")

# Fecha a conexão com o cliente
client_socket.close()

# Fecha o socket do servidor
server_socket.close()
