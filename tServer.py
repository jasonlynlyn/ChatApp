import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 50000)

s.bind(server_address)
s.listen(1)
connection, address = s.accept()
print "Connection from: " + str(address)

while True:
  data = s.recv(1024)
  print "Receiving data from: " + str(data)
  connection.send(data)
  
  connection.close()
  
