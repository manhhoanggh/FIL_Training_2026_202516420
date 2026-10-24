import socket
import time

def system_seconds_since_1900():

    seconds_delta = 2208988800
    seconds_since_unix_epoch = int(time.time())
    seconds_since_1900_epoch = seconds_since_unix_epoch + seconds_delta
    return seconds_since_1900_epoch

def main():
    # 1. Connect to NIST server on port 37 using a TCP socket
    s = socket.socket()
    s.connect(("time.nist.gov", 37))

    # 2. Receive 4 bytes directly without a loop, then close socket
    data = s.recv(4)
    s.close()

    # 3. Decode 4-byte big-endian integer
    nist_time = int.from_bytes(data, "big")

    # 4 & 5. Print out NIST time and local system time
    print(f"NIST time  : {nist_time}")
    print(f"System time: {system_seconds_since_1900()}")

if __name__ == "__main__":
    main()