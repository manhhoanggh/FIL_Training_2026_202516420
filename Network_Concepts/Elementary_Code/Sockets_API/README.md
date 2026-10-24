# Section 3: Introducing The Sockets API

The Sockets API provides a standardized interface. For more information, reflect to the previous topic.

---

## 3.1 Client Connection Process
Connecting a client program to a remote server involves five core steps [3, 4]:
1. **Create a Socket**: Request a socket object from the OS.
2. **DNS Lookup**: Resolve human-readable domain names (e.g., `example.com`) to IP addresses.
3. **Connect**: Establish a connection to the destination IP address on a specified port number (0–65535, e.g., port 80 for HTTP).
4. **Send & Receive Data**: Transmit sequences of bytes between endpoints.
5. **Close Connection**: Terminate the socket when transmission completes.

---

## 3.2 Server Listening Process
1. **Create a Socket**: Request a socket object from the OS.
2. **Bind to a Port**: Assign a local port number for client connections. Ports below 1024 require root/administrator privileges.
3. **Listen**: Inform the OS to monitor the bound port for incoming connection requests.
4. **Accept Connection**: Block (sleep) until an incoming connection arrives.
   * *Key Behavior*: `accept()` returns a **new socket** created specifically for that individual client connection, leaving the original socket listening for future requests [10].
5. **Send & Receive Data**: Process client requests and transmit responses over the new client socket.
6. **Loop**: Return to accept step to handle subsequent client connections.

---

## 3.3 Client API Code (Python)
```python
import socket

# 1. Create socket object
s = socket.socket()

# 2 & 3. Connect to server (performs DNS lookup automatically)
s.connect(("example.com", 80))  # Argument is a (host, port) tuple

# 4. Send and receive data
s.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
data = s.recv(1024)  # Receive up to 1024 bytes

# 5. Close connection
s.close()
```

## 3.4 Server API Code (Python)
``` python
import socket

# 1. Create listening socket
s = socket.socket()

# 2. Bind socket to address and port
s.bind(("localhost", 3490))  # "localhost" specifies the local host machine

# 3. Listen for incoming connections
s.listen()

# 4. Accept connections in a loop
while True:
    client_socket, client_addr = s.accept()  # Blocks until a client connects
    
    # 5. Send and receive data using client_socket
    data = client_socket.recv(1024)
    client_socket.sendall(b"Hello from server!")
    
    # Close specific client connection socket
    client_socket.close()

```