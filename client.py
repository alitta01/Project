import socket

c = socket.socket()
c.connect(('localhost', 9999))
print(c.recv(1024).decode())

while True:
    ch = input(
        "1. Create file\n 2. Edit file\n 3. Delete file\n 4. Read a file\n 5. End connection\n Enter a choice: ")

    if ch == "1":
        c.send(bytes("1", "utf-8"))
        file = input("Enter file name: ")
        c.send(bytes(file, "utf-8"))
        print(c.recv(1024).decode())
        print("\n")
    
    elif ch == "2":
        c.send(bytes("2", "utf-8"))
        file = input("Enter file name: ")
        c.send(bytes(file, "utf-8"))
        file_text = input("Enter the text to be added: ")
        c.send(bytes(file_text, "utf-8"))
        print(c.recv(1024).decode())
        print("\n")

    elif ch == "3":
        c.send(bytes("3", "utf-8"))
        file = input("Enter file name: ")
        c.send(bytes(file, "utf-8"))
        print(c.recv(1024).decode())
        print("\n")

    elif ch == "4":
        c.send(bytes("4", "utf-8"))
        file = input("Enter file name: ")
        c.send(bytes(file, "utf-8"))
        print(c.recv(1024).decode())
        print("\n")

    elif ch == "5":
        c.send(bytes("5", "utf-8"))
        print("The connection has been ended.")
        quit()

    else:
        print("Invalid choice!")
