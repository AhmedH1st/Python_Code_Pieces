import socket
import threading

HEADER = 64
Server_PORT = 8000
LOCAL_HOST = '127.0.0.1'
Server_ADDR = (LOCAL_HOST, Server_PORT)
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(Server_ADDR)


def handle_client(conn, addr, client_num):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg = conn.recv(2048).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False
        print(f"[{addr}] {msg}")
        conn.send((f"Msg received..client[{client_num}]".encode(FORMAT)))

    conn.close()


def start():
    client_num = 1
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(
            target=handle_client, args=(conn, addr, client_num))
        thread.start()
        client_num += 1


print("[STARTING] server is starting...")
start()
