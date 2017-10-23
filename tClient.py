import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 50000)
s.connect(server_address)

message = raw_input("---->")
while True:
  s.send(message)
  data = s.recv(1024)
  print "Receiving from server: " + str(data)
  message = raw_input("--->")
  
  s.close()
