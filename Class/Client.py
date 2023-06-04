import socket
c = socket.socket()
c.connect(('localhost', 9999)) # 192.168.1.63
print(c.recv(1024).decode())
while True:
    t = input("Enter your msg : ")
    c.send(bytes(t,'utf-8'))
    print(c.recv(1024).decode())