# Sockets Basics: Low-Level Networking

So far, we've used high-level protocols like HTTP (via `requests`, `FastAPI`, and `Flask`). But how do computers actually transmit raw bytes across the internet? Under the hood, everything relies on **Sockets**.

---

## 1. What is a Socket?
A socket is an endpoint in a two-way communication channel between two programs running on a network.
- Think of an IP address as a **building's address**, and a Port number as a **specific apartment** or door inside that building.
- A socket combines `(IP Address, Port Number)` to establish a direct connection.

---

## 2. Key Protocols: TCP vs. UDP
Sockets generally operate using one of two transport layer protocols:

| Feature | TCP (Transmission Control Protocol) | UDP (User Datagram Protocol) |
| :--- | :--- | :--- |
| **Connection** | Connection-oriented (Handshake) | Connectionless |
| **Reliability** | Guaranteed delivery (retransmits lost data) | No guarantee (fire and forget) |
| **Speed** | Slower (due to overhead/checking) | Extremely fast |
| **Usage** | Web browsing (HTTP), Email, SSH | Video streaming, online gaming, DNS |

---

## 3. The Lifecycle of a TCP Socket

### The Server:
1. **Create**: Initialize the socket (`socket.socket()`).
2. **Bind**: Attach the socket to an IP and Port (`bind()`).
3. **Listen**: Wait for incoming client connections (`listen()`).
4. **Accept**: Establish the connection with a client (`accept()`).
5. **Send/Receive**: Exchange raw byte data (`send()`, `recv()`).
6. **Close**: Tear down the connection (`close()`).

### The Client:
1. **Create**: Initialize the socket (`socket.socket()`).
2. **Connect**: Establish a connection to the server's IP and Port (`connect()`).
3. **Send/Receive**: Exchange bytes (`send()`, `recv()`).
4. **Close**: Tear down the connection (`close()`).

---

## 4. Crucial Concept: Bytes and Encoding
Sockets send and receive **raw bytes**, not Python strings!
- To send a string, you must **encode** it into bytes: `"hello".encode("utf-8")`
- To read received bytes, you must **decode** them back to a string: `data.decode("utf-8")`

---

## 5. Basic Syntax
```python
import socket

# Create a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# AF_INET = IPv4 addresses
# SOCK_STREAM = TCP protocol
```

---

## 6. Best Practices
1. **Close your Sockets**: Always close sockets when finished, or use context managers (`with` blocks) to prevent ports from getting locked.
2. **Handle Address Already in Use**: If a server crashes, the port might remain locked for a minute. Use `s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)` before binding to bypass this.
3. **Specify Buffer Size**: When receiving data, specify a sensible chunk size (e.g., `1024` or `4096` bytes).

## Resources

- **Official Python Socket Documentation** – https://docs.python.org/3/library/socket.html
- **Real Python: Socket Programming** – https://realpython.com/python-sockets/
- **Beej's Guide to Network Programming** – https://beej.us/guide/bgnet/
- **MDN Web Docs: WebSockets Overview** – https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API
- **Python Network Programming Cookbook** – https://www.packtpub.com/product/python-network-programming-cookbook/9781785284599
