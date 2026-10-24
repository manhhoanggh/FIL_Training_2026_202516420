import sys
import socket
import os #os.path.slittext require it

DEFAULT_PORT = 28333

def get_mime_type(filename):
    
    _, ext = os.path.splitext(filename) # extract .html
    ext = ext.lower()   #unify caplocks
    if ext == '.html' or ext == '.htm': 
        return 'text/html'
    elif ext == '.txt':
        return 'text/plain'
    else:
        return 'application/octet-stream' #generic binary data

def run_server(port):
    """Run the web server loop on the specified port."""
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_socket.bind(('', port))
    server_socket.listen()


    while True:
        client_socket, client_address = server_socket.accept()  #sleep until client connects
        # client_socket store that client, server_socket continues listening for further connections
        
        # Accumulate request header bytes until blank line (\r\n\r\n) is reached
        request_bytes = b"" # string store received payload
        while b"\r\n\r\n" not in request_bytes:
            chunk = client_socket.recv(4096) #if not connect chuck = 0;
            if not chunk:
                break
            request_bytes += chunk
###
        if not request_bytes:  #close conntection, optional
            client_socket.close()
            continue
###
        # Decode header string using ISO-8859-1
        request_str = request_bytes.decode("ISO-8859-1")
        lines = request_str.split("\r\n")
        first_line = lines[0]
        
        # Parse the request line: GET /path/filename HTTP/1.1
        parts = first_line.split(" ") # split to array
        if len(parts) >= 2:
            method = parts[0]
            full_path = parts[1]  #store '/file2.html'
            
            # Strip path hierarchy to only serve files from current working directory
            filename = os.path.split(full_path)[-1]
            
            # Attempt to open and read the requested file in binary mode
            try: #if filename do not exist -> jump to exception
                with open(filename, "rb") as fp: # with auto handle file close
                    payload = fp.read()
                
                content_type = get_mime_type(filename)
                content_length = len(payload)
                
                # HTTP Response
                header = (
                    "HTTP/1.1 200 OK\r\n"
                    f"Content-Type: {content_type}\r\n"
                    f"Content-Length: {content_length}\r\n"
                    "Connection: close\r\n"
                    "\r\n"
                )
                
                client_socket.sendall(header.encode("ISO-8859-1") + payload)
                
            except Exception:
                # File missing or read error -> Send 404 Not Found Response
                body_404 = b"404 not found"
                header_404 = (
                    "HTTP/1.1 404 Not Found\r\n"
                    "Content-Type: text/plain\r\n"
                    f"Content-Length: {len(body_404)}\r\n"
                    "Connection: close\r\n"
                    "\r\n"
                )
                client_socket.sendall(header_404.encode("ISO-8859-1") + body_404)
        
        client_socket.close()

if __name__ == "__main__":
    port = DEFAULT_PORT
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    run_server(port)
