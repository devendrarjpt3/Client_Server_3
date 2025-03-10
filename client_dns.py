#at client code

import socket

host = "server.cclinux3.com"
port = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

data = client.recv(1024)
print("Received:", data.decode())
client.close()
