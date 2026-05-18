"""
PROJECT: The Multi-User Chat Room Simulator

Goal: Build a multi-threaded Chat Server that allows multiple clients to connect simultaneously,
send messages, and have those messages broadcast to every other connected user.

Requirements:

1. The Chat Server ('ChatServer' class):
   - Keeps track of all active client sockets in a list or set.
   - Listens on a port (e.g., 55555).
   - For every client that connects, it starts a NEW thread running 'handle_client(client_socket, address)'.
   - 'handle_client' listens for messages in a loop. When a message is received, it calls 'broadcast(message, sender_socket)'.
   - 'broadcast(message, sender_socket)' sends the message to every active socket *except* the sender.
   - Handles client disconnection gracefully by removing them from the active list and closing their socket.

2. The Chat Client ('ChatClient' class):
   - Connects to the Chat Server.
   - Prompts the user for a "Username".
   - Starts a background thread to continuously receive messages from the server and print them.
   - The main thread runs a loop prompting the user for input and sending messages to the server.

How to Test:
1. Implement the classes below.
2. Run the server script in one terminal: python project.py --server
3. Open one or more new terminals and run: python project.py --client
4. Type messages in different client terminals and watch them broadcast!

Real-World Logic:
- This is how apps like Discord, WhatsApp, or IRC chat channels work. A central socket server coordinates connections, handles threading, and relays messages to keep everyone in sync!
"""

import socket
import threading
import sys

# Default Host and Port
HOST = "127.0.0.1"
PORT = 55555

class ChatServer:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.clients = []  # Keep track of active client connections
        self.lock = threading.Lock() # Protect the clients list from race conditions

    def broadcast(self, message, sender_socket):
        """Sends a message to all clients except the sender."""
        disconnected = []
        with self.lock:
            for client in self.clients:
                if client != sender_socket:
                    try:
                        client.sendall(message)
                    except Exception:
                        # Client might have disconnected abruptly
                        disconnected.append(client)

        # Remove dead clients AFTER releasing the lock to avoid deadlock
        for client in disconnected:
            self.remove_client(client)

    def remove_client(self, client_socket):
        """Removes a client from the active list."""
        with self.lock:
            if client_socket in self.clients:
                self.clients.remove(client_socket)
                client_socket.close()

    def handle_client(self, client_socket, addr):
        """Handles communication with a single client in a dedicated thread."""
        print(f"[SERVER] New connection from {addr}")
        
        # TODO: Implement client greeting, receive loop, and broadcast logic.
        # 1. Add client_socket to self.clients (thread-safe!)
        # 2. Receive messages in a loop: client_socket.recv(1024)
        # 3. If no data received, client disconnected. Break and clean up.
        # 4. Broadcast the received message to everyone else.
        # 5. Clean up: remove the client and close the socket.
        with self.lock:
            self.clients.append(client_socket)
        
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                self.broadcast(data, client_socket)
        except Exception as e:
            print(f"[SERVER] Error: {e}")
        finally:
            self.remove_client(client_socket)
            print(f"[SERVER] Connection closed for {addr}")

    def start(self):
        """Starts the server and listens for incoming connections."""
        self.server_socket.bind((HOST, PORT))
        self.server_socket.listen()
        print(f"[SERVER] Chat Server is running on {HOST}:{PORT}...")
        
        try:
            while True:
                client_socket, addr = self.server_socket.accept()
                # Start a new thread to handle this client
                t = threading.Thread(target=self.handle_client, args=(client_socket, addr), daemon=True)
                t.start()
        except KeyboardInterrupt:
            print("\n[SERVER] Server shutting down.")
        finally:
            # Clean up all client connections on shutdown
            with self.lock:
                for client in self.clients:
                    client.close()
                self.clients.clear() # clear the list
            self.server_socket.close()

class ChatClient:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def receive_messages(self):
        """Listens continuously for messages from the server in a separate thread."""
        # TODO: Implement loop to receive bytes from server, decode, and print.
        # If server closes connection, handle it gracefully.
        try:
            while True:
                data = self.client_socket.recv(1024)
                if not data:
                    break
                # Print message; \r helps clean up the input prompt overlap
                print(f"\r{data.decode('utf-8')}\n> ", end="")
        except Exception as e:
            print(f"[CLIENT] Error: {e}")

    def start(self):
        """Connects to the server, starts receiving thread, and handles user input."""
        try:
            self.client_socket.connect((HOST, PORT))
            print(f"[CLIENT] Connected to Chat Server at {HOST}:{PORT}")
            
            username = input("Enter your username: ").strip()
            
            # Start background thread to listen to incoming server messages
            receive_thread = threading.Thread(target=self.receive_messages, daemon=True)
            receive_thread.start()
            
            # TODO: Loop to take user input, prepend username (e.g. "username: message"),
            # encode to bytes, and send to the server.
            # Exit loop if user types 'exit' or '/quit'.
            while True:
                message = input("> ").strip()
                if message.lower() in ["exit", "/quit"]:
                    break
                if message:
                    self.client_socket.sendall(f"{username}: {message}".encode("utf-8"))
        except Exception as e:
            print(f"[CLIENT] Error connecting to server: {e}")
        finally:
            self.client_socket.close()
            print("[CLIENT] Disconnected.")

if __name__ == "__main__":
    # We allow running as server or client based on CLI args
    if len(sys.argv) > 1 and sys.argv[1] == "--server":
        server = ChatServer()
        server.start()
    elif len(sys.argv) > 1 and sys.argv[1] == "--client":
        client = ChatClient()
        client.start()
    else:
        print("Usage:")
        print("  To run Server: python project.py --server")
        print("  To run Client: python project.py --client")
        # run server: python 13_networking_web_basics/sockets_basics/project.py --server
        # run client: python 13_networking_web_basics/sockets_basics/project.py --client
        # run client: python 13_networking_web_basics/sockets_basics/project.py --client
        # run client: python 13_networking_web_basics/sockets_basics/project.py --client
        
