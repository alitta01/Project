"""import socket

client = socket.socket()
client.connect(('localhost',9999)) #can be given any IP address
msg=client.recv(1024).decode()
print(msg)

while True:
	choice = input("1. Create a file\n 2. Delete a file\n 3. Edit a file\n 4. Read a file\n 5. End connection\n Enter a choice: ")
	
	if choice == "1":
		client.send(bytes("1","utf-8"))
		file = input("Enter file name: ")
		client.send(bytes(file,"utf-8"))
		print_msg=client.recv(1024).decode()
		print(print_msg)
		print("\n")

	elif choice == "2":
		client.send(bytes("2","utf-8"))
		file = input("Enter file name: ")
		client.send(bytes(file,"utf-8"))
		print_msg=client.recv(1024).decode()
		print(print_msg)
		print("\n")

	elif choice == "3":
		client.send(bytes("3","utf-8"))
		file = input("Enter file name: ")
		client.send(bytes(file,"utf-8"))
		content = input("Enter the text to be added: ")
		client.send(bytes(content,"utf-8"))
		print_msg=client.recv(1024).decode()
		print(print_msg)
		print("\n")

	elif choice == "4":
		client.send(bytes("4","utf-8"))
		file = input("Enter file name: ")
		client.send(bytes(file,"utf-8"))
		print_msg=client.recv(1024).decode()
		print(print_msg)
		print("\n")

	elif choice == "5":
		client.send(bytes("5","utf-8"))
		print("The connection has been ended.")
		quit()

	else:
		print("Invalid choice!")
    """

import socket

c = socket.socket()
c.connect(('localhost', 9999))
print(c.recv(1024).decode())

while True:
    choice = input(
        "1. Create a file\n 2. Delete a file\n 3. Edit a file\n 4. Read a file\n 5. End connection\n Enter a choice: ")

    if choice == "1":
        c.send(bytes("1", "utf-8"))
        file = input("Enter file name: ")
        c.send(bytes(file, "utf-8"))
        print_msg = c.recv(1024).decode()
        print(print_msg)
        print("\n")

    elif choice == "2":
        c.send(bytes("2", "utf-8"))
        file = input("Enter file name: ")
        c.send(bytes(file, "utf-8"))
        print_msg = c.recv(1024).decode()
        print(print_msg)
        print("\n")

    elif choice == "3":
        c.send(bytes("3", "utf-8"))
        file = input("Enter file name: ")
        c.send(bytes(file, "utf-8"))
        file_text = input("Enter the text to be added: ")
        c.send(bytes(file_text, "utf-8"))
        print_msg = c.recv(1024).decode()
        print(print_msg)
        print("\n")

    elif choice == "4":
        c.send(bytes("4", "utf-8"))
        file = input("Enter file name: ")
        c.send(bytes(file, "utf-8"))
        print_msg = c.recv(1024).decode()
        print(print_msg)
        print("\n")

    elif choice == "5":
        c.send(bytes("5", "utf-8"))
        print("The connection has been ended.")
        quit()

    else:
        print("Invalid choice!")