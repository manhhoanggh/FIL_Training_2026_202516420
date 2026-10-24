# Section 7: IPv4

## 1. IPv4 Addressing
* **Structure:** ["dots and numbers"][`192.168.1.1`].
* **Size:** Contains 4 bytes ranging from 0 to 255 (`00000000` to `11111111`).
```
  24 network bits         | 8 host bits
-------------------------------+---------
11000110 . 00110011 . 01100100 . 00000000
     198         51        100          0

```
---

## 2. Subnets & Slash Notation
* **Subnet Split:** The IP address is split into a **network portion** (initial bits) and a **host portion** (remaining bits).
* **Slash Notation:** Specifies how many bits represent the network portion (e.g., `/24` means 24 network bits and 8 host bits).
* **Flexible Bit Boundaries:** Subnets do not have to align on byte boundaries; for example, a `/28` subnet leaves 4 host bits, offering 16 total IPs (14 usable hosts and 2 reserved).
* **Subnetting Down:** Networks can be further divided into smaller subnets by reserving additional bits for the network portion.
```
           28 network bits           | 4 host bits
-------------------------------------+----
11000110 . 00110011 . 01100100 . 0110 0010
     198         51        100          98
```
---

## 3. Subnet Masks
* **Definition:** IP-like address with `1`s for all network bits and `0`s for host bits .
* **Subnet Identification:** A router determines an IP address's subnet by performing a **bitwise-AND** operation between the IP address and the subnet mask.
```
 24 network bits         | 8 host bits
  -------------------------------+---------
  11000110 . 00110011 . 01100100 . 01000011    198. 51.100.67
& 11111111 . 11111111 . 11111111 . 00000000  & 255.255.255. 0
-------------------------------------------  ----------------
  11000110 . 00110011 . 01100100 . 00000000    198. 51.100. 0
```
---

## 5. Special IP Addresses
* **`[127.0.0.1]`:** Localhost.
* **`0.0.0.0`:** Reserved network address.
* **`255.255.255.255`:** Global broadcast address.
* **Subnet Broadcast Address:** Broadcast to your local subnet by sending to the host with all bits set to 1. 