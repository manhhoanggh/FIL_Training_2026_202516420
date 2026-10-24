import sys
import socket

port = int(sys.argv[1]) if len(sys.argv) > 1 else 28333

s = socket.socket()

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(('', port))

s.listen()

print(f"Server listening on port {port}...")

# 6. Infinite loop to handle incoming client connections indefinitely
while True:
    # Accept incoming connection (blocks until a client connects)
    new_socket, client_addr = s.accept()
    print("accept() returned:", new_socket, client_addr)

    # Receive HTTP request from client until double CRLF (\r\n\r\n) is found
    request_data = b""
    while b"\r\n\r\n" not in request_data:
        data = new_socket.recv(1024)
        if not data:
            break
        request_data += data

    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/plain\r\n"
        "Content-Length: 6\r\n"
        "Connection: close\r\n"
        "\r\n"
        "Hello!"
    )

    new_socket.sendall(response.encode("ISO-8859-1"))
    new_socket.close()
