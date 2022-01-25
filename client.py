import socket

c=socket.socket()
c.connect(('localhost',9999))
print(c.recv(1024).decode())

while True:
  ch=input("1.Create File\n2.Edit File\n3.Delete File\n4.Read file\n5.End the connection\nEnter your choice:")
  if ch=='1':
    c.send(bytes("1","utf-8"))
    f=input("Enter name of the file:")
    c.send(bytes(f,"utf-8"))
    print(c.recv(1024).decode())
    print("\n")
    
   if ch=='2':
    c.send(bytes("2","utf-8"))
    f=input("Enter name of file:")
    c.send(bytes(f,"utf-8"))
    text=input("Enter the text to be added:")
    
