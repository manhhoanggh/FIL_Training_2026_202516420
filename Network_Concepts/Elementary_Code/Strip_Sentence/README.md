# Section 11: Parsing Packets

## 1. The Stream vs. Packet Problem
* **Stream Behavior:** TCP is a continuous byte stream. Calling `recv(4096)` does not guarantee receiving a full packet; it might return only a few bytes (a partial packet) or multiple packets concatenated together.

---

## 2. Packet Abstraction
* **Goal:** Abstracting byte-stream handling into a dedicated function (e.g., `get_next_packet()`).

---

## 3. The Global Buffer Strategy.
* **In-Memory Processing Steps:**
  1. Inspect the buffer to determine if it contains a complete packet.
  2. **If complete:** Extract the packet, slice it off the front of the buffer (e.g., `buffer = buffer[packet_length:]`), and return the packet.
  3. **If incomplete:** Call `recv()` to fetch more data, append the new bytes to the buffer.
* **Python Usage:** Use the `global` keyword inside helper functions when modifying a global buffer.

---

## 4. Generic Packet Parsing Algorithm
```python
global buffer = b''

function get_next_packet(socket):
    global buffer
    while True:
        if (contains complete packet) = True:
            packet = buffer[:packet_length]
            buffer = buffer[packet_length:]
            return packet
        data = socket.recv(4096)
        if len(data) == 0:
            return None
        buffer += data