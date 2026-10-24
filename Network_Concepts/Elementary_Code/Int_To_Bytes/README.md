# Section 10: Endianness and Integers

## 1. Motivation & Binary Transmission
Networks transmit sequences of individual bytes.Transmitting numbers over a network as raw binary integer is more efficient than string.

---

## 2. Multi-Byte Integer Representations
* **Byte Breakdown:** Any integer can be represented by splitting its binary or hex representation into 8-bit (1-byte / 2 hex digit) chunks.


## 3. Endianness (Byte Ordering)
* **Big-Endian**
* **Little-Endian**
* **Network Byte Order:** Internet protocols standardized on **big-endian**.

---

## 4. Python Byte Conversion Methods
* **Integer to Bytes (`.to_bytes()`)**
* **Reverse (`.from_bytes()`)**


---
