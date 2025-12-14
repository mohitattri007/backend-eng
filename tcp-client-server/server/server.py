import socket

HOST = "0.0.0.0"   # listen on all interfaces
PORT = 8888

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Allow quick restart
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("ffffff")
server_socket.bind((HOST, PORT))
print("ffffff")
server_socket.listen()

print(f"[SERVER] Listening on {HOST}:{PORT}")

while True:
    conn, addr = server_socket.accept()
    print(f"[SERVER] Connected by {addr}")

    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                print(f"[SERVER] Connection closed by {addr}")
                break

            message = data.decode()
            print(f"[SERVER] Received: {message}")

            response = f"Echo: {message}"
            conn.sendall(response.encode())
