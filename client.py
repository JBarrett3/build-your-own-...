import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creates client socket
    client_socket.connect(('localhost', 8000)) # connects client socket to server socket at localhost:8000
    server_ip, server_port = client_socket.getpeername()
    client_ip, client_port = client_socket.getsockname()
    print(f"Connection established: CLI <{client_ip}:{client_port}> to SVR <{server_ip}:{server_port}>")
    while True:
        message = input("> ")
        if message.lower() == 'exit':
            break
        client_socket.sendall((message + "\n").encode('utf-8')) # processes client->server data to utf-8 format
        response = client_socket.recv(1024).decode('utf-8').strip() # processes server->client data from utf-8 format
        print(f"Server response: {response}")

if __name__ == "__main__":
    start_client()