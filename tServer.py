import socket
import handlers as h

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

h.installSignalHandler(lambda: sock.close())

server_address = ('localhost', 50000)
sock.bind(server_address)
sock.listen(1)
conn, address = sock.accept()
print 'Connection from: ' + str(address)

while True:
    data = conn.recv(1024)
    if not data: break
    print 'Receiving data from: ' + str(data)
    conn.send(data)

sock.close()
