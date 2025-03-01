import socket
import threading

HEADER = 16
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSEGE = "End"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    messege = msg.encode(FORMAT)
    msg_length = len(messege)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '* (HEADER - len(send_length))
    client.send(send_length)
    client.send(messege)
    print(client.recv(2048).decode(FORMAT))

connected = True

while connected:
    input1=input("Please enter your time: ")
    try:
        input_messege = int(input1)
        send(input1)
    except ValueError:
        if input1 == "Done":
            connected = False
            send(DISCONNECT_MESSEGE)
        else:
            print("Not a Number")