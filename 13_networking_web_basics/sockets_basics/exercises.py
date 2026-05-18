"""
EXERCISES: The Socket Engineer

EXERCISE 1: The Uppercase Echo
1. Implement a server-client exchange where:
   - The client sends a string.
   - The server receives it, converts it to UPPERCASE, and sends it back.
   - Complete 'run_uppercase_server' and 'run_uppercase_client' below.

EXERCISE 2: The Port Scanner
1. Write a function 'scan_port(host, port)' that:
   - Creates a socket with a timeout of 0.5 seconds.
   - Uses 'connect_ex((host, port))' to try to connect.
   - If the return value is 0, the port is OPEN. Otherwise, it is CLOSED.
   - Return True if open, False if closed.

EXERCISE 3: Structured Data over Sockets (JSON)
1. Write two helper functions:
   - 'send_json(sock, dict_data)': Converts dict to JSON string, encodes to bytes, and sends.
   - 'recv_json(sock)': Receives bytes, decodes, and parses back to a Python dict.
"""

import socket
import json
import threading
import time

HOST = "127.0.0.1"
PORT_EX1 = 65433

# --- Exercise 1: Uppercase Echo ---

def run_uppercase_server():
    # TODO: Implement a server that accepts ONE connection,
    # receives a message, converts it to uppercase, sends it back, and closes.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT_EX1))
    server_socket.listen(1)
    print(f"[SERVER] Listening on {HOST}:{PORT_EX1}...")
    
    client_conn, client_addr = server_socket.accept()
    print(f"[SERVER] Connected by client at {client_addr}")
    
    with client_conn:
        while True:
            data = client_conn.recv(1024)
            if not data:
                break
            
            message = data.decode("utf-8")
            print(f"[SERVER] Received: '{message}'")
            
            reply = message.upper()
            client_conn.sendall(reply.encode("utf-8"))
            
    server_socket.close()
    print("[SERVER] Shut down.")

def run_uppercase_client():
    # TODO: Implement a client that connects, sends a lowercase message,
    # receives the uppercase reply, and prints it.
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT_EX1))
    print("[CLIENT] Connected!")
    
    message = "hello, socket server!"
    client_socket.sendall(message.encode("utf-8"))
    print(f"[CLIENT] Sent: '{message}'")
    
    data = client_socket.recv(1024)
    print(f"[CLIENT] Received from Server: '{data.decode('utf-8')}'")
    
    client_socket.close()
    print("[CLIENT] Closed connection.")


# --- Exercise 2: Port Scanner ---

def scan_port(host, port):
    # TODO: Implement a simple port scanner using socket.connect_ex()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(0.5)
    result = client_socket.connect_ex((host, port))
    client_socket.close()
    return result == 0


# --- Exercise 3: JSON Over Sockets ---

def send_json(sock, dict_data):
    # TODO: Serialize dict to JSON, encode to bytes, and send
    json_string = json.dumps(dict_data)
    sock.sendall(json_string.encode("utf-8"))

def recv_json(sock):
    # TODO: Receive bytes, decode, and parse to dictionary
    data = sock.recv(1024)
    return json.loads(data.decode("utf-8"))


if __name__ == "__main__":
    # Test Exercise 1
    t = threading.Thread(target=run_uppercase_server, daemon=True)
    t.start()
    time.sleep(0.5)
    run_uppercase_client()
    
    # Test Exercise 2
    print("Is local port 80 open?", scan_port("127.0.0.1", 80))

    # Test Exercise 3
    