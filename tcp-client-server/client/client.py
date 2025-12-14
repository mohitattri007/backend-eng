print("CLIENT STARTED")

import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 8888

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((SERVER_IP, SERVER_PORT))
print("[CLIENT] Connected to server")

while True:
    msg = input("Enter message (or 'exit'): ")
    if msg.lower() == "exit":
        break

    try:
        client_socket.sendall(msg.encode())
        data = client_socket.recv(1024)
        print(data)
        print("[CLIENT] Received: sda", data.decode())
    except BrokenPipeError:
        print("[CLIENT] Server closed the connection")
        break
