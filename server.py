#a server that can be reached by many

import socket
import sys
from thread import *

HOST="
PORT=8888

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating a socket

try:
    s.bind((HOST, PORT)) #bind it
except socket.error, msg:
    print "Bind failed. Error code: " + str(msg[0]) + "message " + msg[1]
    sys.exit()

print "socket bind complete"

s.listen(10)

def clientthread(conn):
    conn.send("Welcome to the server. Type something and hit enter \n")
  
    while True:
        data=conn.recv(1024)
        reply="ok..."+data
        if not data:
            break
     
        conn.close() #close connection
 
while True:
    conn, addr=s.accept()
    print "Connected with " + addr[0] + ":" + str(addr[1])
    
    start_new_thread(clientthread, (conn,))

s.close()
