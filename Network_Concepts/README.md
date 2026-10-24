# Section 2: Networking Overview - Summary & Notes

## 1. Core Networking Concepts

### 1.1 Fundamentals of Network Communication
- Goal: exchange arbitrary bytes of data between computers over a LAN/Internet.
 - This requires mechanisms for identification, routing, data integrity, and supporting things involved.

### 1.2 Circuit-Switched vs. Packet-Switched Networks
* **Circuit-Switched Networks**: Establish a dedicated physical connection for the entire duration of a call or session (e.g., traditional telephone lines) [2, 3].
  * *Drawbacks*: Inefficient line utilization, lack of traffic multiplexing, and physical scaling limits due to line reservation even during idle moments [3].
* **Packet-Switched Networks**: Divide data into discrete packets that share physical lines and are routed independently [4, 5].
  * *Advantages*: Multiple devices can send interleaved packets across shared wires simultaneously, maximizing bandwidth efficiency without requiring dedicated end-to-end circuits [5].

---

## 2. Architecture & Abstraction

### 2.1 Client/Server Architecture
* **Server**: A network process that sits idle waiting for incoming connections, accepts them, processes client requests, and transmits responses [6, 7].
* **Client**: A network program that actively initiates a connection to a server to request data or services [6].

### 2.2 The OS & Sockets API
Application programs cannot interact directly with physical network hardware; the Operating System manages all hardware resources [7]. Applications communicate over the network through system calls provided by the **sockets API**, pioneered on Unix systems [7, 8].

### 2.3 Protocols & Protocol Stacks
A **protocol** defines the strict formatting, sequence, and rules governing data exchange between devices [9].
* Common protocols include **TCP** (reliable transport), **UDP** (lightweight transport), **IP** (routing across networks), **HTTP** (web requests), and **Ethernet** (LAN delivery) [10].
* Data is passed down through a **protocol stack**, where each layer prepends its own header to the payload (**Data Encapsulation**) [11, 12].
* Lower layers remain agnostic to the contents of the payload they wrap, allowing protocol substitution across layers without affecting application code [13, 14].

### 2.4 Wired vs. Wireless (WiFi)
Wired networks (Ethernet cables) and wireless networks (WiFi) operate on the same LAN using Ethernet protocol structures at the link layer [15]. The distinction lies in the physical medium: wired networks transmit electrical signals over copper wires, whereas WiFi transmits radio signals through the air [15].

---

## 3. Reflection Answers (Section 2.8)

1. **Is the Internet circuit-switched or packet-switched?**
   The Internet is a **packet-switched network**, breaking data into discrete packets transmitted over shared lines [4].

2. **What is the relationship between a client program and a server program?**
   A server waits for connections and responds to requests, while a client actively connects to the server to request services [6].

3. **What role does the OS play when you’re writing networked programs?**
   The OS controls all network hardware access and provides the **sockets API** through which application code executes network communications [7].

4. **What is a protocol?**
   A protocol is a strictly defined set of rules specifying the byte format, ordering, and timing of data exchanged between endpoints [9].

5. **What are the reasons for having a protocol stack and data encapsulation?**
   It enforces modularity and separation of concerns. Each layer handles a distinct responsibility (e.g., routing, data integrity, physical delivery) without needing to know the details of other layers [12, 13].

6. **What are the practical differences between a WiFi network and a wired network?**
   Both use Ethernet protocol rules on a LAN, but wired networks send electrical signals over cables while WiFi transmits radio waves over the air [15].