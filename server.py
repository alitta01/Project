import socket
import os


def bind_socket():
    try:
        global SERVER
        global PORT
        global server_sock

        SERVER = socket.gethostbyname(socket.gethostname())
        print(SERVER)
        PORT = 8089
        ADDR = (SERVER, PORT)
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_sock.bind(ADDR)
        server_sock.listen(3)
        print('Waiting for connections')
    except:
        print("[ERROR] ")
        bind_socket()


def socket_accept():
    conn, addr = server_sock.accept()
    print("[Connected Sucessfully] :")
    communication(conn)


def communication(conn):
    while True:
        a = ((conn.recv(1024)).decode()).strip()
        if(a.startswith('create')):
            file = a[7:].strip()
            try:
                f = open(file, "x")
                content = '[SUCCESS] File Created'
            except:
                content = '[ERROR] File Not Created'
            f.close()
            print("\n")
        elif(a.startswith('read')):
            file = a[5:].strip()
            try:
                f = open(file, "r")
                content = f.read()
            except:
                content = '[ERROR] File cannot be Found'
            f.close()
            print("\n")
        elif(a.startswith('edit')):
            file = a[5:].strip()
            try:
                f = open(file, "a")
                req = (conn.recv(1024)).decode()
                f.write(req)
                content = '[SUCCESS] File Edited with :'+req
            except:
                content = '[ERROR] File cannot be Found'
            f.close()
            print("\n")
        elif(a.startswith('delete')):
            file = a[7:].strip()
            if os.path.exists(file):
                os.remove(file)
                content = '[SUCCESS] File Deleted'
            else:
                content = '[ERROR] File Cannot be Found'
            print("\n")
        elif(a.startswith('quit')):
            conn.close()
            server_sock.close()
            print("[SUCCESS] CLOSING THE CONNECTION !")
            quit()
        else:
            content = '[ERROR] Invalid Command'
        print(content)
        conn.send(bytes(content, "utf-8"))


bind_socket()
socket_accept()