#Joao Victor Elias Costa
#760927
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

TYPE = "GET_ONE"
FILE_NAME = "OnePiece.jpg"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    if (TYPE == "GET_ONE"):
        sock.send(TYPE.encode())
        response = sock.recv(1024)
        if (response.decode() == 'OK'):
            # pedido do arquivo
            sock.send(FILE_NAME.encode())
            with open(FILE_NAME, 'wb') as file:
                while (True):
                    data = sock.recv(16777216)
                    if not data:
                        break
                    file.write(data)
                    