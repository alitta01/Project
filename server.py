import socket
import os

s=socket.socket()
s.bind(('localhost,9999))
s.listen(1)
print("Waiting for connection....")

while True:
       c,addr=s.accept()
       print("Connected to ",addr)
       c.send(bytes("Connection successful","utf-8"))
       ch=c.recv(1024).decode()
       file=c.recv(1024).decode()
        if ch=='1':
              try:
                    f=open(file,"x")
                    c.send(bytes("File created","utf-8"))
                    f.close()
               except:
                     c.send(bytes("File already exists","utf-8"))
         elif ch=='2':
                try:
                       f=open(file,"a")
                       text=c.recv(1024).decode()
                       f.write(text)
                       c.send(bytes("File has been edited","utf=8"))
                        f.close()
                  except:
                         c.send(bytes("File not found!!!","utf-8")
           elif ch=='3':
                   try:
                          os.remove(file)
                          c.send(bytes("File has been deleted","utf-8"))
                    except:
                           c.send(bytes("File not found!!!","utf-8"))
             elif ch=='4':
                      try:
                            f=open("file","r")
                             note=f.read()
                             if note=="":
                                  c.send(bytes("File is empty","utf-8"))
                             else:
                                   c.send(bytes(note,"utf-8"))
                                   f.close()
                        except:
                              c.send(bytes("File not found!!!","utf-8"))
               elif ch=='5':
                       c.send(bytes("connection has ended","utf-8"))
c.close()
