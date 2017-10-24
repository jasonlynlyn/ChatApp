import socket
import handlers as h

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 50000)
sock.connect(server_address)

h.installSignalHandler(lambda: sock.close())

message = raw_input('---->')
while True:
    sock.send(message)
    data = sock.recv(1024)
    print 'Receiving from server: ' + str(data)
    message = raw_input('--->')
  
sock.close()
