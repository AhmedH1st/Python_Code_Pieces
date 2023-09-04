import socket

PORT = 8000
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "DISCONNECT"
LOCAL_HOST = '127.0.0.1'
ADDR = (LOCAL_HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Officially connecting to the server.
client.connect(ADDR)

while True:
    msg = input()
    msg = msg.encode(FORMAT)
    client.send(msg)
    print(client.recv(2048).decode(FORMAT))
