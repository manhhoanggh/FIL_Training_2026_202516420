# Section 9: Project: A Better Web Serve
## 1. Project Goal & Overview
* **Static File Web Server:** Builds upon basic socket programming to construct a functional HTTP web server capable of serving real files (`.html`, `.txt`, etc.) to standard web browsers like Chrome or Firefox .

---

## 2. Server Request Handling Process
When a web browser requests a URL (e.g., `http://localhost:33490/file2.html`):
1. **Receive & Parse Header:** Reads the incoming request data line-by-line until encountering the empty line.
2. **Extract Method & Path:** Decodes the request with `ISO-8859-1` and splits the request line (`GET /file2.html HTTP/1.1`) to retrieve the requested filename.
3. **Path Stripping (Security):** Strips path hierarchy down to the bare filename (e.g., using `os.path.split()` or `.split('/')[-1]`) to prevent directory traversal attacks (such as requesting `/etc/passwd`) [4, 7].
4. **MIME Type Mapping:** Inspects file extensions (via `os.path.splitext()`) to set the `Content-Type` header (`.html`, `.txt`).
5. **Read File & Calculate Length:** Opens the requested file in binary mode (`"rb"`), reads its bytes, and sets `Content-Length` to the total byte count (`len(data)`).
6. **Construct & Send HTTP Response:** Sends the HTTP header followed by a blank line (`\r\n\r\n`) and the raw binary payload back over the socket.
7. **Handle 404 Not Found:** If opening the file raises an exception (file does not exist), the server returns an `HTTP/1.1 404 Not Found` response.