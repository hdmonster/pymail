import socket

HOST = "127.0.0.1"
PORT = 1313

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
