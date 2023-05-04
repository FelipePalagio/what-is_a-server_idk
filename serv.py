import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
serv.bind(('', port))
serv.listen(5)

while True:
    print("Server is [ALIVE]...")

    zumpa, addr = serv.accept()
    print('Got connection from', addr)

    sully = "EDGERUNNER"

    zumpa.send(sully.encode())

    zumpa.close()

    break
