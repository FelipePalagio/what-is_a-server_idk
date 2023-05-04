import socket

cli = socket.socket()
portera = 12345
cli.connect((socket.gethostbyname(socket.gethostname()), portera))
zaza = cli.recv(1024).decode()
print(zaza)
cli.close()
