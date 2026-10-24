import sys
import socket

host = sys.argv[1]
port = int(sys.argv[2]) if len(sys.argv) > 2 else 80

s = socket.socket()

s.connect((host, port))

request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"

s.sendall(request.encode("ISO-8859-1"))

response = b""
while True:
    data = s.recv(4096)
    if len(data) == 0:
        break
    response += data

print(response.decode("ISO-8859-1"))

s.close()