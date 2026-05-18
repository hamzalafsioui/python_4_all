# Examples: A Simple TCP Echo Server and Client

import socket
import threading
import time

HOST = "127.0.0.1"  # Localhost
PORT = 65432        # Non-privileged port

def run_server():
    """Starts a TCP Echo Server that runs in a background thread."""
    # 1. Create a socket (IPv4, TCP)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2. Allow immediate reuse of the port after stopping the server
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # 3. Bind to host and port
    server_socket.bind((HOST, PORT))
    
    # 4. Listen for incoming connections
    server_socket.listen(1)
    print(f"[SERVER] Listening on {HOST}:{PORT}...")
    
    try:
        # 5. Accept an incoming connection (blocking call)
        client_conn, client_addr = server_socket.accept()
        print(f"[SERVER] Connected by client at {client_addr}")
        
        with client_conn:
            while True:
                # 6. Receive raw bytes from the client
                data = client_conn.recv(1024)
                if not data:
                    break  # Client disconnected
                
                message = data.decode("utf-8")
                print(f"[SERVER] Received: '{message}'")
                
                # 7. Echo the same message back to the client
                reply = f"Echo: {message}"
                client_conn.sendall(reply.encode("utf-8"))
                
    except Exception as e:
        print(f"[SERVER] Error: {e}")
    finally:
        server_socket.close()
        print("[SERVER] Shut down.")

def run_client():
    """Connects to the Echo Server as a Client."""
    time.sleep(1)  # Ensure the server starts first
    
    print("[CLIENT] Connecting to server...")
    # 1. Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # 2. Connect to the server
        client_socket.connect((HOST, PORT))
        print("[CLIENT] Connected!")
        
        # 3. Send a message (must be encoded to bytes!)
        message = "Hello, Socket Server!"
        client_socket.sendall(message.encode("utf-8"))
        print(f"[CLIENT] Sent: '{message}'")
        
        # 4. Receive the server's reply
        data = client_socket.recv(1024)
        print(f"[CLIENT] Received from Server: '{data.decode('utf-8')}'")
        
    except Exception as e:
        print(f"[CLIENT] Error: {e}")
    finally:
        client_socket.close()
        print("[CLIENT] Closed connection.")

if __name__ == "__main__":
    # We use threading so you can see both client and server run in the same terminal!
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    
    # Run the client in the main thread
    run_client()
    
    # Give a tiny moment for final print statements
    time.sleep(0.5)
