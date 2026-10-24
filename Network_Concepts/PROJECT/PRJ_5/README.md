# Section 5: Project: HTTP Client and Server


## 5.1 HTTP Summary
* **Request Structure**: Consists of a request line (`GET /path HTTP/1.1`), header fields (`Host: example.com`, `Connection: close`), and a terminating blank line (`\r\n\r\n`).
* **Line Delimiters**: Every header line must end strictly with a Carriage Return/Linefeed pair (`\r\n`).
* **Response Structure**: Consists of a status line (`HTTP/1.1 200 OK`), headers (`Content-Type`, `Content-Length`, `Connection`), a blank line (`\r\n\r\n`), and the payload data.

---

## 5.1 The Client
* **Execution**: Accepts host and optional port arguments from the command line (defaults to port 80).
* **Workflow**:
  1. Creates a socket object `s = socket.socket()`.
  2. Connects to `(host, port)` using `s.connect()`, which handles DNS resolution automatically .
  3. Sends the HTTP GET request using `s.sendall()` .
  4. Calls `s.recv()` in a loop to receive data chunks into a buffer until `recv()` returns 0 bytes (indicating the connection was closed by the server).
  5. Prints the HTTP response headers and body, then closes the socket with `s.close()`.

---

## 5.2 The Server 
* **Execution**: Listens on a default port (such as 28333) or a port specified via the command line.
* **Workflow**:
  1. Creates a listening socket and binds it to `('', port)` using `s.bind()`.
  2. Calls `s.listen()` and enters an infinite loop accepting connections.
  3. Calls `s.accept()` to obtain a new client socket [14, 15].
  4. Reads the client request in a loop using `recv()` until detecting the header delimiter `\r\n\r\n`.
  5. Transmits a hardcoded HTTP response payload using `sendall()` and closes the client connection.

---

## 5.6 Hints and Troubleshooting
* **Address Already In Use**: Waiting or selecting a different port .
* **Receiving Partial Data**: `recv()` does not guarantee returning all requested bytes in a single call; data must be accumulated in a loop.
* **HTTP 301 / 302 Redirects**: Returned when a requested resource has moved, accompanied by a `Location:` header indicating the new URL.
* **HTTP 400 / 500 Errors**: Indicate malformed request headers or missing `\r\n\r\n` delimiters.
* **HTTP 404 Not Found**: Occurs if the `Host:` header is incorrect or the resource does not exist.