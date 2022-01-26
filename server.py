import socket
import os

SERVER = socket.socket()
SERVER.bind(('localhost', 9999))
SERVER.listen(3)
print("Waiting for connection...")
CLIENT, address = SERVER.accept()
print("Connected to ", address)
CLIENT.send(bytes("Connection established.", "utf-8"))

while True:
    ch = CLIENT.recv(1024).decode()
    file = CLIENT.recv(1024).decode()

    if ch == "1":
       try:
              f = open(file, "x")
              CLIENT.send(bytes("File has been created.", "utf-8"))
              f.close()
       except:
              CLIENT.send(bytes("File already exists!!!", "utf-8"))

    elif ch == "2":
       try:
            f = open(file, "a")
            text = CLIENT.recv(1024).decode()
            f.write(text)
            CLIENT.send(bytes("File edited.", "utf-8"))
            f.close()
       except:
            CLIENT.send(bytes("File does not exist.", "utf-8"))

    elif ch == "3":
       try:
            os.remove(file)
            CLIENT.send(bytes("File deleted.", "utf-8"))
       except:
            CLIENT.send(bytes("File does not exist.", "utf-8"))
    elif ch == "4":
        try:
            f = open(file, "r")
            content = f.read()
            if content == "":
                CLIENT.send(bytes("File is empty.", "utf-8"))
            else:
                CLIENT.send(bytes(content, "utf-8"))
            f.close()
        except:
            CLIENT.send(bytes("File does not exist.", "utf-8"))

    elif ch == "5":
        print("The connection has been ended.")

CLIENT.close()