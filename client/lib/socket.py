import sys
import socket

ADDRESS = "127.0.0.1"
PORT = 1313

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ADDRESS, PORT))
except Exception as e:
    print(e)
    sys.exit(1)
