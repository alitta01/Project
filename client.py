import socket

PORT = 8089
HOST = socket.gethostbyname(socket.gethostname())
ADDR = (HOST, PORT)
client_sock = socket.socket()
client_sock.connect(ADDR)

print("\n { OPERATIONS } \n1 $create\n2 $edit\n3 $read\n4 $delete\n5 $quit\n")
print("[SYNTAX] : OPERATIONS filename.extention \n")
print("[NOTE] : for 'quit' just type quit \n")
while True:
    cmd = input("command:")
    client_sock.send(bytes(cmd, "utf-8"))
    if(cmd.startswith("edit")):
        req = input("Enter the string to be added:")
        client_sock.send(bytes(req, "utf-8"))
    elif(cmd == 'quit'):
        client_sock.close()
        print(". . . . CLOSING THE CONNECTION !")
        print("[SUCESS]  Closed the Connection")
        quit()
    content = (client_sock.recv(1024)).decode()
    print(content)
    print("\n")