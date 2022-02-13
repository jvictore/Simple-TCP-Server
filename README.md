# Simple-TCP-Server
Servidor local TCP simples para troca de arquivos

Para o funcionamento do código só é necessario ter Python 3 instalado. Baixe no link: https://www.python.org/downloads/

### Como funciona:
Temos duas aplicações:
- Servidor
- Cliente

A aplicacao Cliente consegue enviar arquivos para o Servidor, bem como fazer o download dos arquivos do Servidor.
A partir do Cliente também é possivel listar todos os arquivos que se encontram no diretório do Servidor.

### Como utilizar:
#### 1- Vá até a pasta raiz do projeto.
#### 2-	Rode o servidor no terminal com o comando:
	python SocketServer/SocketServer.py

#### 3- Rode o cliente no terminal com o comando:
	python SocketClient/SocketClient.py

#### 4- A partir da janela da aplicacao cliente, é possivel selecionar as opcoes:
- Listar arquivos do servidor.
- Baixar um arquivo do servidor.
- Enviar um arquivo ao servidor.
- Sair
