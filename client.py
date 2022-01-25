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
    
   elif ch=='2':
    c.send(bytes("2","utf-8"))
    f=input("Enter name of file:")
    c.send(bytes(f,"utf-8"))
    text=input("Enter the text to be added:")
    c.send(bytes(text,"utf-8"))
    print(c.recv(1024).decode())
    print("\n")
    
   elif ch=='3':
     c.send(bytes("3","utf-8"))
     f=input("Enter name of the file:")
     c.send(bytes(f,"utf-8"))
     print(c.recv(1024).decode())
     print("\n")

    elif ch=='4':
      c.send(bytes("4","utf-8"))
      f=input("Enter name of the file:")
      c.send(bytes(f,"utf-8"))
      print(c.recv(1024).decode())
      print("\n")
      
     elif ch='5':
      c.send(bytes("5","utf-8"))
      print("Connection has been disconnted")
      quit()
      
     else:
      print("Please enter a valid choice!!")
