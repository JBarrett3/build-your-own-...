import socket

def handle_client(client_socket, address):
    while True:
        data = client_socket.recv(1024).decode('utf-8').strip() # processes client->server data from utf-8 format
        print(f"CLI: {data}")
        if not data: # no data means disconnection
            print(f"Client at {address} disconnected")
            break
        response = "FILLER" # to be replaced
        client_socket.sendall((response + "\n").encode('utf-8')) # processes server->client data into utf-8 format
        print(f"SVR: {response} \n")
    
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creates a socket for IPV4 using TCP
    server_socket.bind(('localhost', 8000)) # binds loalhost to 8000, so a socket exists at localhost:8000
    server_socket.listen(5) # begins listening for connection requests at the socket at localhost:8000
    server_ip, server_port = server_socket.getsockname()
    print(f"SVR listening at <{server_ip}:{server_port}>")
    while True:
        client_socket, address = server_socket.accept() # triggers when a client tries to connect and responds by accepting
        client_ip, client_port = client_socket.getpeername()
        print(f"Connection established: CLI <{client_ip}:{client_port}> to SVR <{server_ip}:{server_port}>")
        handle_client(client_socket, address) # sends the new client's socket (used for communication) and address (IP and port) to be handled

if __name__ == "__main__":
    start_server()