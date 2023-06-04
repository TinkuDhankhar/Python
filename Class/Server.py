import socket
s = socket.socket()
print("Create new Socket")
s.bind(('localhost',9999))
s.listen(100)
print("waiting for connection...")
while True:
    c,addr = s.accept()
    print("connection stable", addr)
    c.send(bytes("Hello world","utf-8"))
    while True:
        print(c.recv(1024).decode())
        i = input("Enter your msg ")
        c.send(bytes(i,'utf-8'))
    c.close()