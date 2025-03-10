#at Server
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 12345))
server.listen(1)
print(f"Server listening on port ", socket.AF_INET)
while True:
    conn, add = server.accept()
    print(f"Connection from {add}")
    conn.sendall(b"Hello from server!")
conn.close()
