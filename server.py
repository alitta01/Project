"""import socket
import os

server = socket.socket()
server.bind(('localhost',9999))
server.listen(1)
print("Waiting for connection...")
client, address = server.accept()
print("Connected to ", address)
client.send(bytes("Connection has been established.","utf-8"))

while True:
	choice = client.recv(1024).decode()
	file = client.recv(1024).decode()
	
	if choice == "1":
		try:
			f = open(file,"x")
			client.send(bytes("File created.","utf-8"))
			f.close()
		except:
			client.send(bytes("File already exists.","utf-8"))

	elif choice == "2":
		try:
			os.remove(file)
			client.send(bytes("File deleted.","utf-8"))
		except:
			client.send(bytes("File does not exist.","utf-8"))

	elif choice == "3":
		try:
			f = open(file,"a")
			edit_text = client.recv(1024).decode()
			f.write(edit_text)
			client.send(bytes("File edited.","utf-8"))
			f.close()
		except:
			client.send(bytes("File does not exist.","utf-8"))

	elif choice == "4":
		try:
			f = open(file,"r")
			file_content = f.read()
			if file_content == "":
				client.send(bytes("File is empty.","utf-8"))
			else:
				client.send(bytes(file_content,"utf-8"))
			f.close()
		except:
			client.send(bytes("File does not exist.","utf-8"))
      
	elif choice == "5":
		print("The connection has been ended.")

client.close()
"""
import socket
import os

SERVER = socket.socket()
SERVER.bind(('localhost', 9999))
SERVER.listen(3)
print("Waiting for connection...")
CLIENT, address = SERVER.accept()
print("Connected to ", address)
CLIENT.send(bytes("Connection has been established.", "utf-8"))

while True:
    choice = CLIENT.recv(1024).decode()
    file = CLIENT.recv(1024).decode()

    if choice == "1":
        try:
            f = open(file, "x")
            CLIENT.send(bytes("File created.", "utf-8"))
            f.close()
        except:
            CLIENT.send(bytes("File already exists.", "utf-8"))

    elif choice == "2":
        try:
            os.remove(file)
            CLIENT.send(bytes("File deleted.", "utf-8"))
        except:
            CLIENT.send(bytes("File does not exist.", "utf-8"))

    elif choice == "3":
        try:
            f = open(file, "a")
            edit_text = CLIENT.recv(1024).decode()
            f.write(edit_text)
            CLIENT.send(bytes("File edited.", "utf-8"))
            f.close()
        except:
            CLIENT.send(bytes("File does not exist.", "utf-8"))

    elif choice == "4":
        try:
            f = open(file, "r")
            file_content = f.read()
            if file_content == "":
                CLIENT.send(bytes("File is empty.", "utf-8"))
            else:
                CLIENT.send(bytes(file_content, "utf-8"))
            f.close()
        except:
            CLIENT.send(bytes("File does not exist.", "utf-8"))

    elif choice == "5":
        print("The connection has been ended.")

CLIENT.close()