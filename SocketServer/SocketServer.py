#Joao Victor Elias Costa
#760927
import socket
import os

HOST = '127.0.0.1'
PORT = 65432


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	sock.bind((HOST, PORT))
	# while (True): - GETONE GETLIST PUT
	sock.listen()
	conn, addr = sock.accept()
	TYPE = conn.recv(1024).decode()

	if (TYPE == "GET_ONE"):
		conn.send("OK".encode())

		with conn:
			print('Connected by', addr)
			FILE_NAME = conn.recv(1024).decode()

			with open(FILE_NAME, 'rb') as file:
				for data in file.readlines():
					print(type(data))
					conn.send(data)

	if (TYPE == "GET_LIST"):
		with conn:
			print('Connected by', addr)
			local_dir = os.path.dirname(os.path.realpath(__file__))
			dir_string = ""

			# adiciona os itens do diretorio na lista
			for directory, subfolders, files in os.walk(local_dir):
				for file in files:
					if (dir_string == ""):
						dir_string = file
					else:
						dir_string = dir_string + "," + file			
			conn.send(dir_string.encode())

