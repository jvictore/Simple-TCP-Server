#Joao Victor Elias Costa
#760927
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
TYPE = ""


while (TYPE != "SAIR"):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        print(f"Escolha uma das seguintes opcoes:\n1 - Listar arquivos do servidor.\n2 - Baixar um arquivo do servidor.\n3 - Enviar um arquivo ao servidor.\n4 - Sair")
        opcao = input()

        # POSSIVEIS OPCOES
        if (opcao == "1"):
            TYPE = "GET_LIST"
        elif (opcao == "2"):
            TYPE = "GET_ONE"
            FILE_NAME = input("Digite o nome do arquivo a ser BAIXADO: ")
        elif (opcao == "3"):
            TYPE = "PUT_ONE"
            FILE_NAME = input("Digite o nome do arquivo a ser ENVIADO: ")
        elif (opcao == "4"):
            TYPE = "SAIR"
        else:
            print("Opcao invalida.")

        if (TYPE == "GET_LIST"):
            sock.send(TYPE.encode())
            dir_string = sock.recv(16777216).decode()
            dir_list = dir_string.split(",")
            dir_list.remove("SocketServer.py")
            print(f"\nArquivos no servidor:")
            for dir in dir_list:
                print("- " + dir)
            print(f"_________________________________\n")

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
                    print("Arquivo baixado com sucesso.\n")
                    print(f"_________________________________\n")

        if (TYPE == "PUT_ONE"):
            sock.send(TYPE.encode())
            response = sock.recv(1024)
            if (response.decode() == 'OK'):
                
                # envia o nome do arquivo
                sock.send(FILE_NAME.encode())

                # envia o arquivo
                with open(FILE_NAME, 'rb') as file:
                    for data in file.readlines():
                        sock.send(data)
                    print("Arquivo enviado com sucesso.\n")
                    print(f"_________________________________\n")
