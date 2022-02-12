#Joao Victor Elias Costa
#760927
import socket

HOST = '127.0.0.1'
PORT = 65432


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	sock.bind((HOST, PORT))
	sock.listen()
	conn, addr = sock.accept()
	with conn:
		print('Connected by', addr)
		FILE_NAME = conn.recv(1024).decode()

		with open(FILE_NAME, 'rb') as file:
			for data in file.readlines():
				conn.send(data)