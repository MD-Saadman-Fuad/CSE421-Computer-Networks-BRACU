import socket
import threading

HEADER = 16
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSEGE = "End"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_clients(conn, addr):
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSEGE:
                connected = False
                conn.send("Goodbye".encode(FORMAT))

            else:
                if int(msg)<0:
                    conn.send(f"Not possible".encode(FORMAT))
                elif int(msg) <= 40:
                    salary = int(msg)*200
                    conn.send(f"{salary}".encode(FORMAT)) 
                else:
                    salary = 8000 + ((int(msg)-40)*300)
                    conn.send(f"{salary}".encode(FORMAT))
                    

            
    conn.close()


def start():
    server.listen()
    print("Server is listening")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_clients, args=(conn,addr))
        thread.start()
        #print(f"Total client's connected currently: {threading.active_count()-1} ")

start()

