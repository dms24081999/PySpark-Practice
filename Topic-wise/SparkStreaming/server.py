import socket
from random import randint

host = 'localhost'
port = 8000
address = (host, port)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(address)
server_socket.listen(1)


print ("Listening for client . . .")
conn, address = server_socket.accept()
print ("Connected to client at ", address)
#pick a large output buffer size because i dont necessarily know how big the incoming packet is
while True:
    try:
        output = input() + "\n"
        conn.send(output.encode('utf-8'))
    except socket.error:
        print ("Error Occured.")
        break
  
conn.close()  