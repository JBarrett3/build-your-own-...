# build-your-own-...

Goals:
 - I think we are building a database that will follow ACID principles. For now, we are just creating a basic database as it is.

Files:
 - server.py + client.py:
    - There is a client and server
    - The client and the server both have IP Addresses
    - The server creates a socket with a port that can be addressed as SVR_IP:SVR_PORT
    - The client creates a socket without a port can be addressed as CLI_IP:_
    - The client sends a request to the server and allocates a port for itself in the process, creating a TCP connection CLI_IP:CLI_PORT <-> SVR_IP:SCR_PORT
        - In this instance, the CLI_IP and SVR_IP are both my local computer (localhost = 127.0.0.1), the SVR_PORT is manually hardcoded to be 8000 arbitrarily (though this is a common choice), and the CLI_PORT is allocated from the dynamic port range (49152-65535)